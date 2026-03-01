# 🚀 Final Capstone Project – End-to-End Machine Learning System  
## Customer Churn, House Price & Sales Prediction

---

## 📌 Project Overview

This capstone project demonstrates a complete end-to-end data science workflow integrating:

- Data preprocessing
- Feature engineering
- Machine learning model development
- Model evaluation
- Model deployment via REST API
- Business impact analysis

The system solves three real-world business problems:

1. Customer Churn Prediction (Classification)  
2. House Price Estimation (Regression)  
3. Sales Forecasting (Regression)  

This project represents a production-ready, modular machine learning system designed for real-world business applications.

---

## 🎯 Project Objectives

- Build a scalable and modular ML system
- Implement classification and regression models
- Apply industry-standard preprocessing techniques
- Evaluate models using appropriate metrics
- Deploy trained models using Flask API
- Translate predictions into actionable business insights

---

## 📊 Datasets Used

### 🧑‍💼 Customer Churn Dataset
- Tenure
- Monthly Charges
- Total Charges
- Contract Type
- Payment Method
- Churn (Target Variable)
- 500+ records

---

### 🏠 House Price Dataset
- Area
- Bedrooms
- Location
- Price (Target Variable)
- 300+ records

---

### 📈 Sales Dataset
- Product
- Quantity
- Region
- Total Sales (Target Variable)
- 100+ records

---

## 🏗 Project Architecture


Data → Preprocessing → Model Training → Evaluation →
Model Serialization → Flask API → Prediction Output


This architecture ensures:

- Modular structure
- Scalability
- Reusability
- Deployment readiness

---

## 📂 Project Structure


Final_Capstone_Project/
│
├── README.md
├── capstone_project.ipynb
│
├── src/
│ ├── preprocessing.py
│ ├── train_model.py
│ ├── evaluate.py
│ └── predict.py
│
├── data/
│ ├── raw_data.csv
│ └── cleaned_data.csv
│
├── reports/
│ ├── technical_documentation.pdf
│ └── business_report.pdf
│
├── deployment/
│ ├── app.py
│ └── requirements.txt
│
└── presentation/
└── final_presentation.pptx


---

## 🧠 Machine Learning Models Used

### 🔹 Customer Churn Model
Algorithm: Random Forest Classifier  
Evaluation Metrics:
- Accuracy
- Precision
- Recall
- F1 Score

---

### 🔹 House Price Model
Algorithm: Random Forest Regressor  
Evaluation Metrics:
- Mean Absolute Error (MAE)
- R² Score

---

### 🔹 Sales Forecast Model
Algorithm: Random Forest Regressor  
Evaluation Metrics:
- Mean Absolute Error (MAE)
- R² Score

---

## 📈 Model Performance (Sample Results)

| Model | Metric | Result |
|--------|--------|--------|
| Churn | Accuracy | 91% |
| House Price | R² | 0.82 |
| Sales | R² | 0.88 |

These results demonstrate strong predictive performance across classification and regression tasks.

---

## ⚙️ Preprocessing Techniques

- Label Encoding for categorical variables
- Standard Scaling for numerical features
- Train-Test Split (80/20)
- Feature cleaning and transformation

Scaling ensures balanced feature contribution during training.

---

## 🚀 Model Deployment

The system is deployed using a Flask REST API.

### ▶️ How To Run Deployment

```bash
cd deployment
pip install -r requirements.txt
python app.py

Open in browser:

http://127.0.0.1:5000/
📡 Example API Call

POST Request:

{
  "features": [1, 24, 75.5, 1800, 1, 0]
}

Response:

{
  "Churn_Prediction": 1
}
📊 Business Impact
🔹 Customer Churn

Early churn detection reduces revenue loss

Enables targeted retention strategies

Improves customer lifetime value

🔹 House Pricing

Improves pricing accuracy

Reduces undervaluation risks

Enhances market competitiveness

🔹 Sales Forecasting

Optimizes inventory planning

Improves revenue forecasting

Supports strategic planning

🧪 Testing & Validation

80/20 Train-Test Split

Model evaluation on unseen data

Deployment tested via API

JSON response validation confirmed

🌟 Key Highlights

End-to-end ML lifecycle

Classification + Regression implementation

Deployment-ready architecture

Business-driven modeling approach

Professional modular project structure

🔮 Future Improvements

Cloud deployment (AWS / Azure)

Add Gradient Boosting / XGBoost

Build Streamlit dashboard UI

Implement automated retraining pipeline

Add real-time monitoring
