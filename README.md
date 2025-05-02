# Job Listings App

The Job Listings App is a full-stack web application that allows users to browse, search, and view job listings. The backend is built with Flask and scrapes job data, while the frontend is built with React to provide a dynamic and responsive user interface.

## Table of Contents
- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
This application provides a platform to view and search job listings. The backend API, built with Flask, scrapes job data and stores it in a database. The frontend, built with React, consumes the API to display job listings in a user-friendly interface.

## Tech Stack
- **Backend**: Flask, Python, SQLAlchemy, MySQL
- **Frontend**: React, JavaScript, Axios
- **Database**: MySQL
- **Tools**: npm, pip, virtualenv

## Installation

### Prerequisites
- Git
- Python 3.8+
- Node.js and npm
- MySQL

### Clone the Repository
```bash
git clone https://github.com/your-username/job-listings-api.git
cd job-listings-api
```

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd flask-job-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file by copying `.env.example` in the `flask-job-api` directory.
   - Add the required values to the `.env` file (e.g., database credentials).

5. Set up the database:
   - Ensure PostgreSQL is running.
   - Create a database:
     ```sql
     CREATE DATABASE job_listings_db;
     ```

6. Run the Flask application:
   ```bash
   python app.py
   ```

7. (Optional) Run the scraper to populate the database with job listings:
   ```bash
   python scraper.py
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend-react-app
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables:
   - Create a `.env` file in the `frontend-react-app` directory.
   - Add the API base URL:
     ```env
     REACT_APP_API_BASE_URL=http://localhost:5000
     ```

4. Start the development server:
   ```bash
   npm start
   ```
   The frontend will be available at `http://localhost:3000`.

## Usage
- **Backend**: The Flask API runs on `http://localhost:5000` and provides endpoints for job listings.
- **Frontend**: The React app runs on `http://localhost:3000` and allows users to browse and search job listings.
- **Scraper**: Run `python scraper.py` to fetch and store job listings in the database.