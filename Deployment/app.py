import pandas as pd
import numpy as np
from joblib import load
from flask import Flask, render_template
from flask import request
import pickle
from sklearn.neighbors import NearestNeighbors
# Create flask app
flask_app = Flask(__name__,template_folder='templates')

@flask_app.route("/")
def Home():
    return render_template("main.html")

@flask_app.route("/", methods = ["GET","POST"])
def predict():
    Gender = request.form.get("Gender", False)
    Age = request.form.get("Age", False)
    Scholarship = request.form.get("Scholarship", False)
    Hipertension = request.form.get("Hipertension", False)
    Diabetes = request.form.get("Diabetes", False)
    Alcoholism = request.form.get("Alcoholism", False)
    Handcap = request.form.get("Handcap", False)
    SMS_received = request.form.get("SMS_received", False)
    waitingTime = request.form.get("waitingTime", False)
    sameday = request.form.get("sameday", False)
    if int(waitingTime) == 0:
        sameday = 1
    else:
        sameday = 0
    model = load('modeleK.jublib')
    tp = ([[int(Gender),int(Age),int(Scholarship),int(Hipertension),int(Diabetes),int(Alcoholism),int(Handcap),int(SMS_received),int(waitingTime),int(sameday)]])
    prediction = model.predict(tp)
    if prediction == 0:
        result = "Will Not Show"
    else:
        result = "Will Show"
    return result


if __name__ == "__main__":
    flask_app.run(debug=True)