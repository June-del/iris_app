from flask import Flask, request, render_template
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Create the Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = np.array(features).reshape(1, -1)
    prediction = model.predict(final_features)[0]

    # Map species to image URLs
    images = {
        "Iris-setosa": "https://upload.wikimedia.org/wikipedia/commons/5/56/Iris_setosa_2.jpg",
        "Iris-versicolor": "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
        "Iris-virginica": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg"
    }

    return render_template("index.html",
                           prediction_text=f"Prediction: {prediction}",
                           flower_image=images[prediction])

if __name__ == "__main__":
    print("🚀 Flask server starting...")
    app.run(debug=True, host="0.0.0.0", port=5000)
