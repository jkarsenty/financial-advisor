import streamlit as st
from financial_advisor.frontend.api_client import get_summary


def render():
    st.header("Résumé financier")

    try:
        data = get_summary()
    except Exception as exc:
        st.error(f"Impossible de charger le résumé : {exc}")
        return

    col1, col2, col3 = st.columns(3)
    col1.metric("Revenus", f"{data['total_incomes']:.2f}")
    col2.metric("Dépenses", f"{data['total_expenses']:.2f}")
    col3.metric("Reste", f"{data['remaining']:.2f}")

    st.progress(min(max(data["expense_ratio"], 0.0), 1.0))

    st.subheader("Transactions")
    st.dataframe(data["transactions"])
