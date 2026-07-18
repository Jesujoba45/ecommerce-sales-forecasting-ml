from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load("sales_forecast_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect form data
    data = [
        float(request.form['Discount']),
        float(request.form['Profit']),
        int(request.form['Quantity']),
        int(request.form['Category']),
        int(request.form['Sub_Category']),
        int(request.form['Region']),
        int(request.form['Segment']),
        int(request.form['Ship_Mode']),
        int(request.form['Order_Month']),
        int(request.form['Order_Year']),
        int(request.form['Order_DayOfWeek'])
    ]

    # Predict
    prediction = model.predict([data])[0]
    return render_template('index.html', prediction_text=f"Predicted Sales: ₦{prediction:.2f}")

if __name__ == '__main__':
    app.run(debug=True)
