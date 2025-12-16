import streamlit as st
from financial_advisor.frontend.api_client import create_income, APIError

INCOME_CATEGORIES = [
    "salaire",
    "prime",
    "revenu_locatif",
    "autre_revenu",
]

def render():
    st.header("Ajouter un revenu")

    amount = st.number_input("Montant", min_value=0.01, step=100.0)
    category = st.selectbox("Catégorie", INCOME_CATEGORIES)
    description = st.text_input("Description (optionnelle)")

    if st.button("Ajouter"):
        if not category:
            st.warning("La catégorie est obligatoire.")
            return None

        try:
            create_income(
                {
                    "amount": amount,
                    "category": category,
                    "description": description or None,
                }
            )

            st.session_state["income_added"] = {
                "amount": amount,
                "category": category,
            }

            st.rerun()

        except APIError as exc:
            st.error(str(exc))
    
    # Message de confirmation après rerun
    if "income_added" in st.session_state:
        info = st.session_state.pop("income_added")
        st.success(
            f"Revenu ajouté avec succès : {info['amount']} € ({info['category']})"
        )
