import streamlit as st

st.set_page_config(
    page_title="PATEKAR AI SCALPER",
    page_icon="📈",
    layout="wide"
)

st.title("📈 PATEKAR AI SCALPER")
st.subheader("NIFTY & BANKNIFTY OPTIONS")

st.warning("PAPER TRADING MODE ONLY")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric("Virtual Capital", "₹50,000")

with col2:
    st.metric("Daily Max Loss", "₹2,000")

st.divider()

st.subheader("Market Status")

col1, col2 = st.columns(2)

with col1:
    st.info("NIFTY: WAIT")

with col2:
    st.info("BANKNIFTY: WAIT")

st.divider()

st.subheader("Trading Configuration")

st.write("Strike: ATM")
st.write("Expiry: Nearest Available")
st.write("Timeframe: 5 Minutes")

st.divider()

st.subheader("Paper Trading")

option = st.selectbox(
    "Select Instrument",
    ["NIFTY CE", "NIFTY PE",
     "BANKNIFTY CE", "BANKNIFTY PE"]
)

price = st.number_input(
    "Demo Entry Price",
    min_value=0.0,
    value=100.0
)

if st.button("BUY (VIRTUAL ONLY)"):
    st.success(
        f"Demo order recorded: {option} at ₹{price}"
    )

st.error("REAL BROKER ORDERS: DISABLED")
st.caption("No live market data or real orders connected yet.")
