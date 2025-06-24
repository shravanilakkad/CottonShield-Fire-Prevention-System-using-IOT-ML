from flask import Flask, render_template
import joblib
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

# Load Firebase credentials
cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://iotproject-d01d2-default-rtdb.firebaseio.com"
})

# Load your trained ML model
model = joblib.load("fire_hazard_model.pkl")  # Make sure this model exists in your project folder

@app.route('/')
def home():
    ref = db.reference("sensor")
    data = ref.get()

    try:
        # Extract sensor values
        temperature = float(data.get("temperature", 0))
        humidity = float(data.get("humidity", 0))
        gas_value = float(data.get("gas", 0))

        # Prepare features for prediction
        features = [temperature, humidity, gas_value]
        prediction = model.predict([features])[0]
        probability = model.predict_proba([features])[0][1] * 100

        # Set result message
        result = "🔥 FIRE HAZARD DETECTED 🔥" if prediction == 1 else "✅ SAFE"

        # Pass data to template
        return render_template(
            "home.html",
            result=result,
            prob=round(probability, 2),
            data={
                "Temperature": temperature,
                "Humidity": humidity,
                "Gas_Value": gas_value
            }
        )

    except Exception as e:
        print("Error:", e)
        return render_template("home.html", result="⚠️ Error in prediction", prob=0, data={})

if __name__ == '__main__':
    app.run(debug=True)
