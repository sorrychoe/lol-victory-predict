import joblib

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/15m', methods = ['POST', 'GET'])
def surrender():
    model = joblib.load('./model/model1.pkl')
    return render_template("15m.html")

@app.route('/full', methods = ['POST', 'GET'])
def full():
    model = joblib.load('./model/model2.pkl')
    return render_template("full_time.html") 

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        result = request.form
    return render_template("result.html", score = model.score()) 


if __name__ == "__main__":
    app.run()