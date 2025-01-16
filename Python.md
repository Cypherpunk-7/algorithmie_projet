Documentation : Les bases essentielles de Python

---

1. Affichage de texte

La commande `print()` permet d'afficher des informations dans la console.
```python
print("Bonjour, monde !")
```

---
2. Variables et types de données

Déclaration de variables

Python est typé dynamiquement, ce qui signifie qu'il n'est pas nécessaire de spécifier le type d'une variable.
```python
nom = "Alice"    # Chaîne de caractères
age = 25          # Entier
pi = 3.14159      # Nombre à virgule flottante
is_active = True  # Booléen
```

 Types de données courants
| Type        | Exemple           |
|-------------|-------------------|
| int         | `42`              |
| float       | `3.14`            |
| str         | `"Python"`       |
| bool        | `True`, `False`   |
| list        | `[1, 2, 3]`       |
| tuple       | `(1, 2, 3)`       |
| dict        | `{ "clé": "valeur" }` |
| set         | `{1, 2, 3}`       |

---

3. Structures de contrôle

Conditions
Les conditions permettent de tester des expressions logiques.
```python
age = 18
if age >= 18:
    print("Majeur")
else:
    print("Mineur")
```

 Boucles

Boucle `for`
Parcourir une séquence comme une liste ou une chaîne de caractères.
```python
for i in range(5):
    print(i)  # Affiche les nombres de 0 à 4
```

Boucle `while`
Répéter une action tant qu'une condition est vraie.
```python
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1
```

---

4. Fonctions

Les fonctions permettent de réutiliser du code.
```python
def saluer(nom):
    return f"Bonjour, {nom}!"

print(saluer("Alice"))
```

Paramètres par défaut
```python
def saluer(nom, ponctuation="!"):
    return f"Bonjour, {nom}{ponctuation}"

print(saluer("Bob", "..."))
```

---

5. Gestion des fichiers

Lire et écrire dans des fichiers avec `open()`.

Lire un fichier
```python
with open("example.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.read()
    print(contenu)
```

Écrire dans un fichier
```python
with open("example.txt", "w", encoding="utf-8") as fichier:
    fichier.write("Hello, world!")
```

---

6. Gestion des erreurs

Utilisez `try-except` pour gérer les exceptions.
```python
try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("Erreur : division par zéro")
```

---

7. Modules et bibliothèques

Python dispose d'un large écosystème de modules intégrés ou tiers.

Importer un module intégré
```python
import math
print(math.sqrt(16))  # Affiche 4.0
```

Installer et utiliser une bibliothèque tierce
```bash
pip install requests
```
```python
import requests
response = requests.get("https://api.example.com")
print(response.text)
```

---

8. Programmation orientée objet

Classes et objets
```python
class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        print(f"Je suis {self.nom}")

chat = Animal("Chat")
chat.parler()
```

---

9. Structures de données avancées

Listes
```python
fruits = ["pomme", "banane", "cerise"]
fruits.append("orange")
print(fruits)
```

Dictionnaires
```python
personne = {"nom": "Alice", "âge": 30}
print(personne["nom"])
```

---

10. Recommandations pour bien coder en Python

- **PEP 8** : Respectez les conventions de style Python.
- **Commentaires** : Commentez votre code pour le rendre compréhensible.
- **Modularité** : Divisez votre code en fonctions et modules réutilisables.

documentation officielle : [https://docs.python.org/3/](https://docs.python.org/3/).

