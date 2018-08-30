# -*- coding: utf-8 -*-
"""
Learn Python the Hard Way: Exercise 44b

"""
class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(Self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()
