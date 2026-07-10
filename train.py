import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

# Load dataset
data = pd.read_csv("data/salary.csv")

# Split into feature (X) and target (y)
X = data[["YearsExperience"]]
y = data["Salary"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Create model directory if it doesn't exist
os.makedirs("model", exist_ok=True)

# Save model
joblib.dump(model, "model/model.pkl")

print("===================================")
print("Model trained successfully!")
print("Model saved at model/model.pkl")
print("===================================")
