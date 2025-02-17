import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set the title
st.title("Financial Dashboard")

# Create columns for the metrics
col1, col2, col3, col4 = st.columns(4)

# Display financial metrics
col1.metric("Total Accounts Receivable", "$6,621,280", "1.86%")
col2.metric("Total Accounts Payable", "$1,630,270", "3.10%")
col3.metric("Equity Ratio", "75.38%")
col4.metric("Debt Equity", "1.10%")

# Add some spacing between sections
st.markdown("---")

# Create sample data for charts
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
accounts_receivable = np.random.randint(200000, 800000, size=12)
accounts_payable = np.random.randint(50000, 400000, size=12)
net_working_capital = np.random.randint(300000, 900000, size=12)

# Create a bar chart
st.subheader("Accounts Receivable and Payable Aging")
fig1, ax1 = plt.subplots()
ax1.bar(months, accounts_receivable, label="Accounts Receivable", color="blue", alpha=0.7)
ax1.bar(months, accounts_payable, label="Accounts Payable", color="red", alpha=0.7)
ax1.legend()
ax1.set_xlabel("Month")
ax1.set_ylabel("Amount ($)")
st.pyplot(fig1)

# Create a line chart for Net Working Capital
st.subheader("Net Working Capital vs Gross Working Capital")
fig2, ax2 = plt.subplots()
ax2.plot(months, net_working_capital, label="Net Working Capital", color="green", marker="o")
ax2.set_xlabel("Month")
ax2.set_ylabel("Amount ($)")
st.pyplot(fig2)

# Add another bar chart for Profit and Loss Summary
profit_loss = np.random.randint(100000, 600000, size=12)
st.subheader("Profit and Loss Summary")
fig3, ax3 = plt.subplots()
ax3.bar(months, profit_loss, color="orange", label="Profit & Loss")
ax3.set_xlabel("Month")
ax3.set_ylabel("Profit/Loss ($)")
st.pyplot(fig3)



st.markdown("""
<style>
    .stMetric {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    .stMetric label {
        font-size: 10px;
        font-weight: bold;
    }
    .stMetric value {
        font-size: 15px;
        color: #2e86c1;
    }
</style>
""", unsafe_allow_html=True)