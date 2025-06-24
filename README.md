# 🔥 CottonShield - Fire Hazard Detection System

CottonShield is an intelligent fire hazard detection system built using **IoT sensors**, **Firebase**, and **Machine Learning**. It monitors real-time temperature, humidity, and gas values to detect early fire risks, alert users, and display a live dashboard via a web app.

---

## 🧠 Project Summary

- **Hardware**: DHT22 (Temperature & Humidity), MQ2 & MQ135 (Gas Sensors), NodeMCU ESP8266, Active Buzzer
- **Cloud**: Firebase Realtime Database (sensor data storage)
- **Machine Learning**: Random Forest / XGBoost / ANFIS models
- **Frontend**: Live dashboard (HTML + CSS + JS)
- **Backend**: Python Flask server for ML prediction and data handling

---

## 📦 Features

- 🔁 Real-time sensor data logging to Firebase
- 🤖 ML prediction (Safe or Fire Hazard)
- 📊 Live dashboard with auto-updating values
- 🚨 Buzzer alert for hazard detection
- 🌐 Web hosting for remote access

---

## 🛠️ Hardware Components

| Component       | Description                        |
|----------------|------------------------------------|
| NodeMCU ESP8266| Microcontroller with Wi-Fi         |
| DHT22          | Temperature & Humidity sensor      |
| MQ2 & MQ135    | Smoke, CO, and CO₂ gas sensors     |
| Active Buzzer  | Alerts when fire is predicted      |
| Breadboard + Jumper Wires | Prototyping connections    |

---

## 🧠 Machine Learning Model

| Algorithm         | Accuracy | F1 Score | Jaccard Score |
|------------------|----------|----------|----------------|
| Random Forest     | 97%      | 0.97     | 0.94           |
| XGBoost           | 96%      | 0.96     | 0.92           |
| ANFIS             | 95%      | 0.95     | 0.91           |
| Logistic Regression | 92%    | 0.93     | 0.87           |

Trained using synthetic + real sensor datasets. Final model is exported as `fire_hazard_model.pkl`.

---

## 🖥️ Web Dashboard

The dashboard displays:

- 🌡️ Temperature
- 💧 Humidity
- 🧪 Gas Value
- 🔥 Prediction Result (Safe / Fire Hazard)
- 🔄 Auto-refresh every 3 seconds

---

##  Firebase Setup

1. Go to [Firebase Console](https://console.firebase.google.com)
2. Create a new project
3. Add a Realtime Database
4. Enable **read/write rules**:
```json
{
  "rules": {
    ".read": "true",
    ".write": "true"
  }
}
