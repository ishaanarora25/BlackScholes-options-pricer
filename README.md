# BlackScholes-options-pricer

## Overview

This repository contains an interactive Streamlit web app to calculate option prices using the Black-Scholes model. The app allows users to input parameters for a call or put option and instantly computes the option price using the Black-Scholes model, allowing users to also fetch the current stock price of a given stock by inputting its ticker symbol. It also graphically depicts how the value of the call and put option has changed over the past month as a result of the change in price of the given underlying stock.

## Project Structure

```
BlackScholes-options-pricer/
    |--- bspricer/
    |        |--- __init__.py
    |        |--- history.py
    |        |--- pricer.py
    |--- .gitignore
    |--- LICENSE 
    |--- README.md
    |--- environment.yml
    |--- bspricer_test.py
    |--- app.py
```

## About

- ```environment.yml```: Conda virtual environment specs
- ```bspricer/```: Black-Scholes Options Pricer package
  - ```bspricer/history.py```: module that fetches current and historical prices of given tickers using yfinance
  - ```bspricer/pricer.py```: module that uses the Black-Scholes model to compute the price of a call or put option, given specific parameters
  - ```bspricer/__init__.py```: initialization for bspricer as a package
- ```bspricer_test.py```: test file to test the modules in the bspricer package
- ```app.py```: interactive streamlit web app to calculate option prices using the Black-Scholes model


## References

- prudhvi-reddy-m's [Black-Scholes] (https://github.com/prudhvi-reddy-m/BlackScholes) implementation
- krivi95's [option-priciing-models] (https://github.com/krivi95/option-pricing-models) implementation

## Dependencies

- ```yfinance```: to fetch current and historical stock prices
- ```streamlit```: to build and deploy the web app
- ```numpy```: for numerical processing
- ```numpy```: for advanced numerical processing
- ```streamlit-echarts```: to plot graphs


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.