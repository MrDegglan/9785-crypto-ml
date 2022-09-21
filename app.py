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
        if request.form['model'] == 'default':
            error = 'No model selected. Please select a model.'
            return render_template('error.html', error=error)
        # Insert logic to get result from model

        result = None # will be changed...
        return render_template('index.html', predict=PREDICT_ENABLED, result=result, model=request.method['model']) 

    if request.method == 'GET':
        return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
