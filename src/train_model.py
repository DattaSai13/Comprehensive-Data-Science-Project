import pickle
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor


def train_churn_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    pickle.dump(model, open("deployment/churn_model.pkl", "wb"))
    return model


def train_house_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    pickle.dump(model, open("deployment/house_model.pkl", "wb"))
    return model


def train_sales_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    pickle.dump(model, open("deployment/sales_model.pkl", "wb"))
    return model