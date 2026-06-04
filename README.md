# 🌸 Iris Flower Prediction App

A machine learning web application built with **Flask** and **Logistic Regression** to predict the species of an Iris flower (Setosa, Versicolor, Virginica) based on sepal and petal measurements.

---

## 🚀 Features
- Trains a model using the **Iris dataset**
- Web form for entering flower measurements
- Predicts flower species with a dedicated image for each type
- Runs locally, on your phone, or deployed online
- Styled with CSS for a clean, user-friendly interface

---

## 📂 Project Structure
iris_app/
│── app.py              # Flask web app
│── train_model.py      # Model training script
│── iris.csv            # Dataset
│── model.pkl           # Saved trained model
│── templates/
│    └── index.html     # Web form
│── static/
└── style.css      # Styling
└── images/        # Flower images (Setosa, Versicolor, Virginica)

Code

---

## 🛠 Installation & Setup

1. Clone the repo:
   git clone https://github.com/June-del/iris_app.git
   cd iris_app
2. Create a virtual environment:
python -m venv venv
.\venv\Scripts\activate
3. Install dependencies:
pip install -r requirements.txt
4. Train the model:
python train_model.py
5. Run the app:
python app.py
6. Open in browser:
http://127.0.0.1:5000
📱 Run on Phone
Connect your phone to the same Wi‑Fi as your computer
Use the IP shown in Flask logs (e.g., http://192.168.137.99:5000)
