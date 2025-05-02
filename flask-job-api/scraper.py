import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Job, Base
import schedule
from datetime import datetime
import os
from database import  SessionLocal

# Load environment variables
from dotenv import load_dotenv
load_dotenv()
db = SessionLocal()
# Logging configuration
logging.basicConfig(filename='scraper.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless for automation
chrome_options.add_argument("--disable-gpu")

def scrape_jobs():
    logging.info("Scraping started...")
    try:
        driver = webdriver.Chrome(service=Service(), options=chrome_options)
        driver.get("https://www.actuarylist.com/")

        # Wait for job listings to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Job_grid-section__kgIsR"))
        )

        job_cards = driver.find_elements(By.CSS_SELECTOR, "article")
        scraped_count = 0

        for card in job_cards:
            try:
                title = card.find_element(By.CLASS_NAME, "Job_job-card__position__ic1rc").text
                company = card.find_element(By.CLASS_NAME, "Job_job-card__company__7T9qY").text
                location = card.find_element(By.CLASS_NAME, "Job_job-card__country__GRVhK").text

                # Check if job already exists
                existing_job = db.query(Job).filter_by(title=title, company=company, location=location).first()
                if not existing_job:
                    new_job = Job(title=title, company=company, location=location)
                    db.add(new_job)
                    db.commit()
                    scraped_count += 1

            except Exception as e:
                logging.error(f"Error parsing card: {str(e)}")
                continue
            finally:
                db.close()

        logging.info(f"Scraping complete. {scraped_count} new jobs added.")
        driver.quit()

    except Exception as e:
        logging.error(f"Scraping failed: {str(e)}")


# Get the interval (in seconds) from the environment variable
job_interval_seconds = os.getenv("JOB_SCHEDULES_EVERY_SECOND")  # For testing set seconds in .env

# Check if the variable exists and is a valid number
if job_interval_seconds is not None:
    if job_interval_seconds.isdigit():  # Check if the value is numeric
        schedule.every(int(job_interval_seconds)).seconds.do(scrape_jobs)
        print(f"Job scheduled to run every {job_interval_seconds} seconds.")
    else:
        print(f"Invalid value for JOB_SCHEDULES_EVERY_SECOND: {job_interval_seconds}. Must be a number.")
else:
    print("JOB_SCHEDULES_EVERY_SECOND not set in the environment. Skipping job scheduling.")

# Load and split schedule times
schedule_times = os.getenv("JOB_SCHEDULES", "").split(",")

# Register jobs for each time
for sched_time in schedule_times:
    clean_time = sched_time.strip()
    if clean_time:
        schedule.every().day.at(clean_time).do(scrape_jobs)
        print(f"Scheduled job at {clean_time}")

# Uncomment for real cron-like scheduling and comment the above line
# schedule.every().day.at("00:00").do(scrape_jobs)
# schedule.every().day.at("03:00").do(scrape_jobs)
# schedule.every().day.at("06:00").do(scrape_jobs)

if __name__ == "__main__":
    logging.info("Starting job scraper...")
    scrape_jobs()  # First run immediately
    while True:
        schedule.run_pending()
        time.sleep(1)
