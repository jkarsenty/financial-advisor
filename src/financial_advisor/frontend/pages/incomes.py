import streamlit as st
from financial_advisor.frontend.api_client import create_income


def render():
    st.header("Ajouter un revenu")

    amount = st.number_input("Montant", min_value=0.0, step=100.0)
    category = st.text_input("Catégorie")
    description = st.text_input("Description (optionnelle)")

    if st.button("Ajouter"):
        try:
            create_income(
                {
                    "amount": amount,
                    "category": category,
                    "description": description or None,
                }
            )
            st.success("Revenu ajouté avec succès")
        except Exception as exc:
            st.error(f"Erreur API : {exc}")
