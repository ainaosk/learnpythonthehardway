# -*- coding: utf-8 -*-
"""
Learn Python the Hard Way: Exercise 38
"""

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ') #split on space
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #removes last item from more_stuff list
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There's %d items now." % len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1]) #print second item of stuff
print(stuff[-1]) #print last item of stuff
print(stuff.pop()) #remove last item from stuff
print(' '.join(stuff)) #join all elements in one string with a space between each
print('#'.join(stuff[3:5]))#join items 3 and 4 with a # between them
