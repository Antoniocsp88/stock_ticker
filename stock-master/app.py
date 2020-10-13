from flask import Flask
import joblib
import csv
from datetime import datetime
from src.business_logic.process_query import create_business_logic
from src.IO.get_data_from_yahoo import get_last_price, get_live_price

#from src.IO.storage_tools import get_model_from_bucket

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return f'Hello you should use an other route:!\nEX: get_stock_val/<ticker>\n'


@app.route('/get_stock_val/<ticker>', methods=['GET'])
def get_stock_value(ticker):
    bl = create_business_logic()
    prediction = bl.do_predictions_for(ticker)
    last_close = get_last_price(ticker)
    live_price = get_live_price(ticker)
    return f'<br/><br/>{ticker} prediction: {prediction}<br/><br/>{ticker} last close: {last_close}' \
           f'<br/><br/>{ticker} live price: {live_price}<br/><br/>'


#@app.route('/get_pkl/<ticker>', methods=['GET'])
#def get_pkl(ticker):
#    file_name = ticker+".pkl"
#    with open(file_name, 'rb') as f:
#        joblib.load(f)
#    print(f)
#    return f'a'


#@app.route('/get_model/<ticker>', methods=['GET'])
#def get_model(ticker):
#    file_name = ticker+".pkl"
#    model = get_model_from_bucket(file_name, 'model_bucket_9876_100')
#    print(model)
#    return f'a'


if __name__ == '__main__':
    # Used when running locally only. When deploying to Cloud Run,
    # a webserver process such as Gunicorn will serve the app.
    app.run(host='localhost', port=9999, debug=True)
