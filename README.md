# E-commerce Sales Forecasting using Machine Learning

A machine learning project that predicts e-commerce sales using historical sales data. This project demonstrates the complete machine learning workflow, from data preprocessing and exploratory data analysis (EDA) to model training, evaluation, and deployment with Flask.

---

## Project Overview

Accurate sales forecasting is essential for inventory management, financial planning, and business decision-making. This project applies Machine Learning techniques to forecast sales using an e-commerce dataset.

The project covers the complete data science lifecycle including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Building
- Model Evaluation
- Hyperparameter Tuning
- Model Deployment using Flask

---

## Objectives

The objectives of this project are to:

- Predict future sales using historical e-commerce data.
- Compare machine learning performance for sales prediction.
- Improve prediction accuracy through hyperparameter tuning.
- Deploy the trained model as a web application.

---

## Dataset

The dataset contains historical e-commerce transaction records including:

- Order Date
- Ship Date
- Customer Information
- Product Category
- Region
- Sales
- Quantity
- Discount
- Profit

Target Variable:

- **Sales**

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Flask
- Joblib
- Jupyter Notebook

---

## Project Structure

```
ecommerce-sales-forecasting-ml/
│
├── data/
│   └── stores_sales_forecasting.csv
│
├── notebook/
│   └── Sales_Forecasting.ipynb
│
├── model/
│   └── sales_forecast_model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── images/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Exploratory Data Analysis

The following analyses were performed:

- Distribution of Sales
- Sales by Category
- Discount vs Sales Relationship
- Correlation Analysis
- Actual vs Predicted Sales Comparison

---

## Machine Learning Model

The model used is:

- **Random Forest Regressor**

Hyperparameter tuning was performed using **GridSearchCV** to improve prediction performance.

---

## Model Performance

| Metric | Value |
|---------|--------|
| R² Score | **0.7053** |
| RMSE | **300.52** |
| MAE | **122.69** |

The tuned Random Forest model achieved good predictive performance and generalized well on unseen data.

---

## Features

- Data preprocessing
- Feature engineering
- Machine learning prediction
- Hyperparameter tuning
- Model evaluation
- Flask web application
- Sales prediction interface

---

## How to Run the Project

### Clone the repository


### Navigate into the project

```bash
cd ecommerce-sales-forecasting-ml
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Project Screenshots

You can include screenshots such as:

- Sales Distribution
- Sales by Category
- Actual vs Predicted Plot
- Flask Home Page
- Prediction Result

---

## Future Improvements

- Deploy on Render or Railway
- Build an interactive Streamlit dashboard
- Time Series Forecasting
- Deep Learning implementation
- Docker containerization
- REST API development

---

## Author

**Oyeboade Solomon**

Applied Statistics Student | Data Analyst | Machine Learning Enthusiast

### Skills

- Python
- Machine Learning
- Data Analysis
- SPSS
- R
- Power BI
- Flask
- Git & GitHub

---

## Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

It helps others discover the project and supports my work.

---

## 📄 License

This project is licensed under the MIT License.
