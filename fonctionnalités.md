Documentation : Gestion des utilisateurs, hashage et API Have I Been Pwned

---

1. Interface graphique avec `Tkinter` et `ttkbootstrap`

Fonctionnalités principales :
Le fichier `graph_menu_main.py` gère l'interface utilisateur en créant un menu principal avec des boutons interactifs.

Exemple de code clé :
```python
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

window = ttk.Window(themename="vapor")
window.title("Menu principal")
window.geometry("1000x600")

connexion_button = ttk.Button(window, text="Connexion", command=connexion, bootstyle="PRIMARY")
connexion_button.pack(pady=(40,10))

quit_button = ttk.Button(window, text="Quitter", command=window.destroy, bootstyle="SECONDARY")
quit_button.pack(pady=20)

window.mainloop()
```

Points à noter :
- **Utilisation de ttkbootstrap** : Améliore l’apparence des widgets `Tkinter`.
- **Commandes associées aux boutons** : Les fonctions (`connexion`, `inscription`, etc.) sont importées depuis un module externe.

---

2. Gestion et hashage des mots de passe

Méthodologie :
Pour sécuriser les mots de passe des utilisateurs, il est essentiel d'utiliser un **sel** et un algorithme de hashage. Cela empêche les attaques par force brute basées sur des tables pré-calculées (tables arc-en-ciel).

Exemple de hashage :
```python
import hashlib
import os

def generate_salt():
    """Génère un sel aléatoire de 16 octets"""
    return os.urandom(16).hex()

def hashed_input(password, salt) -> str:
    """Retourne le hash SHA-1 du mot de passe salé."""
    salted_pw = password + salt
    return hashlib.sha1(salted_pw.encode('utf-8')).hexdigest().upper()

# Exemple d'utilisation
salt = generate_salt()
hashed_pw = hashed_input("password", salt)
print(salt, hashed_pw)
```

Améliorations suggérées :
- Utiliser un algorithme plus robuste comme **SHA-256** ou **bcrypt** pour une sécurité accrue.
- Ne jamais enregistrer les mots de passe en clair.

Avec bcrypt (exemple) :
```python
from bcrypt import hashpw, gensalt

password = b"mon_mot_de_passe"
hashed = hashpw(password, gensalt())
print(hashed)
```

---

3. Vérification avec l’API Have I Been Pwned

L'API de HIBP permet de vérifier si un mot de passe a été compromis dans une fuite de données. Pour cela, seule une partie du hash SHA-1 est envoyée, garantissant la confidentialité.

Étapes pour utiliser l’API :
1. **Convertir le mot de passe en SHA-1.**
2. **Envoyer les 5 premiers caractères du hash** à l’API.
3. **Analyser les réponses** pour trouver des correspondances avec les hashes restants.

Exemple de code :
```python
import hashlib
import requests

def check_password_pwned(password):
    """Vérifie si un mot de passe est compromis."""
    # Hash du mot de passe
    sha1_pw = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_pw[:5], sha1_pw[5:]

    # Requête API
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError("Erreur API")

    # Vérification des correspondances
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return True, count
    return False, 0

# Exemple d'utilisation
password = "password123"
is_pwned, count = check_password_pwned(password)
if is_pwned:
    print(f"Le mot de passe a été compromis {count} fois !")
else:
    print("Le mot de passe est sûr.")
```

Points importants :
- Les appels à l’API doivent être effectués avec modération pour éviter de surcharger le service.
- Toujours utiliser HTTPS pour protéger la transmission des données.

---

4. Gestion et stockage des utilisateurs

Pour associer des utilisateurs à leurs produits ou données spécifiques, une base de données est recommandée (par ex. SQLite ou PostgreSQL).

Exemple avec SQLite :
```python
import sqlite3

# Connexion à la base de données
conn = sqlite3.connect("utilisateurs.db")
c = conn.cursor()

# Création d'une table
c.execute('''CREATE TABLE IF NOT EXISTS utilisateurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    salt TEXT NOT NULL
)''')

# Insertion d'un utilisateur
username = "user1"
salt = generate_salt()
hash_pw = hashed_input("mon_mot_de_passe", salt)
c.execute("INSERT INTO utilisateurs (username, password_hash, salt) VALUES (?, ?, ?)", (username, hash_pw, salt))

conn.commit()
conn.close()
```

---

5. Recommandations générales

Sécurité :
- **Ne pas réinventer la roue** : Utilisez des bibliothèques éprouvées comme `bcrypt`, `argon2`, ou `cryptography`.
- **Vérifier les entrées utilisateur** pour éviter les injections SQL ou autres attaques.

Performances :
- Si le projet grandit, envisagez d'utiliser une base de données plus robuste (PostgreSQL, MySQL).

UX/UI :
- Proposez des messages clairs pour guider les utilisateurs, notamment en cas d’erreur (mot de passe faible, déjà utilisé, etc.).

---

