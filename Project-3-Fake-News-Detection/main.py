from model import detect_news

while True:

    print("\n==============================")
    print(" AI Fake News Detection Tool")
    print("==============================")
    print("1. Detect Fake News")
    print("2. About Model")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nPaste your news below:\n")

        news = input()

        label, confidence = detect_news(news)

        print("\n==============================")
        print("Prediction :", label)
        print(f"Confidence : {confidence}%")
        print("==============================")

    elif choice == "2":

        print("\nModel Information")
        print("----------------------------")
        print("Algorithm : Logistic Regression")
        print("Vectorizer: TF-IDF")
        print("Dataset   : Kaggle Fake & Real News Dataset")

    elif choice == "3":

        print("\nThank you!")
        break

    else:

        print("\nInvalid Choice!")