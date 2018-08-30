# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 08:59:21 2018

@author: Aina
"""

#Symbol review

def tasty_fruit():
    
    fruit_response = input("What kind of fruit do you like? \n > ")
    
    if "apple" or "apples" in fruit_response:
        print("Apples are great!")
    elif "orange" or "oranges" in fruit_response:
        print("Oranges are best squeezed..")
    elif "pear" or "pears" in fruit_response:
        print("Pears are sweet, but make a mess.")
    else:
        print("Is that a fruit? Not in my world..")

tasty_fruit()
