Resume Screening App

A Resume Screening App that uses Machine Learning and Natural Language Processing (NLP) to automate the process of screening resumes. This app streamlines the hiring process by identifying and ranking candidates based on relevant skills, experience, and qualifications. The web interface is built with Flask.

Features
Machine Learning-Powered Resume Screening: Uses an NLP model to extract relevant information from resumes, such as skills, experience, and education.
Keyword Matching: Compares resumes with job descriptions based on keywords and ranks candidates accordingly.
Custom Scoring Criteria: Adjust the screening criteria (e.g., years of experience, specific skills) to fit different job roles.
File Upload: Supports resume uploads in various formats like PDF, DOCX, and TXT.
Admin Dashboard: View and manage screened resumes, ranked by relevance to job requirements.
Tech Stack
Backend: Flask (Python)
Machine Learning:
NLP Libraries: spaCy, NLTK
Machine Learning Framework: scikit-learn, TensorFlow or PyTorch
Model Types: Logistic Regression, Random Forest, or a custom-built classifier for resume screening
Frontend: HTML, CSS, JavaScript (Flask templates)
Database: SQLite / PostgreSQL (optional for storing resumes and results)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/resume-screening-app.git
cd resume-screening-app
Install dependencies: Create and activate a virtual environment, then install the required packages.

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Set up environment variables: Create a .env file to store any required environment variables like secret keys or database URIs.

env
Copy code
FLASK_APP=app.py
FLASK_ENV=development
Train the machine learning model: Train your NLP model using the provided dataset or your own resumes.

bash
Copy code
python train_model.py
Run the app:

bash
Copy code
flask run
Navigate to http://127.0.0.1:5000/ to view the app.

Usage
Upload Resumes: Upload resumes in PDF or DOCX format.
Run Screening: The model will analyze the resumes, extract relevant information, and rank candidates based on matching criteria.
View Results: Check the dashboard for ranked resumes and detailed reports.
Model Training
Data: Use a dataset of resumes and job descriptions to train the model.
Preprocessing: The resumes are parsed using NLP tools like spaCy or NLTK to extract features such as skills, job titles, and education.
Model: Train a classifier (e.g., Logistic Regression, Random Forest, etc.) on these features to rank resumes based on job descriptions.
Example of Feature Extraction:
Skills Matching: Identify and compare the skills listed in the resume against job requirements.
Experience Calculation: Parse job history and calculate years of experience.
Education Matching: Compare degrees and certifications against job criteria.
API Endpoints
POST /upload: Upload a resume to be screened.
GET /results: Get a list of screened resumes with relevance scores.
POST /train: Trigger training of the model using new data (optional).
Screenshots
(Include images of your web app interface, admin dashboard, and results screen here)

Contributing
We welcome contributions! If you'd like to improve this project, follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/your-feature).
Create a new Pull Request.