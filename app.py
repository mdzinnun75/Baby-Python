# from function2 package

# Way --> 1
import function2.demo48_shipping

function2.demo48_shipping.buy_sell()
# package.class.method

# Way --> 2
from function2.demo48_shipping import buy, sell, buy_sell
buy()
sell()
buy_sell()