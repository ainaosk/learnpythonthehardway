# -*- coding: utf-8 -*-
"""
Learn Python the Hard Way: Exercise 20
"""

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)# the "read head" moves to the start of the file (0 byte)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file :\n")

print_all(current_file)
print('')
print("Now let's rewind, kind of like a tape.\n")

rewind(current_file)

print("Let's print three lines:\n")

#print line number 1
current_line = 1
print_a_line(current_line, current_file)

#print line number 2
current_line += 1
print_a_line(current_line, current_file)

#print line number 3
current_line += 1
print_a_line(current_line, current_file)
