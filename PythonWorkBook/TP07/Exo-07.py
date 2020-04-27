"""
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula
sum = (n)*(n + 1) / 2
"""

n = int(input("Give an integer : "))

print(int((n)*(n + 1) / 2) if n > 0 else 1)