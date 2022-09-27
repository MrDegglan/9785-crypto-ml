import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
PREDICT_ENABLED = None


def format_datetime(input):

    split_datetime = input.split('T')
    raw_date = split_datetime[0]
    raw_time = split_datetime[1]

    split_date = raw_date.split('-')
    split_time = raw_time.split(':')

    print(split_date)
    print(split_time)

def predict_money(year, month, day, hour):
    # Add prediction logic here

    return


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
        # Receive datetime from template
        predict_list = request.form.to_dict()
        predict_list = list(predict_list.values())
        print(request.form['input'])
        format_datetime(request.form['input'])

        result = None # will be changed...
        return render_template('index.html', predict=PREDICT_ENABLED, result=result) 

    if request.method == 'GET':
        return render_template('error.html')


<<<<<<< HEAD
def predict_money(hour, day, month, year):
    hour = 0
    


=======
>>>>>>> 279a918 (Redid form inputs and split datetime function)
if __name__ == '__main__':
    lstm_model = pickle.load(open('pickles/RNN_LSTM_SIMPLE.pkl', 'rb'))
    gru_model = pickle.load(open('pickles/RNN_GRU_SIMPLE.pkl', 'rb'))
    app.run(debug=True, port=5000)
