try:
    from joblib import load
except ImportError:
    import pickle

    def load(path):
        with open(path, "rb") as f:
            return pickle.load(f)

import pandas as pd
from driving_tips import generate_tips


# Load trained AI model
model = load(
    "../models/ev_model.pkl"
)


print("\n========== EV Efficiency Predictor ==========\n")


# User input
speed = float(
    input("Enter vehicle speed (km/h): ")
)


terrain = int(
    input(
        "Enter terrain (0 = Flat, 1 = Uphill, 2 = Downhill): "
    )
)


braking = int(
    input(
        "Enter braking level (1-5): "
    )
)


acceleration = int(
    input(
        "Enter acceleration level (1-5): "
    )
)


# Prepare data for prediction
input_data = pd.DataFrame(
    [
        [
            speed,
            terrain,
            braking,
            acceleration
        ]
    ],
    columns=[
        "speed",
        "terrain",
        "braking",
        "acceleration"
    ]
)


# Predict energy consumption
prediction = model.predict(
    input_data
)


energy = prediction[0]


# Display result
print("\n========== RESULT ==========")

print(
    "Predicted Energy Consumption:",
    round(energy, 2),
    "kWh/100 km"
)


# Generate AI recommendations
tips = generate_tips(
    speed,
    terrain,
    braking,
    acceleration,
    energy
)


print("\n===== AI Driving Recommendations =====")


for number, tip in enumerate(tips, start=1):
    print(
        f"{number}. {tip}"
    )


print("\nThank you for using the EV Efficiency Optimizer!")