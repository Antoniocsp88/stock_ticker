from datetime import datetime, timedelta

from yahoo_fin import stock_info as si


def get_last_stock_price(ticker, last=False):
    if last:
        now = datetime.now()
        today6pm = now.replace(hour=18, minute=0, second=0, microsecond=0)
        if now < today6pm:
            delta = 2
        else:
            delta = 1
        yesterday = now - timedelta(days=delta)
        start_date = yesterday - timedelta(days=30)
        #print(si.get_data(ticker, start_date, yesterday))######
        return si.get_data(ticker, start_date, yesterday)

    return si.get_data(ticker)


def get_last_stock_price2(ticker, last=False):
    if last:
        now = datetime.now()
        start_date = now - timedelta(days=30)
        #print(si.get_data(ticker, start_date, yesterday))######
        return si.get_data(ticker, start_date, now)

    return si.get_data(ticker)


def get_last_close(ticker):
    now = datetime.now()
    #print(si.get_data(ticker, now, now))######
    df_price = si.get_data(ticker, now, now)
    if df_price['adjclose'].empty:
        return df_price.iloc[0]['open']
    else:
        return df_price.iloc[0]['adjclose']

def get_last_last_close(ticker):
    now = datetime.now()
    yesterday = now - timedelta(days=1)
    #print(si.get_data(ticker, yesterday, now))######
    df_price = si.get_data(ticker, yesterday, now)
    if df_price['adjclose'].empty:
        return df_price.iloc[0]['open']
    else:
        return df_price.iloc[0]['adjclose']



def get_live_price(ticker):
    #print(si.get_live_price(ticker))######
    return si.get_live_price(ticker)


