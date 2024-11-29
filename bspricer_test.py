from bspricer.pricer import BlackScholesPricer as bsp
from bspricer.history import history, InvalidTicker
import matplotlib.pyplot as plt

test_option = bsp(100, 100, 0.1, 0.2, 3)

print(f'Call price = {bsp.get_call_price(test_option)}')
print(f'Put price = {bsp.get_put_price(test_option)}')

# valid test for get_price
try:
    stock_price = history.get_price('AAPL')
    print(f'Stock price = {stock_price}')
except InvalidTicker as e:
    raise(e)

# invalid test for get_price
try:
    stock_price = history.get_price('AA12')
    print(f'Stock price = {stock_price}')
except InvalidTicker as e:
    print(e)

# valid test for get_price_history
try:
    data = history.get_price_history('AAPL')
    print(data)
except InvalidTicker as e:
    raise(e)

# invalid test for get_price_history
try:
    data = history.get_price('AA12')
    print(data)
except InvalidTicker as e:
    print(e)
