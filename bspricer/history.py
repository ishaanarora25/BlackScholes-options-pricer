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
        Retrieve current stock price of given ticker using the yfinance API

        Param:
        ticker: desired stock's ticker symbol
        '''

        try:
            stock = yf.Ticker(ticker)

            price = stock.history(period="1d")['Close'].iloc[-1]

            return price
        except Exception as e:
            raise InvalidTicker(e)
    
    @staticmethod
    def get_price_history(ticker):
        '''
        Retrieve last month's stock price history of given ticker using the yfinance API

        Param:
        ticker: desired stock's ticker symbol
        '''

        try:
            data = yf.Ticker(ticker).history(period="1mo")

            return data
        except Exception as e:
            raise InvalidTicker(e)
