from numpy import exp, sqrt, log
from scipy.stats import norm

class BlackScholesPricer:
    def __init__(self, stock_price, exercise_price, risk_free_rate, volatility, time_to_maturity):
        '''
        Initializes necessary variables for the Black-Scholes Pricing Model

        stock_price: current stock price of the underlying asset
        exercise_price: exercise price of the option contract
        risk_free_rate: return on risk-free assets
        volatility: standard deviation of the asset's log returns, which represents volatility of the underlying
        '''
        self.S = stock_price
        self.X = exercise_price
        self.r = risk_free_rate
        self.sigma = volatility
        self.T = time_to_maturity
        self.d1 = (log(self.S / self.X) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * sqrt(self.T))
        self.d2 = (log(self.S / self.X) + (self.r - 0.5 * self.sigma ** 2) * self.T) / (self.sigma * sqrt(self.T))
    
    def get_call_price(self):
        '''
        returns the price of a call option using the Black-Scholes Formula
        '''
        return self.S * norm.cdf(self.d1, 0.0, 1.0) - self.X * exp(-self.r * self.T) * norm.cdf(self.d2, 0.0, 1.0)

    def get_put_price(self):
        '''
        returns the price of a put option using the Black-Scholes Formula
        '''
        return self.X * exp(-self.r * self.T) * norm.cdf(-self.d2, 0.0, 1.0) - self.S * norm.cdf(-self.d1, 0.0, 1.0)