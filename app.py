from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("model/model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    years = float(request.form["years"])

    prediction = model.predict([[years]])

    salary = round(prediction[0], 2)

    return render_template(
        "index.html",
        prediction_text=f"Predicted Salary: ₹ {salary}"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
