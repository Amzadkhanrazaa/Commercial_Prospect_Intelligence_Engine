# AI-Driven Lead Scoring & Customer Acquisition Engine

## Overview

This project is a machine learning powered **Lead Scoring System** that helps businesses identify high-value prospects and prioritize sales outreach.

The system analyzes behavioral engagement data such as:

* Website visits
* Pages viewed
* Time spent on site
* Email engagement
* Demo requests

Using machine learning, the system predicts the **probability of conversion** and assigns a **lead score** to each prospect.

This helps sales teams focus on leads most likely to convert, improving **customer acquisition efficiency**.

---

# System Architecture

Data Generation → Feature Engineering → Model Training → Model Evaluation → Lead Scoring → Database Storage → SQL Analytics → AI Insights

---

# Project Structure

```
AI-Driven-Lead-Scoring/
│
├── data/
│   └── prospect.csv
│
├── database/
│   ├── schema.sql
│   └── queries.sql
│
├── src/
│   ├── app.py
│   ├── config.py
│   ├── data_generator.py
│   ├── database_loader.py
│   ├── evaluate_model.py
│   ├── feature_engineering.py
│   ├── genai_engine.py
│   ├── logger.py
│   ├── scoring_engine.py
│   ├── sql_analytics.py
│   ├── train_model.py
│   └── utils.py
│
├── requirements.txt
└── README.md
```

---

# Features

* Synthetic CRM Data Generation
* Feature Engineering for Lead Engagement
* Machine Learning Lead Scoring Model
* Model Evaluation Metrics
* Automated Lead Ranking
* SQLite Database Integration
* SQL Analytics for Business Insights
* AI Generated Sales Recommendations

---

# Machine Learning Model

Algorithm Used:

Random Forest Classifier

Features used:

* Website Visits
* Pages Viewed
* Time Spent on Website
* Email Opens
* Demo Request
* Engagement Score

Target Variable:

```
Converted (1 = Converted, 0 = Not Converted)
```

---

# Evaluation Metrics

```
Accuracy: ~99%
Precision: 0.99
Recall: 1.00
F1 Score: 0.99
```

These metrics indicate the model effectively identifies high-value prospects.

---

# Example Output

Top Lead Scores

```
Name                Company              Lead Score
--------------------------------------------------
Kaitlyn Vasquez     Morales-Cohen           1.00
Joseph Sandoval     Jones Reynolds Smith    1.00
Patricia Rhodes     Morris LLC              1.00
```

---

# SQL Business Insights

Example Query:

Top Companies with Highest Lead Scores

```
SELECT company, AVG(lead_score)
FROM leads
GROUP BY company
ORDER BY 2 DESC
LIMIT 5
```

---

# Installation

Clone repository

```
git clone https://github.com/Amzadkhanrazaa/lead-scoring-engine.git
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Run the Project

```
python src/app.py
```

Pipeline execution:

1. Generate dataset
2. Train ML model
3. Evaluate model
4. Score leads
5. Store results in database
6. Run analytics

---

# Visualization Dashboard

Run Streamlit dashboard:

```
streamlit run dashboard.py
```

Dashboard displays:

* Lead score distribution
* Top converting leads
* Engagement metrics
* Company insights

---

# Tech Stack

Python
Pandas
Scikit-Learn
SQLite
Streamlit
Faker
NumPy

---

# Future Improvements

* Real CRM integration
* API deployment using FastAPI
* Lead scoring REST API
* Automated retraining pipeline
* Airflow data pipelines
* Customer Lifetime Value prediction
* LLM powered sales insights

---

# Use Cases

* SaaS Lead Qualification
* Marketing Campaign Optimization
* Sales Pipeline Prioritization
* Customer Acquisition Intelligence

---

# Author

Amzad Raza Khan

