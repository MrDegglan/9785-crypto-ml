import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
PREDICT_ENABLED = None


def format_datetime(input):
    final_datetime: dict = None

    split_datetime = input.split('T')

    split_date = split_datetime[0].split('-')
    split_time = split_datetime[1].split(':')

    final_datetime.update("year", split_date[0])
    final_datetime.update("month", split_date[1])
    final_datetime.update("day", split_date[2])
    final_datetime.update("hour", split_time[0])

    print(final_datetime)
    return final_datetime

def predict_money(datetime: dict):
    # Add prediction logic here

    return


@app.route('/')
def welcome():
    return render_template('index.html', predict=PREDICT_ENABLED)


@app.errorhandler(404)
def pageNotFound():
    return render_template('error.html'), 404


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        # Receive datetime from template
        predict_list = request.form.to_dict()
        predict_list = list(predict_list.values())
        print(request.form['input'])
        datetime: dict = format_datetime(request.form['input'])
        result = predict_money(datetime)

        return render_template('predict.html', result=result) 

    if request.method == 'GET':
        return render_template('error.html')
    

if __name__ == '__main__':
    lstm_model = pickle.load(open('pickles/RNN_LSTM_SIMPLE.pkl', 'rb'))
    gru_model = pickle.load(open('pickles/RNN_GRU_SIMPLE.pkl', 'rb'))
    app.run(debug=True, port=5000)
