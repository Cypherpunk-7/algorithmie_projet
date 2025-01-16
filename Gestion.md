Documentation : Gestion des fichiers en Python

1. Ouverture d'un fichier

Pour ouvrir un fichier en Python, utilisez la fonction `open()`.

Syntaxe :
```python
open(file, mode='r', encoding=None)
```

Arguments principaux :
- **file** : Le chemin du fichier à ouvrir (relatif ou absolu).
- **mode** : Le mode d’ouverture (à défaut : `r` pour lecture).
- **encoding** : L'encodage (par exemple : `utf-8`).

Modes d'ouverture :
| Mode | Description |
|------|-------------|
| `r`  | Lecture seule. Le fichier doit exister. |
| `w`  | Écriture seule. Crée un nouveau fichier ou écrase le fichier existant. |
| `x`  | Création uniquement. Échoue si le fichier existe. |
| `a`  | Ajout. Écrit à la fin du fichier sans le tronquer. |
| `b`  | Mode binaire. Utilisé avec d'autres modes (par ex. `rb` ou `wb`). |
| `t`  | Mode texte. Utilisé par défaut. |
| `+`  | Lecture et écriture. |

Exemple :
```python
# Ouverture en lecture
f = open("example.txt", mode="r", encoding="utf-8")
```

2. Lecture d'un fichier

Python offre plusieurs méthodes pour lire le contenu d’un fichier.

Lire tout le fichier :
```python
with open("example.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
    print(contenu)
```

Lire ligne par ligne :
```python
with open("example.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.strip())
```

Lire un nombre de caractères :
```python
with open("example.txt", "r", encoding="utf-8") as f:
    contenu = f.read(10)  # Lire les 10 premiers caractères
    print(contenu)
```

3. Écriture dans un fichier

Pour écrire dans un fichier, utilisez les méthodes `write()` ou `writelines()`.

Exemple avec `write()` :
```python
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Bonjour, monde !\n")
```

Exemple avec `writelines()` :
```python
lignes = ["Ligne 1\n", "Ligne 2\n", "Ligne 3\n"]
with open("example.txt", "w", encoding="utf-8") as f:
    f.writelines(lignes)
```

Mode ajout (`a`) :
```python
with open("example.txt", "a", encoding="utf-8") as f:
    f.write("Nouvelle ligne ajoutée.\n")
```

4. Fermeture des fichiers

Bien que Python ferme automatiquement les fichiers à la sortie d'un bloc `with`, vous pouvez le faire manuellement avec `close()`.

Exemple :
```python
f = open("example.txt", "r", encoding="utf-8")
# Opérations sur le fichier
f.close()
```

Pourquoi utiliser `with` ?
L'utilisation de `with` garantit que le fichier est fermé correctement, même en cas d'exception.

5. Gestion des erreurs

Utilisez des blocs `try-except` pour gérer les erreurs potentielles.

Exemple :
```python
try:
    with open("example.txt", "r", encoding="utf-8") as f:
        contenu = f.read()
except FileNotFoundError:
    print("Le fichier n'existe pas.")
except IOError:
    print("Une erreur d'entrée/sortie s'est produite.")
```

6. Manipulation avancée

Obtenir la position actuelle :
```python
with open("example.txt", "r", encoding="utf-8") as f:
    print(f.tell())  # Position actuelle du curseur
```

Déplacer le curseur :
```python
with open("example.txt", "r", encoding="utf-8") as f:
    f.seek(5)  # Se déplacer à la 5ème position
    contenu = f.read()
    print(contenu)
```

7. Suppression et renommage de fichiers

Pour manipuler des fichiers (hors lecture/écriture), utilisez le module `os`.

Exemple :
```python
import os

# Supprimer un fichier
os.remove("example.txt")

# Renommer un fichier
os.rename("ancien_nom.txt", "nouveau_nom.txt")
```

8. Bibliothèques utiles

- **shutil** : Pour copier ou déplacer des fichiers.
- **pathlib** : Une interface orientée objet pour les chemins de fichiers.

Exemple avec pathlib :
```python
from pathlib import Path

# Créer un fichier
chemin = Path("example.txt")
chemin.write_text("Contenu du fichier", encoding="utf-8")

# Lire un fichier
print(chemin.read_text(encoding="utf-8"))
```

---
documentation officielle : https://docs.python.org/3/library/io.html.

