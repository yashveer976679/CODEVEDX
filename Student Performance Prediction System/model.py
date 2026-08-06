import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def predict_marks(attendance, study_hours, internal_marks):
    # Read student data
    df = pd.read_csv("student_data.csv")

    # Input features
    X = df[["Attendance", "StudyHours", "InternalMarks"]]

    # Target value
    y = df["FinalMarks"]

    # Train the model
    model = LinearRegression()
    model.fit(X, y)

    # Create input for prediction
    student = pd.DataFrame({
        "Attendance": [attendance],
        "StudyHours": [study_hours],
        "InternalMarks": [internal_marks]
    })

    # Predict final marks
    prediction = model.predict(student)
    return round(prediction[0], 2)

def model_accuracy():
    # Read data
    df = pd.read_csv("student_data.csv")

    # Features
    X = df[["Attendance", "StudyHours", "InternalMarks"]]

    # Target
    y = df["FinalMarks"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Calculate R² Score
    score = r2_score(y_test, y_pred)

    return round(score * 100, 2)

    return round(prediction[0], 2)