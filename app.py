from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import random

app = Flask(__name__)

# Load the model

model_heart = joblib.load('heart-disease-GaussianNB-model.pkl')
model_sugar = joblib.load('diabetes-model-logistic-regression.pkl')

@app.route('/')
def form():
    return render_template('home.html')

@app.route('/diabetes')
def diabetes_page():
    return render_template('diabetes.html')

@app.route('/heart')
def heart_page():
    return render_template('heart.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/predict_heart', methods=['POST'])
def predictHeart():
    # Retrieve data from form
    try:
        # Log incoming data for debugging
        print("Received form data:", request.form)

        # Extract and convert form data using the correct keys
        data = [
            float(request.form.get("age")),
            int(request.form.get("sex")),
            int(request.form.get("chest_pain")),  # updated key
            float(request.form.get("bp")),          # updated key
            float(request.form.get("cholesterol")), # updated key
            float(request.form.get("fbs")),
            int(request.form.get("ekg")),           # updated key
            float(request.form.get("max_hr")),      # updated key
            float(request.form.get("exercise_angina")), # updated key
            float(request.form.get("st_depression")),   # updated key
            int(request.form.get("slope_of_st")),   # updated key
            int(request.form.get("num_vessels")),    # updated key
            int(request.form.get("thallium"))        # updated key
        ]

        # Ensure all data points are valid
        if any(x is None for x in data):
            return jsonify({"error": "Missing input values."}), 400

    except ValueError as e:
        return jsonify({"error": f"Invalid input type: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 400

    # Predict using the model
    prediction = model_heart.predict([data])[0]
    result = "Heart disease detected" if prediction == 1 else "No heart disease detected"
    return jsonify({"result": result})

@app.route('/predict_sugar', methods=['POST'])
def predictSugar():
    try:
        # Log incoming data for debugging
        print("Received form data:", request.form)

        # Extract and convert form data for prediction
        data = [
            int(request.form.get("high_bp")),
            int(request.form.get("high_chol")),
            int(request.form.get("chol_check")),
            float(request.form.get("bmi")),
            int(request.form.get("smoker")),
            int(request.form.get("stroke")),
            int(request.form.get("heart_disease")),
            int(request.form.get("phys_activity")),
            int(request.form.get("fruits")),
            int(request.form.get("veggies")),
            int(request.form.get("hvy_alcohol")),
            int(request.form.get("any_healthcare")),
            int(request.form.get("no_docbc_cost")),
            int(request.form.get("gen_health")),
            int(request.form.get("ment_health")),
            int(request.form.get("phys_health")),
            int(request.form.get("diff_walk")),
            int(request.form.get("sex")),
            int(request.form.get("age"))
        ]

        # Check for missing data
        if any(x is None for x in data):
            return jsonify({"error": "Missing input values."}), 400

    except ValueError as e:
        return jsonify({"error": f"Invalid input type: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 400

    # Make the prediction using the model
    prediction = model_sugar.predict([data])[0]
    if prediction == 2:
        result = 'Diabetes Detected'
    else:
        result = 'No Diabetes Detected'
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
