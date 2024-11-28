import re

def verifier_mot_de_passe(mot_de_passe):
    if len(mot_de_passe) < 8:      # Sert à définir le minimum de caractère pour le mot de passe
        return False
    
    if not re.search(r"[A-Z]", mot_de_passe): # Sert qu'on peut écrire toutes les lettres de l'alphabet en majuscule
        return False
    
    if not re.search(r"[a-z]", mot_de_passe):# Sert qu'on peut écrire toutes les lettres de l'alphabet en minuscule
        return False
        
    if not re.search(r"[0-9]", mot_de_passe):
        return False


    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", mot_de_passe): #Sert à séléctionner les caractères spéciaux qu'on peut mettre dans notre mot de passe
        return False
    return True

mot_de_passe = input("Entrez un mot de passe") 

while not verifier_mot_de_passe(mot_de_passe):    # Verifie si le mot de passe comporte minimum 8 caractères, des chiffres, des caractères spéciaux et comporte des minsucules et des majuscules.
    print(" Erreur le mot de passe doit contenir au moins 8 caractères, des chiffres, des majuscules, des minuscules et des caractères spéciaux.")  # affichage d'une erreur si la forme du mot de passe n'est pas accepter.
    mot_de_passe = input("Entrez un mot de passe (au moins 8 caractères, avec des chiffres, des majuscules, des minuscules et des caractères spéciaux) : ")    # Verifie si le mot de passe comporte minimum 8 caractères, des chiffres, des caractères spéciaux et comporte des minsucules et des majuscules.

    

print("Mot de passe accepté.")

import hashlib

import hashlib
import os

def hash_password_with_salt(password):
    # Générer un salt aléatoire
    salt = os.urandom(16)
    # Convertir le mot de passe en bytes
    password_bytes = password.encode('utf-8')
    # Combiner le salt et le mot de passe
    salted_password = salt + password_bytes
    # Créer un objet hash SHA-256
    sha256 = hashlib.sha256()
    # Mettre à jour l'objet hash avec le mot de passe salé
    sha256.update(salted_password)
    # Obtenir le hash hexadécimal
    hashed_password = sha256.hexdigest()
    return salt, hashed_password

# Exemple d'utilisation
mot_de_passe = "monSuperMotDePasse"
salt, mot_de_passe_hache = hash_password_with_salt(mot_de_passe)
print(f"Salt: {salt.hex()}")
print(f"Mot de passe haché: {mot_de_passe_hache}")

