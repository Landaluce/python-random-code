import numpy
from sklearn import linear_model


def main():
    # Reshaped for Logistic function.
    x = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1, 1)
    y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

    logr = linear_model.LogisticRegression()
    logr.fit(x, y)

    # predict if tumor is cancerous where the size is 3.46mm:
    predicted = logr.predict(numpy.array([3.46]).reshape(-1, 1))
    print('Prediction:', 'No' if predicted[0] == 0 else 'Yes')

    log_odds = logr.coef_
    odds = numpy.exp(log_odds)

    print('For every 1mm the tumor grows, the odds of being cancerous increase by', odds[0][0])


if __name__ == "__main__":
    main()
