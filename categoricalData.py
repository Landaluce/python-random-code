import pandas as pd
from sklearn import linear_model


def main():
    cars = pd.read_csv("cars_data.csv")
    ohe_cars = pd.get_dummies(cars[['Car']])
    x = pd.concat([cars[['Volume', 'Weight']], ohe_cars], axis=1)
    y = cars['CO2']

    model = linear_model.LinearRegression()
    model.fit(x, y)

    # predict the CO2 emission of a Volvo where the weight is 2300kg, and the volume is 1300cm3:
    predicted_co2 = model.predict([[2300, 1300, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])

    print(predicted_co2[0])


if __name__ == "__main__":
    main()
