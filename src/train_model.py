import pandas as pd

try:
    import joblib
except ImportError:
    try:
        from sklearn.externals import joblib
    except ImportError as error:
        raise ImportError(
            "joblib is not installed. Install it using 'pip install joblib'."
        ) from error

try:
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_absolute_error, r2_score
except ImportError as error:
    raise ImportError(
        "scikit-learn is not installed. Install it using 'pip install scikit-learn'."
    ) from error


# Load the dataset
data = pd.read_csv("../data/driving_data.csv")

print("\nDataset Loaded Successfully\n")
print(data)


# Select input features
X = data[
    [
        "speed",
        "terrain",
        "braking",
        "acceleration"
    ]
]


# Select output target
y = data["energy_consumption"]


# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create Random Forest Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# Train the model
model.fit(X_train, y_train)

print("\nModel Training Completed Successfully")


# Test the model
predictions = model.predict(X_test)


# Evaluate performance
mae = mean_absolute_error(
    y_test,
    predictions
)

r2 = r2_score(
    y_test,
    predictions
)


print("\n===== MODEL PERFORMANCE =====")

print(
    "Mean Absolute Error:",
    round(mae, 2),
    "kWh/100km"
)

print(
    "R2 Score:",
    round(r2, 2)
)


# Save the trained model
joblib.dump(
    model,
    "../models/ev_model.pkl"
)

print(
    "\nModel saved successfully as ev_model.pkl"
)

print("\nTraining Completed!")