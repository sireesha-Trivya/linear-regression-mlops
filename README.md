# 🚀 Linear Regression MLOps Project

An end-to-end Machine Learning project that predicts employee salary based on years of experience using a **Linear Regression** model. The application is built with **Flask**, containerized using **Docker**, and successfully deployed on an **AWS EC2** instance.

---

## 📌 Project Overview

This project demonstrates a complete Machine Learning workflow:

- Data preprocessing
- Model training using Scikit-learn
- Model serialization with Joblib
- Flask web application for predictions
- Docker containerization
- Deployment on AWS EC2

The application allows users to enter their years of experience and predicts the expected salary using the trained model.

---

## 🛠 Tech Stack

- Python 3
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- HTML
- Docker
- AWS EC2
- Git & GitHub

---

## 📂 Project Structure

```
linear-regression-mlops/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
│
├── data/
│   └── salary_data.csv
│
├── model/
│   ├── train.py
│   └── model.pkl
│
├── templates/
│   └── index.html
│
└── static/
```

---

## 📊 Dataset

The model is trained using a Salary Dataset containing:

- Years of Experience
- Salary

The objective is to predict salary based on the number of years of professional experience.

---

## ⚙️ Model Training

The training script:

- Loads the dataset
- Splits data into training and testing sets
- Trains a Linear Regression model
- Evaluates model performance
- Saves the trained model as:

```
model/model.pkl
```

---

## 🌐 Flask Application

The Flask application:

- Loads the trained model
- Accepts user input through a web interface
- Predicts salary
- Displays the prediction instantly

---

## 🐳 Dockerization

### Build Docker Image

```bash
docker build -t linear-regression-mlops:v1 .
```

### Run Docker Container

```bash
docker run -d -p 5000:5000 linear-regression-mlops:v1
```

Application URL:

```
http://localhost:5000
```

---

## ☁️ AWS EC2 Deployment

This project was successfully deployed on an AWS EC2 instance using Docker.

Deployment workflow:

- Launch EC2 instance
- Install Docker
- Clone GitHub repository
- Build Docker image
- Run Docker container
- Access the application through the EC2 public IP

> **Note:** The EC2 instance used for deployment has been terminated after successful validation to avoid unnecessary cloud costs.

---

## ▶️ Running Locally

Clone the repository

```bash
git clone https://github.com/<your-username>/linear-regression-mlops.git
```

Move into the project directory

```bash
cd linear-regression-mlops
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://localhost:5000
```

---

## 📷 Application Demo

Home Page

```
Enter Years of Experience
        ↓
Click Predict
        ↓
Predicted Salary Displayed
```

You can replace this section with screenshots of the application.

---

## 🚀 Future Improvements

- Add REST API endpoints
- Integrate CI/CD using Jenkins
- Deploy on Kubernetes
- Add model versioning with MLflow
- Implement monitoring with Prometheus & Grafana
- Add automated testing
- Deploy using GitHub Actions

---

## 🎯 Key Learning Outcomes

- Machine Learning model training
- Model serialization using Joblib
- Flask application development
- Docker containerization
- AWS EC2 deployment
- Git & GitHub version control
- End-to-end MLOps workflow

---

## 👩‍💻 Author

**Sireesha Buddha**

If you found this project helpful, consider giving it a ⭐ on GitHub.
