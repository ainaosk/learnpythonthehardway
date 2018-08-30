# -*- coding: utf-8 -*-
"""
Learn Python the Hard Way: Exercise 32
"""

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print("This is count %d" % number)

for fruit in fruits:
    print("A fruit of type: %s" % fruit)

for i in change:
    print("I got %r" % i)
    #in a mixed list, we have to use %r since we don't know what's in it

elements = [] #build empty list

for i in range(0, 6):
    print("Adding %d to the list." % i)
    elements.append(i) #add i to list "elements"

for i in elements: #prints the elements in the list
    print("Element was: %d" % i)
