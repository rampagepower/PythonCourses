#Create an empty list
spam = []

#Create a list with values
spam = ['cat', 'bat', 'rat', 'elephant']

#Get a value from a list
print(spam[0])

#A list can contain another list
spam2 = [['cat', 'bat'], [10, 20, 30, 40, 50]]

#Acces to double list
print(spam2[0][1])
print(spam2[1][2])

#Get the last value of a list
print(spam[-1])

#Get values with slice
print(spam[0:2])

#Get the leght of a list
print(len(spam2))

#Modify a list
spam[0] = "Hagrid"
print(spam)

#List concatenation
spam = spam + ['A', 'B', 'C']
print(spam)

#List multiplication
spam = spam * 2
print(spam)

# Create a list to contain similar velues instead of creating several useless variables
listofthing = []
""" 
while True :
    print("Enter value that you want to save or hit enter to exit : ")
    element = input()
    if element =='' :
        print(listofthing)
        break
    listofthing = listofthing + [element] #List concatenation

    #Loop inside of a list
    for unite in listofthing :
        print(unite)
"""

#Loop inside of a list with for loop and range function
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)) :
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

#Operator "in" and "not in"
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])

#Create a list from a loop of range
import random
empty_list = []
for i in range(1,10) :
    empty_list = empty_list + [random.randrange(1,50)]
print(empty_list)

#Multiple assignement
cat = [['fat', 'black', 'loud'],['russia','vaccined','visa']]
size, color, caractere = cat[0]
nation, vaccin, passport = cat[1]
print(size, color, caractere,"+",nation,vaccin,passport)

#Add value at the end to list
cat.append(["Micheal","man"])
print(cat)

#Add value in anywhere to list
cat[2].insert(2,"cat lover")
print(cat)

#find a value inside of a list
print(cat[2].index('Micheal')) #index method can't find Michael of we don't show up exactly where is he. Index works fine for a simple list

#Sort a list
cat.sort()
print(cat)
#Sort with options
cat[1].sort(key=str.lower)
print("sort with keys :",cat)


#Remove a value from a list with Remove and Pop methode / Remove = anywhere / Pop = at the end of the list
cat[0].remove("cat lover")
print(cat)

cat.pop(2)
print("cat popé ", cat)