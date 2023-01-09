# Script qui affiche les ports ouverts sur un ordinateur Ubuntu :

import subprocess

def list_open_ports():
    # Récupération de la liste des ports ouverts en utilisant la commande netstat
    result = subprocess.run(["netstat", "-an"], stdout=subprocess.PIPE)
    output = result.stdout.decode("utf-8")

    # Parcours de la sortie de netstat et affichage des ports ouverts
    for line in output.split("\n"):
        if "LISTEN" in line:
            print(line)

if __name__ == "__main__":
    list_open_ports()