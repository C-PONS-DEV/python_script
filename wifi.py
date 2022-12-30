import pyqrcode
import os

# Nom du réseau Wi-Fi
ssid = "Livebox-PONS"

# Mot de passe du réseau Wi-Fi
password = "motdepasse"

# Création du QR code avec les informations de connexion Wi-Fi
qr = pyqrcode.create(f"WIFI:S:{ssid};T:WPA;P:{password};;")

# Enregistrement du QR code dans un fichier PNG
qr.png("wifi.png", scale=6)

# Affichage du QR code dans la console
print(qr.terminal(quiet_zone=1))


# Installer : pip install pyqrcode
