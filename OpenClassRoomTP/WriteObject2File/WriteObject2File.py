import os
import pickle

echiquier = {}
echiquier['a', 1] = "tour blanche" # En bas à gauche de l'échiquier
echiquier['b', 1] = "cavalier blanc" # À droite de la tour
echiquier['c', 1] = "fou blanc" # À droite du cavalier
echiquier['d', 1] = "reine blanche" # À droite du fou
# ... Première ligne des blancs
echiquier['a', 2] = "pion blanc" # Devant la tour
echiquier['b', 2] = "pion blanc" # Devant le cavalier, à droite du pion

print(os.listdir())

mode ="wb+"

with open("object2file", mode) as fichier :
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(echiquier)

print(mon_pickler)
print(fichier.closed)

mode = "rb"
with open("object2file", mode) as fichier :
    print(fichier.closed)
    mon_depickler = pickle.Unpickler(fichier)
    recup_echequier = mon_depickler.load()

print(recup_echequier)
print(fichier.closed)