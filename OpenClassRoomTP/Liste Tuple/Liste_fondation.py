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

#find a value inside of a list
print(cat[2].index('Micheal')) #index method can't find Michael of we don't show up exactly where is he. Index works fine for a simple list

#Sort a list
cat.sort()
print(cat)
#Sort with options
cat[1].sort(key=str.lower)
print("sort with keys :",cat)


#Remove a value from a list with Remove, Pop and del methode / Remove = anywhere + value/ Pop = at the end of the list / Del delete by index
cat[0].remove("cat lover")

cat.pop(2)

del(cat[1][0])

#Copy a list by reference
cat2 = cat
print(f'cat2 is cat : {cat2 is cat} and it\'s id is : {id(cat2)}')

#Copy a list to a real list
cat3 = cat.copy()
print(f'cat3 is cat : {cat3 is cat} and it\'s id is : {id(cat3)}')

import copy
cat4 = copy.copy(cat)

print(f'cat4 is cat : {cat3 is cat} and it\'s id is : {id(cat4)}')

print(cat4)

"""
1. What is []?
A:  Creating an empty list
"""

"""
2. How would you assign the value 'hello' as the third value in a list stored
in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
"""
spam = [2, 4, 6, 8, 10]
spam[2] = "hello"
print(spam)

"""
For the following three questions, let’s say spam contains the list ['a','b', 'c', 'd'].
3. What does spam[int(int('3' * 2) / 11)] evaluate to?
"""
spam = ['a','b', 'c', 'd']

#3 => d
print(spam[int(int('3' * 2) / 11)])

"""
4. What does spam[-1] evaluate to?
"""
#d
print(spam[-1])
"""
5. What does spam[:2] evaluate to?
"""

#a,b
print(spam[:2])

"""
For the following three questions, let’s say bacon contains the list
[3.14, 'cat', 11, 'cat', True].
6. What does bacon.index('cat') evaluate to?
"""
bacon=[3.14, 'cat', 11, 'cat', True]

#1
print(bacon.index('cat'))

"""
7. What does bacon.append(99) make the list value in bacon look like?
"""

bacon.append(99)

#[3.14, 'cat', 11, 'cat', True,99]
print(bacon)

"""
8. What does bacon.remove('cat') make the list value in bacon look like?
"""
#Remove only one cat
bacon.remove('cat')
print(bacon)

"""
9. What are the operators for list concatenation and list replication?
"""

#List concatenation => + or append

#List replication : copy or deepcopy

"""
10. What is the difference between the append() and insert() list methods?
"""

#Append => add at the end

#Insert => add by index given

"""
11. What are two ways to remove values from a list?
"""

# Pop / del / remove

"""
12. Name a few ways that list values are similar to string values.
"""

for elements in bacon :
    if type(elements) == str :
        print(f'print only string {elements}')
    elif isinstance(elements,int) :
        print(f'print only int : {elements}')

"""
13. What is the difference between lists and tuples?
"""
#list can be modified and tuples is not

"""
14. How do you type the tuple value that has just the integer value 42 in it?
"""
mytuple = (42,)

print(type(mytuple),mytuple)

"""
15. How can you get the tuple form of a list value? How can you get the list
form of a tuple value?
"""

#Convert tuple to list
list_of_tuple =list(mytuple)
print(type(list_of_tuple))

#Convert list to tupl
tuple_of_list=tuple(list_of_tuple)
print(type(tuple_of_list))

"""
16. Variables that “contain” list values don’t actually contain lists directly.
What do they contain instead?
"""

#Reference


"""
17. What is the difference between copy.copy() and copy.deepcopy()?
"""
# deepcopy can copy lists inside of a list to the new list