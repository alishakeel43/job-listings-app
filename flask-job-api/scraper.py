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

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Set up logging
logging.basicConfig(filename='scraper.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

from database import session  # Import the session from database.py

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
                existing_job = session.query(Job).filter_by(title=title, company=company, location=location).first()
                if existing_job:
                    continue

                new_job = Job(title=title, company=company, location=location)
                session.add(new_job)
                scraped_count += 1
            except Exception as e:
                logging.error(f"Error parsing card: {str(e)}")
                continue

        session.commit()
        logging.info(f"Scraping complete. {scraped_count} new jobs added.")
        driver.quit()

    except Exception as e:
        logging.error(f"Scraping failed: {str(e)}")

# Schedule the job every 3 minutes (for testing)
schedule.every(1).seconds.do(scrape_jobs)

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
