echiquier = {}
echiquier['a', 1] = "tour blanche" # En bas à gauche de l'échiquier
echiquier['b', 1] = "cavalier blanc" # À droite de la tour
echiquier['c', 1] = "fou blanc" # À droite du cavalier
echiquier['d', 1] = "reine blanche" # À droite du fou
# ... Première ligne des blancs
echiquier['a', 2] = "pion blanc" # Devant la tour
echiquier['b', 2] = "pion blanc" # Devant le cavalier, à droite du pion

print(echiquier)

print("supperimer Fou blanc")
del echiquier['c',1]

print(echiquier)

for cle in echiquier.keys() :
    print(cle)


for value in echiquier.values() :
    print(value)

for cle,value in echiquier.items() :
    print(value)

