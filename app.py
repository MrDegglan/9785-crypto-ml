from crypt import methods
from math import fabs
from flask import Flask, render_template, request

app = Flask(__name__)
PREDICT_ENABLED = None


@app.route('/')
def welcome():
    PREDICT_ENABLED = False
    return render_template('index.html', predict=PREDICT_ENABLED)


@app.errorhandler(404)
def pageNotFound():
    return render_template('error.html'), 404


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        PREDICT_ENABLED = True
        model = request.form['model']

        return render_template('index.html', predict=PREDICT_ENABLED, model=model) 

    if request.method == 'GET':
        return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
