from enum import Enum, auto
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn import tree


class Nationality(Enum):
    """
    Enum representing nationalities with numerical values.

    Attributes:
        UK: Nationality UK with value 0.
        USA: Nationality USA with value 1.
        N: Nationality N with value 2.
    """
    UK = auto()
    USA = auto()
    N = auto()


class Decision(Enum):
    """
    Enum representing decision outcomes with numerical values.

    Attributes:
        YES: Decision outcome YES with value 1.
        NO: Decision outcome NO with value 0.
    """
    YES = auto()
    NO = auto()


def convert_nationality_to_int(value: str) -> int:
    """
    Converts a single categorical value to its numerical label using Enum.

    Args:
        value: A categorical value to be converted.

    Returns:
        The numerical label corresponding to the input categorical value.
    """
    return Nationality[value].value


def create_decision_tree(data: dict) -> DecisionTreeClassifier:
    """
    Creates a decision tree from the input data.

    Args:
        data: The initial data.

    Returns:
        The trained DecisionTreeClassifier model.
    """
    df = pd.DataFrame.from_dict(data)

    # Change string values to numerical using Enum
    df['Nationality'] = df['Nationality'].apply(lambda x: Nationality[x].value)
    df['Go'] = df['Go'].apply(lambda x: Decision[x].value)

    # Separate the feature columns from the target column
    features = ['Age', 'Experience', 'Rank', 'Nationality']
    features_df = df[features]
    target_df = df['Go']

    # Train the decision tree model
    decision_tree = DecisionTreeClassifier()
    decision_tree.fit(features_df, target_df)

    save_decision_tree(decision_tree, features)

    return decision_tree


def save_decision_tree(decision_tree: DecisionTreeClassifier, features: list) -> None:
    """
    Saves the decision tree plot to a file.

    Args:
        decision_tree: The trained DecisionTreeClassifier model.
        features: List of feature names.
    """
    plt.figure(figsize=(10, 5))
    tree.plot_tree(decision_tree, feature_names=features, filled=False)
    plt.tight_layout(pad=3.0)
    plt.savefig("decision_tree.png")


def predict_new_applicant(dtree: DecisionTreeClassifier, new_applicant: dict) -> str:
    """
    Predicts the outcome for a new applicant using a trained decision tree model.

    Args:
        dtree: The trained DecisionTreeClassifier model.
        new_applicant: A dictionary containing feature values for the new applicant.

    Returns:
        The predicted outcome ('YES' or 'NO') for the new applicant.
    """
    # Convert categorical feature 'Nationality' to numerical label using Enum
    new_applicant['Nationality'] = Nationality[new_applicant['Nationality']].value

    # Create a DataFrame for the new applicant's data
    new_applicant_df = pd.DataFrame([new_applicant])

    # Use the decision tree to predict the outcome
    prediction = dtree.predict(new_applicant_df[['Age', 'Experience', 'Rank', 'Nationality']])

    return Decision(prediction[0]).name


def main():
    data = {
        'Age': [36, 42, 23, 52, 43, 44, 66, 35, 52, 35, 24, 18, 45],
        'Experience': [10, 12, 4, 4, 21, 14, 3, 14, 13, 5, 3, 3, 9],
        'Rank': [9, 4, 6, 4, 8, 5, 7, 9, 7, 9, 5, 7, 9],
        'Nationality': ['UK', 'USA', 'N', 'USA', 'USA', 'UK', 'N', 'UK', 'N', 'N', 'USA', 'UK', 'UK'],
        'Go': ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'YES', 'YES', 'YES', 'YES', 'NO', 'YES', 'YES']
    }

    decision_tree = create_decision_tree(data)

    new_applicant = {
        'Age': 30,
        'Experience': 5,
        'Rank': 7,
        'Nationality': 'USA'
    }
    result = predict_new_applicant(decision_tree, new_applicant)
    print(f"Predicted outcome for new applicant: {result}")


if __name__ == "__main__":
    main()
