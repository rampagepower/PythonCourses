import os

print(os.listdir())

mode = input("Entrez mode d'ouverture w+,r,a: ")

with open("/Python Trainning/OpenClassRoomTP/Poem/Wise_remembrances.txt", mode) as mon_fichier :
    if mode == "w+" :
        mon_fichier.write("Hello\n")
        mon_fichier.write("Premier test d'écriture dans un fichier via Python")
    elif mode == "r" :
        print(mon_fichier.read())

print("File is closed" if mon_fichier.closed else "File is still opened")

