def square(n) :
    return n*n

def add(*elements) :
    elements = list(elements)
    total = 0
    for i, unite in enumerate(elements) :
        elements[i] = int(unite)
        total += elements[i]
    return total

def multiplication(*elements):

    elements = list(elements)

    total = 1

    for i, unite in enumerate(elements) :
        elements[i] = int(unite)
        total *= elements[i]

    return total

def substract(a,b) :

    result = a - b if a > b else b-a

    return result

def split_float(*x) :
    x = list(x)

    for i,element in enumerate(x) :
        x[i] = str(element)

    entier,floatant = x[0].split(".")
    nbr_decimal = len(floatant)

    if nbr_decimal > int(x[1]) :
        nbr_decimal = int(x[1])

    y = x[2].join([entier,floatant[:nbr_decimal]])

    print([2*num for num in y])


def convert_float():
    nbr = float(input("Donnez un nombre float : \n"))
    decimal = int(input("Combien de decimal vous voulez : \n"))
    sep=","

    if type(nbr) is not float :
        raise TypeError("Le nombre doit être un float")

    split_float(nbr,decimal,sep)

def gestion_stock():

    nbr_a_retirer = 3
    stock_restant =[4,5,6,7]

    inventaire = [
        ("pommes", 22),
        ("melons", 4),
        ("poires", 18),
        ("fraises", 76),
        ("prunes", 51),
        ]

    print("Sous traction avec une liste simple\n")
    print([nbr - nbr_a_retirer for nbr in stock_restant if nbr_a_retirer<nbr])


    inventaire_inversed = [(nbr,fruit) for fruit,nbr in inventaire]
    inventaire_inversed.sort(reverse=True)

    print("inverser une liste complexe \n")
    inventaire = [(fruit, nbr) for nbr,fruit in inventaire_inversed]
    print(inventaire)

    print("Sous traction avec une liste complexe\n")
    liste_course = [(fruit,nbr - nbr_a_retirer) for fruit, nbr in inventaire if nbr > nbr_a_retirer]
    print(liste_course)


if __name__== "__main__" :

   #convert_float()
   #print(multiplication(2,2,3,2))
   #print(add(1,2,3,4))
   #print(substract(3,5))

    gestion_stock()