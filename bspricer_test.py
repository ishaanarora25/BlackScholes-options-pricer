from bspricer.pricer import BlackScholesPricer as bsp

test_option = bsp(100, 100, 0.1, 0.2, 3)

print(f'Call price = {bsp.get_call_price(test_option)}')
print(f'Put price = {bsp.get_put_price(test_option)}')