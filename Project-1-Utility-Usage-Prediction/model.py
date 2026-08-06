import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_usage(month):
    # Read the CSV file
    df = pd.read_csv("data.csv")

    # Input (Month)
    X = df[["Month"]]

    # Output (Units)
    y = df["Units"]

    # Create and train model
    model = LinearRegression()
    model.fit(X, y)

    # Predict
    future_month = pd.DataFrame({"Month": [month]})
    prediction = model.predict(future_month)

    return prediction[0]