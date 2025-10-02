import joblib
import json
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load dataset
with open("./landmarks_dataset.json", "r") as f:
    data = json.load(f)

X = []
y = []
num_skipped = 0

for i, sample in enumerate(data):
    seq = sample["sequence"]

    if not seq:
        print(f"Warning: Sample {i} has empty sequence, skipping.")
        num_skipped+=1
        continue

    # Convert dicts to numeric vectors
    seq_numeric = []
    for frame in seq:
        values = [frame[k] for k in sorted(frame.keys())]  # alphabetical order
        seq_numeric.append(values)

    seq_array = np.array(seq_numeric)  # shape = (frames, features)

    # Summarize sequence: mean, std, min, max per feature
    features = np.concatenate([
        seq_array.mean(axis=0),
        seq_array.std(axis=0),
        seq_array.min(axis=0),
        seq_array.max(axis=0)
    ])

    X.append(features)
    y.append(sample["exercise_type"])

# Convert to numpy arrays
X = np.array(X)
y = np.array(y)

# Check
print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}")
print(f"First row of X: {X[0]}")
print(f"First label: {y[0]}")

# Encode Labels
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0, stratify=y
)

# Train RandomForest
model = RandomForestClassifier(max_depth=None, random_state=0)
model.fit(X_train, y_train)

# Eval
y_pred = model.predict(X_test)
print(f"Number of data points skipped: {num_skipped}")
print(classification_report(y_test, y_pred, target_names=encoder.classes_))

# Save Model
joblib.dump(model, "./models/exercise_classify_model.pkl")
joblib.dump(encoder, "./models/exercise_label_encoder.pkl")