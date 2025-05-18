import pandas as pd
# Importe la bibliothèque pandas, utilisée pour manipuler des données tabulaires (DataFrame).

def process_entries(entries):
    # Déclare une fonction qui prend en entrée une liste de dictionnaires (les entrées Gravity Forms).

    df = pd.DataFrame(entries)
    # Convertit la liste d’entrées en DataFrame pandas (tableau à deux dimensions).

    df.dropna(axis=1, how='all', inplace=True)
    # Supprime toutes les colonnes qui ne contiennent que des valeurs manquantes (NaN ou None).

    for col in df.columns:
        df[col] = df[col].astype(str).str.split(',').str[0]
        # Pour chaque colonne, convertit toutes les valeurs en chaîne de caractères,
        # puis coupe la chaîne au premier séparateur virgule et ne garde que la première partie.
        # Cela permet d’avoir une seule donnée par cellule, même si la donnée d’origine était une liste ou une chaîne séparée par des virgules.

    return df
    # Retourne le DataFrame nettoyé.