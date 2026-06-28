# 🚗 AI-Powered EV Driving Efficiency Optimizer

An AI-based Machine Learning project that predicts **Electric Vehicle (EV) energy consumption** based on driving behavior and provides **personalized driving recommendations** to improve battery efficiency.

---

## 📌 Project Overview

Electric Vehicles are becoming increasingly popular, but driving behavior significantly affects battery performance and driving range.

This project uses **Machine Learning (Random Forest Regression)** to predict energy consumption based on driving parameters such as:

- Vehicle Speed
- Terrain
- Braking Level
- Acceleration Level

The system then provides AI-generated driving recommendations to help drivers maximize battery efficiency.

---

## 🎯 Objectives

- Predict EV energy consumption using Machine Learning.
- Analyze driving behavior.
- Suggest intelligent driving tips.
- Demonstrate AI applications in Electric Vehicles.

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Scikit-learn | Machine Learning |
| Joblib | Save & Load ML Model |
| VS Code | Development Environment |
| Git & GitHub | Version Control |

---

## 📂 Project Structure

```
AI-EV-Efficiency-Optimizer/
│
├── data/
│   └── driving_data.csv
│
├── models/
│   └── ev_model.pkl
│
├── src/
│   ├── train_model.py
│   ├── predictor.py
│   └── driving_tips.py
│
├── requirements.txt
└── README.md
```

---

## ⚙ Features

✔ Machine Learning Model Training

✔ Energy Consumption Prediction

✔ Intelligent Driving Recommendations

✔ Random Forest Regression

✔ Easy Command-Line Interface

---

## 📊 Dataset

The dataset contains simulated EV driving data with the following features:

| Feature | Description |
|----------|-------------|
| Speed | Vehicle speed (km/h) |
| Terrain | Flat, Uphill, Downhill |
| Braking | Braking intensity (1–5) |
| Acceleration | Acceleration level (1–5) |
| Energy Consumption | Battery consumption (kWh/100 km) |

---

## 🧠 Machine Learning Model

Algorithm Used:

**Random Forest Regressor**

Evaluation Metrics:

- Mean Absolute Error (MAE)
- R² Score

Example Result:

```
Mean Absolute Error : 1.83 kWh/100 km

R² Score : 0.90
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Sarkarishika/AI-EV-Efficiency-Optimizer.git
```

Go to the project directory

```bash
cd AI-EV-Efficiency-Optimizer
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Train the Model

```bash
cd src

python train_model.py
```

This generates:

```
models/ev_model.pkl
```

---

## ▶ Run Prediction

```bash
python predictor.py
```

Example:

```
Enter vehicle speed (km/h): 60

Terrain:
0 = Flat
1 = Uphill
2 = Downhill

Enter terrain: 0

Enter braking level: 2

Enter acceleration level: 3
```

Output:

```
Predicted Energy Consumption

14.52 kWh/100 km

AI Driving Recommendations

✔ Drive smoothly

✔ Avoid aggressive acceleration

✔ Maintain constant speed

✔ Use regenerative braking
```

---

## 💡 AI Driving Recommendations

The system provides personalized suggestions such as:

- Reduce excessive acceleration.
- Maintain steady speed.
- Avoid harsh braking.
- Drive efficiently on uphill terrain.
- Improve battery usage.

---

## 📈 Future Improvements

- Real-time IoT Sensor Integration
- Battery Temperature Prediction
- State of Charge (SOC) Estimation
- Battery Health Monitoring
- Streamlit Dashboard
- Mobile Application
- Cloud Deployment
- Deep Learning Model
- Live Vehicle Data

---

## 📸 Sample Output

```
========== EV Efficiency Predictor ==========

Vehicle Speed : 60 km/h

Terrain : Flat

Braking : 2

Acceleration : 3

----------------------------------------

Predicted Energy Consumption

14.52 kWh/100 km

----------------------------------------

AI Recommendations

✔ Smooth acceleration

✔ Good braking habits

✔ Maintain steady speed

✔ Efficient driving
```

---

## 🎓 Internship Project

This project was developed as part of an internship to demonstrate practical applications of:

- Machine Learning
- Data Analytics
- Electric Vehicle Technology
- Python Programming

---

## 👩‍💻 Author

**Ishika Sarkar**

GitHub:
https://github.com/Sarkarishika

LinkedIn:
https://www.linkedin.com/in/ishika-sarkar-1184aa267/

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.
