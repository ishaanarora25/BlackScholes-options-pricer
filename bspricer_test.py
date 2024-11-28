from bspricer.pricer import BlackScholesPricer as bsp
from bspricer.history import history

test_option = bsp(100, 100, 0.1, 0.2, 3)

print(f'Call price = {bsp.get_call_price(test_option)}')
print(f'Put price = {bsp.get_put_price(test_option)}')

stock_price = history.get_price('AAPL')
print(f'Stock price = {stock_price}')
