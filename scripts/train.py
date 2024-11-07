import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv("data/iris.csv")  # Sesuaikan path jika perlu

# Drop kolom 'Id' dan gunakan 'Species' sebagai target
X = data.drop(["Id", "Species"], axis=1)
y = data["Species"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate and save model
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions)}")

# Save the trained model
joblib.dump(model, "models/iris_model.pkl")  