# Script qui vérifie est intalle automatiquement les mises à jours windows 

import subprocess

def update_system():
    # Mise à jour du système via la commande wuauclt
    subprocess.run(["wuauclt", "/detectnow"])

if __name__ == "__main__":
    update_system()
