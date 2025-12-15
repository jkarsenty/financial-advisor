# Financial Advisor

MVP de gestion de finances personnelles développé en Python.  
Ce projet évoluera en plusieurs étapes : logique métier, API, frontend, infrastructure (Docker/cloud), IA et CI/CD.

---

## Objectif du projet

Construire une application complète permettant :

- la saisie de revenus et dépenses
- la catégorisation
- le calcul de métriques financières (totaux, reste à vivre, ratios)
- l’exposition via une API REST (FastAPI)
- un frontend interactif (Streamlit)
- un déploiement industrialisé (Docker, cloud)
- l’ajout progressif de fonctionnalités IA
- une chaîne CI/CD propre (GitHub Actions)

---

## Étape actuelle : Backend API (FastAPI)

L’application expose désormais une **API REST fonctionnelle**, construite sur une logique métier robuste.

### Fonctionnalités disponibles

- Création de revenus (`POST /api/income`)
- Création de dépenses (`POST /api/expense`)
- Consultation du résumé financier (`GET /api/summary`)
- Health check (`GET /health`)
- Validation automatique des entrées (Pydantic)
- Documentation interactive Swagger (/docs)

---

## Structure du projet (Step 1)

```

financial-advisor/
├── src/
│   └── financial_advisor/
│       ├── **init**.py
│       │
│       ├── core/                  # Logique métier pure
│       │   ├── incomes.py
│       │   ├── expenses.py
│       │   ├── categories.py
│       │   ├── calculations.py
│       │   ├── storage.py
│       │   └── models.py
│       │
│       └── api/                   # Backend FastAPI
│           ├── main.py
│           ├── routes/
│           │   ├── incomes.py
│           │   ├── expenses.py
│           │   └── summary.py
│           └── schemas/
│               ├── income_schema.py
│               ├── expense_schema.py
│               └── summary_schema.py
│
├── data/
│   └── transactions.json          # Stockage local temporaire
│
├── tests/
│   └── core/                      # Tests unitaires (Step 0)
│
├── pyproject.toml
├── requirements.txt
└── README.md

````

---

## Installation

Créer un environnement virtuel (conda, venv, etc.), puis :

```bash
pip install -r requirements.txt
pip install -e .
````

---

## Lancer l’API

Depuis la racine du projet :

```bash
uvicorn financial_advisor.api.main:app --reload
```

Puis ouvrir :

* Swagger UI : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Health check : [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

---

## Tests

### Tests unitaires (core)

```bash
pytest -v
```

---

## Roadmap

* Step 0 : Core Logic (Python) --> OK
* Step 1 : Backend API (FastAPI) --> OK
* Step 2 : Frontend Streamlit
* Step 3 : Docker + PostgreSQL
* Step 4 : Machine Learning
* Step 5 : Déploiement cloud
* Step 6 : CI/CD complet

---

## 📄 Licence

MIT