import hashlib
import os
def generate_salt():
    """Génère un sel aléatoire de 16 octets"""
    return os.urandom(16).hex()

def hashed_input(password, salt) -> str:
    """Retourne le hash SHA-1 du mot de passe salé."""
    salted_pw = password + salt
    return hashlib.sha1(salted_pw.encode('utf-8')).hexdigest().upper()

salt = generate_salt()
hashed_pw = hashed_input("password", salt)
print(
    salt,
    hashed_pw
)