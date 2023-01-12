# Script qui utilise l'API de Windows Update pour vérifier s'il y a des mises à jour disponibles pour Windows 11

import subprocess

def check_updates():
    result = subprocess.run(["powershell.exe", "-Command", "Get-WindowsUpdate"], stdout=subprocess.PIPE)
    output = result.stdout.decode("utf-8")
    if "Updates are available." in output:
        print("Des mises à jour sont disponibles.")
    else:
        print("Aucune mise à jour disponible.")

check_updates()


