# 🩺 Diabetes Prediction Web App (Machine Learning + Streamlit)

A simple and interactive **Machine Learning web app** that predicts the risk of diabetes based on medical input parameters. Built using **Streamlit** and a trained **TensorFlow/Keras model**.

---

## 🚀 Live Demo
If deployed on Streamlit Cloud:
https://your-app-link.streamlit.app

---

## 📌 Project Overview
This project predicts whether a person is at **low risk or high risk of diabetes** using 8 medical features. The model is trained on healthcare data and deployed as a web app using Streamlit.

---

## 🧠 Machine Learning Model
- Model Type: Deep Learning (Neural Network)
- Framework: TensorFlow / Keras
- Preprocessing: StandardScaler (saved as `scaler.pkl`)
- Output: Binary Classification (0 = Low Risk, 1 = High Risk)

---

## 📊 Input Features
The model takes the following inputs:

- Pregnancies  
- Glucose Level  
- Blood Pressure  
- Skin Thickness  
- Insulin  
- BMI  
- Diabetes Pedigree Function  
- Age  

---

## 🛠️ Tech Stack
- Python 🐍  
- Streamlit 🎈  
- TensorFlow / Keras 🤖  
- NumPy  
- Pandas  
- Scikit-learn  
- Pickle  

---


## ⚙️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/diabetes-predictor.git
cd diabetes-predictor

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

streamlit run app.py
 ```


## 🚀 Future Improvements

- Add probability score (e.g., 78% risk instead of just High/Low classification)
- Improve model accuracy using better feature engineering and tuning
- Add charts and data visualization for insights (BMI vs Age, Glucose trends, etc.)


- Add user authentication for personalized health history tracking
