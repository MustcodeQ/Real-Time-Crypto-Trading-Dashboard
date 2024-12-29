

# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.graph_objects as go
# import time
# from datetime import datetime
# import os
# import threading
# import time
# import random

# # # Navbar
# # st.sidebar.title("Crypto Signal Application")
# # menu = st.sidebar.radio("Navigation", ["Orders", "Feedbacks", "Backtesting", "Notebook Save"])

# # # Title
# # st.title("Enhanced SMA Crossover Strategy with Price Action")

# # # User inputs for SMA periods and timeframe
# # short_period = st.sidebar.number_input("Short SMA Period", min_value=1, value=10)
# # long_period = st.sidebar.number_input("Long SMA Period", min_value=1, value=50)
# # timeframe = st.sidebar.selectbox("Timeframe", ["1m", "5m", "15m", "1h", "1d"])

# # # Placeholder for cryptocurrency data (simulated)
# # st.subheader("Cryptocurrency Prices")
# # data = {
# #     "Time": pd.date_range(start="2023-01-01", periods=100, freq="H"),
# #     "Close": np.random.uniform(100, 200, 100)
# # }
# # df = pd.DataFrame(data)
# # st.line_chart(df["Close"], width=700, height=400)

# # # Calculate SMAs
# # short_sma = df["Close"].rolling(window=short_period).mean()
# # long_sma = df["Close"].rolling(window=long_period).mean()

# # # Generate buy and sell signals
# # momentum = df["Close"].pct_change(periods=10)
# # buy_signal = (short_sma > long_sma) & (momentum > 0)
# # sell_signal = (short_sma < long_sma) & (momentum < 0)

# # df["Buy Signal"] = buy_signal

# # # Display buy and sell signals
# # st.subheader("Signals")
# # st.write("Buy Signals:", df[buy_signal][["Time", "Close"]])
# # st.write("Sell Signals:", df[sell_signal][["Time", "Close"]])

# # # Additional features for other menu options
# # if menu == "Orders":
# #     st.subheader("Orders")
# #     st.write("Manage your orders here.")
# # elif menu == "Feedbacks":
# #     st.subheader("Feedbacks")
# #     st.write("Share your feedback about the application.")
# # elif menu == "Backtesting":
# #     st.subheader("Backtesting")
# #     st.write("Simulate past trades using historical data.")
# # elif menu == "Notebook Save":
# #     st.subheader("Notebook Save")
# #     st.write("Save your analysis and notes here.")

# # # Save notebook functionality
# # if menu == "Notebook Save":
# #     notebook_input = st.text_area("Enter your notes below:")
# #     if st.button("Save Notes"):
# #         with open("notebook.txt", "a") as f:
# #             f.write(notebook_input + "\n")
# #         st.success("Notes saved successfully!")
