# 🏥 HealthRisk AI Assistant

An AI-powered healthcare risk assessment platform built using Flask, Machine Learning, SQLite, and Google Gemini AI.

## 📌 Project Overview

HealthRisk AI Assistant helps healthcare professionals analyze patient health records and identify potential health risks using machine learning and artificial intelligence.

The system predicts patient risk levels based on blood report parameters, generates AI-powered health recommendations, and provides an interactive dashboard for managing patient records.

---

## 🚀 Features

### Patient Management

* Add New Patient
* View Patient Records
* Edit Patient Information
* Delete Patient Records

### AI & Machine Learning

* Health Risk Prediction Model
* AI-Generated Health Recommendations
* Automated Health Score Calculation

### Analytics Dashboard

* Total Patients Count
* Low Risk Patients Count
* Medium Risk Patients Count
* High Risk Patients Count
* Risk Distribution Pie Chart

### Patient Insights

* Detailed Patient Profile Page
* Health Score Visualization
* Risk Level Classification
* AI Health Analysis

### Reports

* PDF Report Generation
* Download Patient Reports

### Emergency Alert System

* Detect Critical Health Conditions
* Highlight High-Risk Patients
* Alert Banner for Immediate Attention

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

### Backend

* Python
* Flask
* Flask-SQLAlchemy

### Database

* SQLite

### Machine Learning

* Scikit-Learn
* Joblib

### Artificial Intelligence

* Google Gemini AI

### Reporting

* ReportLab

---

## 📊 Health Parameters Used

The system analyzes:

* Glucose Level
* Haemoglobin Level
* Cholesterol Level

Based on these parameters, the model predicts:

* Low Risk
* Medium Risk
* High Risk

---

## 📂 Project Structure

health-risk-ai/

├── app.py

├── models.py

├── prediction.py

├── ai_service.py

├── train_model.py

├── model.pkl

├── requirements.txt

├── static/

│ └── style.css

├── templates/

│ ├── dashboard.html

│ ├── add_patient.html

│ ├── edit_patient.html

│ └── patient_details.html

└── README.md

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Praneetha200/health-risk-ai-assistant.git

cd health-risk-ai-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 🎯 Future Enhancements

* Email Health Reports
* Patient History Tracking
* Doctor Authentication System
* AI Diet Recommendations
* Health Trend Analysis
* Cloud Deployment

---

## 👩‍💻 Author

**Praneetha Tripurana**

Aspiring Software Engineer | Java Spring Boot Developer | AI & ML Enthusiast

GitHub:
https://github.com/Praneetha200
