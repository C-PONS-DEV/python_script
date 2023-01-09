import os
import zipfile

def backup_documents_folder():
    # Définition du chemin du dossier à sauvegarder
    documents_path = os.path.expanduser("~/Documents")

    # Vérification de l'existence du dossier
    if not os.path.exists(documents_path):
        print("Le dossier Documents n'existe pas.")
        return

    # Création d'un fichier ZIP pour la sauvegarde
    zip_file = zipfile.ZipFile("documents_backup.zip", "w")

    # Ajout des fichiers du dossier Documents au fichier ZIP
    for root, dirs, files in os.walk(documents_path):
        for file in files:
            file_path = os.path.join(root, file)
            zip_file.write(file_path)

    # Fermeture du fichier ZIP
    zip_file.close()

if __name__ == "__main__":
    backup_documents_folder()
