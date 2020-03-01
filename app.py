# Importing the necessary libraries
import numpy as np
import pandas as pd
from flask import Flask, request, render_template, abort
import pickle

from city_ids import get_cityid
import error_handlers

# Creating the flast app
app = Flask(__name__)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', city=city_name, state=state), 404


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

# prediction function `


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 13)
    model = pickle.load(open('model.pkl', 'rb'))
    result = model.predict(to_predict)
    return result[0]


@app.route('/predict', methods=['POST'])
def predict():
    global state
    global city_name
    '''
    For rendering results on HTML GUI
    '''
    to_predict_list = request.form.to_dict()
    to_predict_list = list(to_predict_list.values())
    state, city_name = to_predict_list[0], to_predict_list[1]

    # Removing the first element from the list
    to_predict_list.pop(0)
    # Adding the city id in the first position of the list
    to_predict_list[0] = get_cityid(state, city_name)

    if to_predict_list[0] == '0':
        print(to_predict_list)
        abort(404)
        # return render_template("500.html"), 500
    else:
        pred = ValuePredictor(to_predict_list)

        # If prediction is 1 means the customer is going to renew the subscription and
        # 0 means the customer is not going to renew the subscription
        if pred == 1:
            output = "Yes"
        else:
            output = "No"

        return render_template('index.html', prediction_text='Will customer renew the subscription : {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
    app.run()
