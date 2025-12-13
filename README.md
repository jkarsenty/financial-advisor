# Financial Advisor

MVP de gestion de finances personnelles développé en Python.  
Ce projet évoluera en plusieurs étapes : logique métier, API, frontend, ML, Docker, infrastructure cloud et CI/CD.

---

## Étape actuelle : Step 0 – Core Logic

Cette première étape pose les fondations du projet :

- Modèles internes (revenus, dépenses)
- Gestion des catégories
- Calculs financiers : totaux, reste à vivre, ratios
- Stockage local simple (JSON)
- Tests unitaires avec pytest
- Structure de projet propre et évolutive

---

## Structure du projet (Step 0)

```
financial-advisor/
├── src/
│   └── financial_advisor/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── incomes.py
│       │   ├── expenses.py
│       │   ├── categories.py
│       │   ├── calculations.py
│       │   ├── storage.py
│       │   └── models.py
│       │
│       └── main.py   (temporaire, sera remplacé plus tard)
│
├── tests/
│   └── core/
│       ├── test_categories.py
│       ├── test_incomes.py
│       ├── test_expenses.py
│       ├── test_calculations.py
│       └── test_storage.py
│
├── pyproject.toml
└── README.md
```

---

## Installation

```
pip install -r requirements.txt
```

---

## Exécuter les tests

```
pytest -v
```

---

## Objectif des prochaines étapes

- Étape 1 : API FastAPI  
- Étape 2 : Frontend Streamlit  
- Étape 3 : Docker + PostgreSQL  
- Étape 4 : Machine Learning (classification des dépenses)  
- Étape 5 : Déploiement cloud  
- Étape 6 : CI/CD GitHub Actions  

---

## Licence

MIT