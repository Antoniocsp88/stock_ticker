from flask import Flask
import joblib
import csv
from datetime import datetime
from src.business_logic.process_query import create_business_logic, create_business_logic2
from src.IO.get_data_from_yahoo import get_last_close, get_live_price, get_last_last_close

#from src.IO.storage_tools import get_model_from_bucket

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return f'Hello you should use an other route:!\nEX: get_stock_val/<ticker>\n'


@app.route('/get_stock_val/<ticker>', methods=['GET'])
def get_stock_value(ticker):
    bl = create_business_logic()
    bl2 = create_business_logic2()
    prediction = bl.do_predictions_for(ticker)
    prediction2 = bl2.do_predictions_for(ticker)
    last_close = get_last_close(ticker)
    live_price = get_live_price(ticker)
    before_yesterday_close = get_last_last_close(ticker)
    return f'<br/><br/>{ticker} prediction for last close: {prediction}' \
           f'<br/><br/>{ticker} last close: {last_close}' \
           f'<br/><br/>{ticker} prediction for next close: {prediction2}' \
           f'<br/><br/>{ticker} live price: {live_price}' \
           f'<br/><br/>{ticker} previous close: {before_yesterday_close}<br/><br/>'


if __name__ == '__main__':
    # Used when running locally only. When deploying to Cloud Run,
    # a webserver process such as Gunicorn will serve the app.
    app.run(host='localhost', port=9999, debug=True)
