# -*- coding: utf-8 -*-
"""
Learn Python the Hard Way: Exercise 33
"""

i = 0
numbers = []
six = 6

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)

print("The numbers: ")

for num in numbers:
    print(num)

def numbers_function(i):
    for i in range(0, 6):
        print("At the top i is %d" % i)

        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

numbers_function(6)
