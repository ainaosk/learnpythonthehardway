# -*- coding: utf-8 -*-
"""
Learn Python the Hard Way: Exercise 18
"""

def print_two(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))

def print_one(arg1):
    print("arg1: %r" % arg1)

def print_none():
    print("I got nothin'.")

print_two("My", "Name")
print_one("First!")
print_none()
