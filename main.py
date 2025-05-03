import streamlit as st

st.set_page_config(page_title="Lagora Dashboard", layout="wide")

st.title("Lagora: Week 2 Dashboard")
st.markdown("Welcome to the central control panel for all modules.")

st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Go to", ["Portfolio", "Model Lab", "Statement Library"])

if page == "Portfolio":
    st.subheader("Portfolio Manager")
    st.write("Track holdings, prices, and performance here.")
elif page == "Model Lab":
    st.subheader("Model Lab")
    st.write("Run simulations and build custom financial models.")
elif page == "Statement Library":
    st.subheader("Statement Library")
    st.write("View and analyze company filings and financials.")
