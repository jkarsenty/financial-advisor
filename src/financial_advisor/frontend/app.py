import streamlit as st
from financial_advisor.frontend.pages import dashboard, incomes, expenses

st.set_page_config(page_title="Financial Advisor", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à", ["Dashboard", "Revenus", "Dépenses"])

if page == "Dashboard":
    dashboard.render()
elif page == "Revenus":
    incomes.render()
else:
    expenses.render()
