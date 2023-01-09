# Script python qui renomme un ordinateur windows

import subprocess

def rename_computer(new_name):
    # Utilisation de la commande net pour changer le nom de l'ordinateur
    subprocess.run(["net", "computername", new_name])

if __name__ == "__main__":
    # Remplacer "new_name" par le nouveau nom de l'ordinateur
    rename_computer("new_name")
