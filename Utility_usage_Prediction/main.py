import pandas as pd
from model import predict_usage

while True:
    print("1. Add Usage")
    print("2. Update Usage")
    print("3. View Data")
    print("4. Predict Usage")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            month = int(input("Enter Month: "))
            units = int(input("Enter Units: "))

            # Read existing data
            df = pd.read_csv("data.csv")

            # Create new row
            new_data = pd.DataFrame({
                "Month": [month],
                "Units": [units]
            })

            # Add new row
            df = pd.concat([df, new_data], ignore_index=True)

            # Save back to CSV
            df.to_csv("data.csv", index=False)

            print("Data added successfully!")

        except Exception as e:
            print("Error:", e)

    elif choice == "2":
        try:
            month = int(input("Enter Month to Update: "))
            new_units = int(input("Enter New Units: "))

            df = pd.read_csv("data.csv")

            if month in df["Month"].values:
                df.loc[df["Month"] == month, "Units"] = new_units
                df.to_csv("data.csv", index=False)
                print("Data updated successfully!")
            else:
                print("Month not found!")

        except Exception as e:
            print("Error:", e)

    elif choice == "3":
        try:
            df = pd.read_csv("data.csv")
            print("\nCurrent Data:")
            print(df)
        except FileNotFoundError:
            print("data.csv not found!")

    elif choice == "4":
        try:
            month = int(input("Enter Future Month: "))
            result = predict_usage(month)
            print(f"\nPredicted Usage: {result:.2f} Units")
        except Exception as e:
            print("Error:", e)

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")