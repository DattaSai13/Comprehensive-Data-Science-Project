from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

churn_model = pickle.load(open("churn_model.pkl", "rb"))
house_model = pickle.load(open("house_model.pkl", "rb"))
sales_model = pickle.load(open("sales_model.pkl", "rb"))


@app.route("/")
def home():
    return "Capstone ML API Running"


@app.route("/predict_churn", methods=["POST"])
def predict_churn():
    data = request.json["features"]
    prediction = churn_model.predict([data])
    return jsonify({"Churn_Prediction": int(prediction[0])})


@app.route("/predict_house", methods=["POST"])
def predict_house():
    data = request.json["features"]
    prediction = house_model.predict([data])
    return jsonify({"House_Price": float(prediction[0])})


@app.route("/predict_sales", methods=["POST"])
def predict_sales():
    data = request.json["features"]
    prediction = sales_model.predict([data])
    return jsonify({"Sales_Prediction": float(prediction[0])})


if __name__ == "__main__":
    app.run(debug=True)