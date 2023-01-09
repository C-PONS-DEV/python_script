# Voici un script en python qui renomme un ordinateur Linux

import subprocess

def rename_computer(new_name):
    # Utilisation de la commande hostnamectl pour changer le nom de l'ordinateur
    subprocess.run(["hostnamectl", "set-hostname", new_name])

    # Modification du fichier /etc/hosts pour mettre à jour le nom de l'ordinateur
    with open("/etc/hosts", "r") as f:
        lines = f.readlines()

    with open("/etc/hosts", "w") as f:
        for line in lines:
            if line.startswith("127.0.1.1"):
                line = "127.0.1.1\t" + new_name + "\n"
            f.write(line)

if __name__ == "__main__":
    # Remplacer "new_name" par le nouveau nom de l'ordinateur
    rename_computer("new_name")
