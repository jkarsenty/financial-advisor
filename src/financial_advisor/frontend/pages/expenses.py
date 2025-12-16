import streamlit as st
from financial_advisor.frontend.api_client import create_expense, APIError

EXPENSE_CATEGORIES = [
    "logement",
    "services_publics",
    "courses",
    "transport",
    "divertissement",
    "sante",
    "abonnements",
    "autre_depense",
]

def render():
    st.header("Ajouter une dépense")

    amount = st.number_input("Montant", min_value=0.0, step=50.0)
    category = st.selectbox("Catégorie", EXPENSE_CATEGORIES)
    description = st.text_input("Description (optionnelle)")

    if st.button("Ajouter"):
        if not category:
            st.warning("La catégorie est obligatoire.")
            return None
        
        try:
            create_expense(
                {
                    "amount": amount,
                    "category": category,
                    "description": description or None,
                }
            )

            st.session_state["expense_added"] = {
                "amount": amount,
                "category": category,
            }


            st.rerun()

        except APIError as exc:
            st.error(f"Erreur API : {exc}")

    if "expense_added" in st.session_state:
        info = st.session_state.pop("expense_added")
        st.success(
            f"Dépense ajoutée : {info['amount']} € ({info['category']})"
        )
