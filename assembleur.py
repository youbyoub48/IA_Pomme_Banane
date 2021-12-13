import shutil, os

from glob import glob

PATH = os.path.abspath(os.path.split(__file__)[0])
Dossier1 = os.path.join(PATH, "Pomme")
Dossier2 = os.path.join(PATH, "Banane")

fichier1 = glob(os.path.join(Dossier1, "*"))
fichier2 = glob(os.path.join(Dossier2, "*"))

fichier = fichier1+fichier2
destination = os.path.join(PATH, "Images")

for i in range(len(fichier)):
    shutil.copy(fichier[i], os.path.join(destination, f"{i}.jpg"))