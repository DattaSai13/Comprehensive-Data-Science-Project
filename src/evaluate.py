from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score


def evaluate_churn(model, X_test, y_test):
    preds = model.predict(X_test)
    print("Churn Accuracy:", accuracy_score(y_test, preds))


def evaluate_regression(model, X_test, y_test, name):
    preds = model.predict(X_test)
    print(f"{name} MAE:", mean_absolute_error(y_test, preds))
    print(f"{name} R2:", r2_score(y_test, preds))