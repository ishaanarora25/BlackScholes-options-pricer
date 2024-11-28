import requests_cache
import datetime
import yfinance as yf

class InvalidTicker(Exception):
    '''
    Exception for when an invalid ticker is input into the function
    '''
    pass

class history:

    @staticmethod
    def get_price(ticker):
        '''
        Retrieve and cache current stock price of given ticker using the yfinance API

        Param:
        ticker: desired stock's ticker symbol
        '''

        try:
            stock = yf.Ticker(ticker)

            price = stock.history(period="1d")['Close'].iloc[-1]

            return price
        except Exception as e:
            raise InvalidTicker(e)