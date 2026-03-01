import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder


def load_datasets():
    sales = pd.read_csv("data/sales_data.csv")
    house = pd.read_csv("data/house_prices.csv")
    churn = pd.read_csv("data/customer_churn.csv")
    return sales, house, churn


def preprocess_churn(df):
    df = df.copy()

    le = LabelEncoder()
    for col in df.select_dtypes(include="object").columns:
        df[col] = le.fit_transform(df[col])

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return train_test_split(X_scaled, y, test_size=0.2, random_state=42)


def preprocess_house(df):
    df = df.copy()
    X = df.drop("Price", axis=1)
    y = df["Price"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return train_test_split(X_scaled, y, test_size=0.2, random_state=42)


def preprocess_sales(df):
    df = df.copy()
    X = df.drop("Total_Sales", axis=1)
    y = df["Total_Sales"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return train_test_split(X_scaled, y, test_size=0.2, random_state=42)