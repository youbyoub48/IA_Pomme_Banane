from IA import IA
from glob import glob

import os, shutil

PATH = os.path.abspath(os.path.split(__file__)[0])
Pomme = os.path.join(PATH, "Pomme")
Banane = os.path.join(PATH, "Banane")
Images = os.path.join(PATH, "Images")

if not os.path.exists(Pomme):
    os.mkdir(Pomme)

if not os.path.exists(Banane):
    os.mkdir(Banane)

images = glob(os.path.join(Images, "*"))

for line in images:
    prediction = IA(line)
    
    if prediction == "pomme":
        shutil.copy(line, Pomme)
    
    if prediction == "banane":
        shutil.copy(line, Banane)