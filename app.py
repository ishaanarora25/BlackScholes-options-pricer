import streamlit as st
from bspricer.pricer import BlackScholesPricer as bsp

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

with st.container():
    col1, col2, col3 = st.columns([2, 2, 2], gap='medium')  # Adjust column widths
    
    # Inputs for the Black-Scholes model
    with col1:
        stock_price = st.number_input("Stock Price (S)", min_value=0.0, value=100.0, step=0.01)
        exercise_price = st.number_input("Exercise Price (K)", min_value=0.0, value=100.0, step=0.01)
    with col2:
        volatility = st.number_input("Volatility (σ)", min_value=0.0, max_value=1.0, value=0.2, step=0.01)
        time_to_maturity = st.number_input("Time to Maturity (T, in years)", min_value=0.0, value=1.0, step=0.1)
    with col3:
        risk_free_rate = st.number_input("Risk-Free Rate (r)", min_value=0.0, max_value=1.0, value=0.05, step=0.01)

# Add a "Calculate" button
if st.button("Calculate"):

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