import subprocess

def update_system():
    # Mise à jour de la liste des packages disponibles
    subprocess.run(["apt", "update"])

    # Mise à jour des packages installés
    subprocess.run(["apt", "upgrade", "-y"])

    # Installation des nouveaux packages recommandés
    subprocess.run(["apt", "install", "--no-install-recommends", "-y"])

    # Nettoyage des fichiers de cache inutiles
    subprocess.run(["apt", "autoremove", "-y"])
    subprocess.run(["apt", "clean"])

if __name__ == "__main__":
    update_system()
