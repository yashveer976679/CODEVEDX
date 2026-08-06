import pandas as pd
import matplotlib.pyplot as plt
from model import predict_marks, model_accuracy

while True:
    print("\n===== Student Performance Prediction System =====")
    print("1. Add Student Data")
    print("2. View Student Data")
    print("3. Predict Final Marks")
    print("4. Show Charts")
    print("5. Show Model Accuracy")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            attendance = int(input("Enter Attendance (%): "))
            study_hours = int(input("Enter Study Hours: "))
            internal_marks = int(input("Enter Internal Marks: "))
            final_marks = int(input("Enter Final Marks: "))

            try:
                df = pd.read_csv("student_data.csv")
            except FileNotFoundError:
                df = pd.DataFrame(columns=["Attendance", "StudyHours", "InternalMarks", "FinalMarks"])

            new_student = pd.DataFrame({
                "Attendance": [attendance],
                "StudyHours": [study_hours],
                "InternalMarks": [internal_marks],
                "FinalMarks": [final_marks]
            })

            df = pd.concat([df, new_student], ignore_index=True)
            df.to_csv("student_data.csv", index=False)

            print("Student data added successfully!")
        except Exception as e:
            print("Error:", e)

    elif choice == "2":
        try:
            df = pd.read_csv("student_data.csv")
            print("\nStudent Data:")
            print(df)
        except FileNotFoundError:
            print("student_data.csv not found!")

    elif choice == "3":
        try:
            attendance = int(input("Enter Attendance (%): "))
            study_hours = int(input("Enter Study Hours: "))
            internal_marks = int(input("Enter Internal Marks: "))

            result = predict_marks(attendance, study_hours, internal_marks)

            print(f"\nPredicted Final Marks: {result}")

        except Exception as e:
            print("Error:", e)
    elif choice == "4":
        try:
            df = pd.read_csv("student_data.csv")

            # Attendance vs Final Marks
            plt.figure(figsize=(6,4))
            plt.scatter(df["Attendance"], df["FinalMarks"])
            plt.title("Attendance vs Final Marks")
            plt.xlabel("Attendance")
            plt.ylabel("Final Marks")
            plt.grid(True)
            plt.show()

            # Study Hours vs Final Marks
            plt.figure(figsize=(6,4))
            plt.scatter(df["StudyHours"], df["FinalMarks"])
            plt.title("Study Hours vs Final Marks")
            plt.xlabel("Study Hours")
            plt.ylabel("Final Marks")
            plt.grid(True)
            plt.show()

            # Internal Marks vs Final Marks
            plt.figure(figsize=(6,4))
            plt.scatter(df["InternalMarks"], df["FinalMarks"])
            plt.title("Internal Marks vs Final Marks")
            plt.xlabel("Internal Marks")
            plt.ylabel("Final Marks")
            plt.grid(True)
            plt.show()

        except Exception as e:
            print("Error:", e)

    elif choice == "5":
        try:
            accuracy = model_accuracy()
            print(f"\nModel Accuracy: {accuracy}%")
        except Exception as e:
            print("Error:", e)

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")