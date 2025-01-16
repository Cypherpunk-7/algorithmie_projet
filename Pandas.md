Documentation : Introduction à Pandas

Installation

pip install pandas
```

---

## Structures de données principales

### 1. Series
Une Series est une structure de données unidimensionnelle similaire à un tableau ou une liste.

#### Création d'une Series
```python
import pandas as pd

# Créer une Series à partir d'une liste
serie = pd.Series([10, 20, 30, 40])
print(serie)

# Créer une Series avec des index personnalisés
serie_custom = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(serie_custom)
```

2. DataFrame
Un DataFrame est une structure bidimensionnelle (tableau avec des lignes et colonnes).

Création d'un DataFrame
```python
# À partir d'un dictionnaire
data = {
    "Nom": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Ville": ["Paris", "Lyon", "Marseille"]
}
df = pd.DataFrame(data)
print(df)

# À partir d'une liste de listes
data = [["Alice", 25, "Paris"], ["Bob", 30, "Lyon"], ["Charlie", 35, "Marseille"]]
df = pd.DataFrame(data, columns=["Nom", "Age", "Ville"])
print(df)
```

---

Opérations fondamentales sur les DataFrames

1. Chargement et sauvegarde de fichiers

Lire un fichier CSV
```python
df = pd.read_csv("fichier.csv")
print(df)
```

Sauvegarder un DataFrame en CSV
```python
df.to_csv("fichier_sortie.csv", index=False)
```

Autres formats pris en charge
- Excel : `pd.read_excel()` / `to_excel()`
- JSON : `pd.read_json()` / `to_json()`
- SQL : `pd.read_sql()` / `to_sql()`

2. Vue et exploration des données

Aperçu du DataFrame
```python
print(df.head())  # Affiche les 5 premières lignes
print(df.tail(3)) # Affiche les 3 dernières lignes
print(df.info())  # Informations sur les colonnes et les types
print(df.describe())  # Statistiques descriptives
```

Accéder aux colonnes et lignes
```python
# Accéder à une colonne
print(df["Nom"])

# Accéder à plusieurs colonnes
print(df[["Nom", "Ville"]])

# Accéder à une ligne par index
print(df.loc[0])  # Par label
print(df.iloc[0]) # Par position
```

3. Filtrage et manipulation des données

Filtrer les lignes
```python
# Lignes où l'age est supérieur à 30
print(df[df["Age"] > 30])
```

Ajouter une colonne
```python
df["Score"] = [90, 85, 95]
print(df)
```

Supprimer une colonne
```python
df = df.drop("Score", axis=1)
print(df)
```

Modifier une valeur
```python
df.loc[0, "Age"] = 26
print(df)
```

4. Gestion des valeurs manquantes

Identifier les valeurs manquantes
```python
print(df.isnull())  # Booleéen indiquant les valeurs NaN
print(df.isnull().sum())  # Nombre de NaN par colonne
```

Remplir les valeurs manquantes
```python
df["Age"] = df["Age"].fillna(30)  # Remplir avec une valeur
```

Supprimer les lignes/colonnes avec des NaN
```python
df = df.dropna()
```

---

Opérations avancées

1. Groupement et agrégation

Groupement par une colonne
```python
grouped = df.groupby("Ville")["Age"].mean()
print(grouped)
```

2. Fusion et jointures

Concaténer des DataFrames
```python
result = pd.concat([df1, df2])
```

Fusionner des DataFrames
```python
result = pd.merge(df1, df2, on="Nom", how="inner")
```

3. Pivot et réorganisation
```python
pivot = df.pivot_table(values="Age", index="Nom", columns="Ville", aggfunc="mean")
print(pivot)
```

---

Bibliothèques complémentaires
- **NumPy** : Pour les opérations numériques performantes.
- **Matplotlib/Seaborn** : Pour la visualisation des données.

---

documentation officielle : https://pandas.pydata.org/.

