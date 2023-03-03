import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor


def preprocess_dataframe(df):
    """Function to preprocess the dataframe

    Args:
        df (dataframe): dataframe that needs to preprocessed

    Returns:
        dataframe: preprocessed dataframe
    """

    print("preprocessing dataframe...")
    df["CITY"] = list(map(lambda city: city.split(",")[-1], df["ADDRESS"]))
    unique_cities = df["CITY"].unique()
    pd.DataFrame(unique_cities,
                 columns=['city']).to_csv("cities.csv", index=False)
    print("done processing.")
    return df


def make_X_Y(df):
    """Function to make dependent and independant variable

    Args:
        df (datafarme)

    Returns:
        dataframe, list
    """

    df = preprocess_dataframe(df)
    print("Creating pandas dummies...")
    dummies_city_df = pd.get_dummies(df.CITY, drop_first=True)
    df = pd.concat([df, dummies_city_df], axis="columns")

    print("making X_Y...")
    X = df.drop(
        columns=[
            "POSTED_BY",
            "BHK_OR_RK",
            "RERA",
            "RESALE",
            "ADDRESS",
            "LONGITUDE",
            "LATITUDE",
            "TARGET(PRICE_IN_LACS)",
            "CITY",
        ]
    )
    Y = df["TARGET(PRICE_IN_LACS)"]
    return X, Y


def train_and_save_model():
    """Function to train and save the model

    Returns:
        float: model score
    """

    df = pd.read_excel("city_house_price.xlsx")
    X, Y = make_X_Y(df)
    # split the data into training and testing
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

    # make the model object
    knr_model = KNeighborsRegressor()
    print("training the model...")
    knr_model.fit(X_train, Y_train)

    print("saving the model...")
    with open("knr_model", "wb") as model:
        pickle.dump(knr_model, model)
    score = knr_model.score(X_train, Y_train)

    print(f"done with score of {score}")
    return score


if __name__ == "__main__":
    # run this file only if you want to train the model again
    train_and_save_model()
