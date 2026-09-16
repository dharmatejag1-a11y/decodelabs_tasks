"""
Project 2: Data Classification Using AI

This project loads a small Iris dataset, explores it,
splits it into training/testing data, and trains a
simple classification model.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


def main():
    # 1. Load the dataset
    data = pd.read_csv("iris.csv")

    print("First 5 rows of the dataset:")
    print(data.head())

    print("\nDataset shape:", data.shape)
    print("\nClass distribution:")
    print(data["species"].value_counts())

    # 2. Separate features and target
    X = data.drop("species", axis=1)
    y = data["species"]

    # 3. Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    print("\nTraining samples:", len(X_train))
    print("Testing samples:", len(X_test))

    # 4. Create and train a simple classification model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    # 5. Make predictions
    y_pred = model.predict(X_test)

    # 6. Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)

    print("\nModel Accuracy:", round(accuracy * 100, 2), "%")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # 7. Predict a new sample
    sample = [[5.1, 3.5, 1.4, 0.2]]
    prediction = model.predict(sample)

    print("Prediction for sample", sample[0], ":", prediction[0])


if __name__ == "__main__":
    main()
