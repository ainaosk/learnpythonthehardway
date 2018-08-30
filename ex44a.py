# -*- coding: utf-8 -*-
"""
Exercise 44: Inheritance
"""

#Implicit inheritance
class Parent(object):
    
    def implicit(self):
        print("PARENT implicit()")
        
class Child(Parent):
    pass #tells Python to create empty block. 
    #The class Child() will inherit all its behavior from Parent()

dad = Parent()
son = Child()

print("Dad: ")
dad.implicit()
print("Son: ")
son.implicit()
