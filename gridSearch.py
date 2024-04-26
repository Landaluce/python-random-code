import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn import datasets


def find_best_c(x: np.ndarray, y: np.ndarray) -> float:
    """
    Finds the best regularization parameter (C) for Logistic Regression using cross-validation.

    This function performs a search for the best regularization parameter (C) by fitting
    Logistic Regression models with different values of C and selecting the one that maximizes
    the accuracy score on the provided dataset.

    Args:
        x: Input features (numpy array or array-like).
        y: Target labels (numpy array or array-like).

    Returns:
        The best value of C that maximizes the model accuracy.
    """
    logit = LogisticRegression(max_iter=10000)
    cs = [round(x, 2) for x in np.arange(0.05, 2.05, 0.05)]
    scores = []

    for choice in cs:
        logit.set_params(C=choice)
        logit.fit(x, y)
        scores.append(logit.score(x, y))

    idx = scores.index(max(scores))
    return cs[idx]


def main() -> None:
    """
    Main function to demonstrate finding the best regularization parameter (C)
    for Logistic Regression on the Iris dataset.
    """
    iris = datasets.load_iris()
    x = iris['data']
    y = iris['target']

    c = find_best_c(x, y)
    logit = LogisticRegression(max_iter=10000, C=c)
    logit.fit(x, y)

    accuracy = logit.score(x, y)
    print("Model accuracy:", accuracy)


if __name__ == "__main__":
    main()
