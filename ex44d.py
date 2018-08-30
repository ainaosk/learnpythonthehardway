# -*- coding: utf-8 -*-
"""

Learn Python the Hard Way: Exercise 44

"""

class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(Self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit() #PARENT implicit()
son.implicit() #PARENT implicit()

dad.override() #PARENT override()
son.override() #CHILD override()

dad.altered() #PARENT altered()
son.altered()
#CHILD, BEFORE PARENT altered()
#PARENT altered()
#CHILD AFTER PARENT altered()
