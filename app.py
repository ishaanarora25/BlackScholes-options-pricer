import streamlit as st
from bspricer.pricer import BlackScholesPricer as bsp
from bspricer.history import history, InvalidTicker
from datetime import datetime, timedelta

st.title("Black-Scholes Options Pricer")

st.markdown("""
<style>

[data-testid="stMetric"] {
    background-color: #393939;
    text-align: center;
    padding: 15px 0;
}

[data-testid="stMetricLabel"] {
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>
""", unsafe_allow_html=True)

if "stock_ticker" not in st.session_state:
    st.session_state["stock_ticker"] = ""
if "stock_price" not in st.session_state:
    st.session_state["stock_price"] = 100.0
if "error_message" not in st.session_state:
    st.session_state["error_message"] = ""

def update_price_on_ticker():
    '''
    Callback to set default stock price when the ticker is entered    
    '''
    st.session_state.error_message = ""
    
    try:
        st.session_state.stock_price = history.get_price(st.session_state.stock_ticker)
    except InvalidTicker as e:
        st.session_state.error_message = "Invalid ticker!"
    

def clear_ticker_on_price_change():
    '''
    Callback to clear the ticker when the stock price is changed
    '''
    st.session_state.stock_ticker = ""
    st.session_state.error_message = ""

current_date = datetime.now().date()

with st.container():
    col1, col2, col3 = st.columns([2, 2, 2], gap='medium')  # Adjust column widths
    
    # Inputs for the Black-Scholes model
    with col1:
        stock_ticker = st.text_input("Underlying Stock Ticker (Optional)", value=st.session_state.stock_ticker, on_change=update_price_on_ticker, key="stock_ticker")
        if st.session_state.error_message:
            st.error(st.session_state.error_message)
        exercise_price = st.number_input("Exercise Price (K)", min_value=0.0, value=100.0, step=0.01)
    with col2:
        stock_price = st.number_input("Stock Price (S)", min_value=0.0, value=st.session_state.stock_price, on_change=clear_ticker_on_price_change, step=0.01)
        expiration_date = st.date_input("Expiration Date", min_value=current_date + timedelta(days=1))
    with col3:
        volatility = st.number_input("Volatility (σ)", min_value=0.0, max_value=1.0, value=0.2, step=0.01)
        risk_free_rate = st.number_input("Risk-Free Rate (r)", min_value=0.0, max_value=1.0, value=0.05, step=0.01)

# Add a "Calculate" button
if st.button("Calculate"):
    
    time_to_maturity = ((expiration_date - current_date).days) / 365.0

    option = bsp(stock_price=stock_price, exercise_price=exercise_price, risk_free_rate=risk_free_rate, volatility=volatility, time_to_maturity=time_to_maturity)
    call_price = bsp.get_call_price(option)
    put_price = bsp.get_put_price(option)
    
    # Display results in a centered container
    with st.container():
        st.subheader("Option Prices")
        col1, col2 = st.columns([3, 3])
        with col1:
            st.metric(label="Call Option Value", value="${:,.2f}".format(call_price))
        with col2:
            st.metric(label="Put Option Value", value="${:,.2f}".format(put_price))