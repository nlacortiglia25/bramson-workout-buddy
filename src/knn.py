import json
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# -------------------------
# Load data
# -------------------------
with open("landmarks_dataset.json", "r") as f:
    data = json.load(f)

# -------------------------
# Build feature (joint) list
# -------------------------
all_keys = set()
for dataPoint in data:
    for frame in dataPoint.get("sequence", []):
        all_keys.update(frame.keys())

feature_names = sorted(all_keys)
print("Feature names (order used):", feature_names)

# -------------------------
# Helper: resample sequence to fixed length
# -------------------------
def resample_sequence(seq, target_len, feature_names):
    arr = np.array([[frame.get(k, np.nan) for k in feature_names] for frame in seq], dtype=float)
    current_len = len(arr)

    if current_len == 0:
        arr_resampled = np.full((target_len, len(feature_names)), np.nan)
    elif current_len == target_len:
        arr_resampled = arr
    else:
        idx = np.linspace(0, current_len - 1, target_len).astype(int)
        arr_resampled = arr[idx]

    return arr_resampled.flatten()

# -------------------------
# Build dataset X, y
# -------------------------
target_len = 50   # adjust as needed
X, y = [], []

for ex in data:
    vec = resample_sequence(ex.get("sequence", []), target_len, feature_names)
    X.append(vec)
    y.append(ex.get("exercise_type", "unknown"))

X = np.array(X, dtype=float)
y = np.array(y)

# -------------------------
# Preprocess: impute missing, scale, encode labels
# -------------------------
imputer = SimpleImputer(strategy="mean")
X_imputed = imputer.fit_transform(X)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

le = LabelEncoder()
y_enc = le.fit_transform(y)
print("Classes:", le.classes_)

# -------------------------
# Train/test split
# -------------------------
try:
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y_enc, test_size=0.2, random_state=42, stratify=y_enc
    )
except ValueError:
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y_enc, test_size=0.2, random_state=42
    )

# -------------------------
# Grid-search KNN
# -------------------------
param_grid = {"n_neighbors": [3, 5, 7, 9, 11], "weights": ["uniform", "distance"]}
knn = KNeighborsClassifier()
grid = GridSearchCV(knn, param_grid, cv=5, n_jobs=-1, scoring="accuracy")
grid.fit(X_train, y_train)

best_knn = grid.best_estimator_
print("Best params:", grid.best_params_)

# -------------------------
# Evaluate
# -------------------------
y_pred = best_knn.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Test accuracy: {acc:.4f}")

print("\nClassification report:")
print(classification_report(y_test, y_pred, target_names=le.classes_))

print("\nConfusion matrix (rows=true, cols=pred):")
print(confusion_matrix(y_test, y_pred))

# -------------------------
# Predict on new sequence
# -------------------------
def predict_sequence(seq):
    """seq: list of frames (dicts). Returns predicted exercise class."""
    vec = resample_sequence(seq, target_len, feature_names).reshape(1, -1)
    vec = imputer.transform(vec)
    vec = scaler.transform(vec)
    pred_idx = best_knn.predict(vec)[0]
    return le.inverse_transform([pred_idx])[0]

# Example:
# new_seq = [{"elbow_angle": 45, "shoulder_angle": 90}, {"elbow_angle": 50, "shoulder_angle": 92}, ...]
# print("Predicted exercise:", predict_sequence(new_seq))
