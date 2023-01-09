# Script qui vérifie la présence de virus sur  Windows et indiquer le dossier où le virus est présent

import os
import subprocess

def check_for_virus(directory):
    # Vérification de la présence de virus dans le dossier spécifié en utilisant la commande sfc
    result = subprocess.run(["sfc", "/scannow", directory], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Si sfc a détecté un virus, affichage du dossier où il se trouve
    if result.returncode != 0:
        print(f"Un virus a été détecté dans le dossier {directory}")
    else:
        print("Aucun virus détecté dans le dossier spécifié.")

if __name__ == "__main__":
    # Remplacer "directory" par le dossier à analyser
    check_for_virus("directory")
