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

## Étape actuelle : Dockerisation (API + Frontend)

L’application dispose désormais :

* d’une **API REST FastAPI fonctionnelle**
* d’un **frontend Streamlit** consommant exclusivement l’API

La logique métier reste centralisée dans le backend ; le frontend agit uniquement comme client.

---

## Backend API (FastAPI)

### Fonctionnalités disponibles

- Création de revenus (`POST /api/income`)
- Création de dépenses (`POST /api/expense`)
- Consultation du résumé financier (`GET /api/summary`)
- Health check (`GET /health`)
- Validation automatique des entrées (Pydantic)
- Documentation interactive Swagger (/docs)

---

## Frontend (Streamlit)

Une interface utilisateur simple permet :

* l’ajout de revenus
* l’ajout de dépenses
* la visualisation du résumé financier
* l’affichage des transactions
* la gestion propre des erreurs API

Le frontend :

* ne contient aucune logique métier
* communique uniquement via HTTP avec l’API FastAPI
* est conçu pour être facilement remplaçable (React, etc.)

---

## Docker (API + Frontend)

L’application est désormais entièrement dockerisée.

Deux services sont fournis via Docker Compose :

- **API FastAPI**
- **Frontend Streamlit**

La communication entre les services se fait via le réseau Docker interne.

### Architecture

- API : `http://api:8000`
- Frontend : `http://frontend:8501`
- Accès local :
  - API : http://localhost:8000/docs
  - Frontend : http://localhost:8501


## Structure du projet (Step 1)

```

financial-advisor/
├── src/
│   └── financial_advisor/
│       ├── __init__.py
│       │
│       ├── core/                  # Logique métier pure
│       │   ├── incomes.py
│       │   ├── expenses.py
│       │   ├── categories.py
│       │   ├── calculations.py
│       │   ├── storage.py
│       │   └── models.py
│       │
│       ├── api/                   # Backend FastAPI
│       │   ├── main.py
│       │   ├── routes/
│       │   │   ├── incomes.py
│       │   │   ├── expenses.py
│       │   │   └── summary.py
│       │   └── schemas/
│       │       ├── income_schema.py
│       │       ├── expense_schema.py
│       │       └── summary_schema.py
│       │
│       └── frontend/              # Frontend Streamlit
│           ├── app.py
│           ├── api_client.py
│           ├── config.py
│           └── _pages/
│               ├── dashboard.py
│               ├── incomes.py
│               └── expenses.py
│
├── data/
│   └── transactions.json          # Stockage local temporaire
│
├── tests/
│   ├── core/                      # Tests unitaires core
│   ├── api/                       # Tests API
│   └── frontend/                  # Tests client frontend
│
├── scripts/
│   └── seed_dev_data.py
│
├── docker/
│   ├── Dockerfile.api             # Image API FastAPI
│   └── Dockerfile.frontend        # Image Frontend Streamlit
│
├── docker-compose.yml             # Orchestration API + Frontend
├── .env.example                   # Variables d’environnement (exemple)
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

## Données de développement

Pour peupler l’application avec des données fictives (dev uniquement) :

```bash
python scripts/seed_dev_data.py
```

## Lancer l’application en local

### Backend (API)

```bash
uvicorn financial_advisor.api.main:app --reload
```

Accès :

* Swagger UI : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Health check : [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

---

### Frontend (Streamlit)

```bash
streamlit run src/financial_advisor/frontend/app.py
```

Accès :

* Frontend : [http://localhost:8501](http://localhost:8501)

---

## Lancer l’application avec Docker

### Prérequis
- Docker
- Docker Compose

### Démarrage

```bash
cp .env.example .env
docker compose up --build
```

### Accès

API (Swagger) : http://localhost:8000/docs

Frontend : http://localhost:8501

--- 

## Tests

```bash
pytest -v
```

Les tests couvrent :

* la logique métier (core)
* l’API FastAPI
* le client frontend (mock HTTP)

---

## Roadmap

* Step 0 : Core Logic (Python) -> OK
* Step 1 : Backend API (FastAPI) -> OK
* Step 2 : Frontend Streamlit -> OK
* Step 3 : Docker (API + Frontend) -> OK
* Step 4 : PostgreSQL (en cours)
* Step 5 : Machine Learning
* Step 6 : Déploiement cloud
* Step 7 : CI/CD complet

---

## Licence

MIT