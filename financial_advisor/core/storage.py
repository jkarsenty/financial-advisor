"""
Module: storage
Description:
    Fournit une couche de persistance simple basée sur JSON pour stocker
    les listes de transactions (revenus, dépenses).

    Approche fonctionnelle :
    - Les données sont manipulées sous forme de dicts (Transaction).
    - Lecture/écriture JSON robuste.
"""

import json
from typing import List
from pathlib import Path

from .models import Transaction


# -------------------------------------------------------------------
# Sauvegarde
# -------------------------------------------------------------------

def save_transactions(file_path: Path, transactions: List[Transaction]) -> None:
    """
    Sauvegarde une liste de transactions dans un fichier JSON.

    Args:
        file_path: Chemin du fichier JSON.
        transactions: Liste de dictionnaires Transaction.

    Raises:
        IOError: En cas de problème d'écriture disque.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with file_path.open("w", encoding="utf-8") as f:
            json.dump(transactions, f, ensure_ascii=False, indent=4, default=str)
    except OSError as e:
        raise IOError(f"Erreur lors de l'écriture du fichier {file_path}: {e}") from e


# -------------------------------------------------------------------
# Chargement
# -------------------------------------------------------------------

def load_transactions(file_path: Path) -> List[Transaction]:
    """
    Charge une liste de transactions depuis un fichier JSON.

    Args:
        file_path: Chemin du fichier JSON.

    Returns:
        Une liste de Transaction (peut être vide).
    """
    if not file_path.exists():
        return []

    try:
        with file_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except (OSError, json.JSONDecodeError) as e:
        raise IOError(f"Erreur lors de la lecture du fichier {file_path}: {e}") from e
