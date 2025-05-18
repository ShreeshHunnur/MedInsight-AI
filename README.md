# 🩺 MedInsight-AI

**MedInsight-AI** is a machine learning-powered web application designed to predict the risk of heart disease and diabetes. It provides users with an intuitive interface to input health metrics and receive real-time risk assessments, aiming to assist in early detection and promote proactive health management.

---

## 🚀 Features

- **Heart Disease Risk Prediction**: Utilizes a Gaussian Naive Bayes model trained on heart disease datasets.
- **Diabetes Risk Prediction**: Employs a Logistic Regression model trained on the BRFSS 2015 dataset.
- **User-Friendly Interface**: Interactive web application built with Flask, featuring HTML templates and static assets.
- **Data Visualization**: Presents insights and predictions in an accessible format for users.

---

## 🗂️ Project Structure

```
MedInsight-AI/
├── app.py
├── templates/
│   └── [HTML template files]
├── static/
│   └── [CSS, JS, and image files]
├── Heart_Disease_Prediction.csv
├── diabetes_012_health_indicators_BRFSS2015.csv
├── heart-disease-GaussianNB-model.pkl
├── diabetes-model-logistic-regression.pkl
├── model_machine_learning_cardio_health_risk.ipynb
├── .gitignore
└── README.md
```

- `app.py`: Main Flask application script.
- `templates/`: Contains HTML templates for rendering web pages.
- `static/`: Holds static files like CSS, JavaScript, and images.
- `*.csv`: Datasets used for training and evaluation.
- `*.pkl`: Serialized machine learning models.
- `model_machine_learning_cardio_health_risk.ipynb`: Jupyter notebook detailing the model training process.

---

## 🛠️ Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ShreeshHunnur/MedInsight-AI.git
   cd MedInsight-AI
   ```

2. **Create and Activate a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:

   ```bash
   python app.py
   ```

   The application will start on `http://127.0.0.1:5000/`. Open this URL in your web browser to access the app.

---

## 📊 Usage

- Navigate to the home page.
- Select either the Heart Disease or Diabetes prediction tool.
- Input the required health metrics.
- Submit the form to receive a risk assessment based on the provided data.

---

## 📈 Model Training

The `model_machine_learning_cardio_health_risk.ipynb` notebook provides a comprehensive walkthrough of the data preprocessing, model training, and evaluation processes for both heart disease and diabetes prediction models.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeatureName`.
3. Commit your changes: `git commit -m 'Add your feature'`.
4. Push to the branch: `git push origin feature/YourFeatureName`.
5. Open a pull request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## ⚠️ Disclaimer

This application is intended for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider regarding medical conditions or concerns.

---

*Developed by [Shreesh Hunnur](https://github.com/ShreeshHunnur)*
