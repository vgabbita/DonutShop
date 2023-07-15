#File Header:
#Project Name: Project 4.3.5 Image Artist
#Authors: Varun G
#Date: 2/26/2023
#Description: This program allows the user input their desired donut. The user can choose the flavor, toppings, and style of the donut.

import colorsys

def donutInput():
    '''User inputs:
    Flavors of each donut: None(old fashioned), Chocolate, Strawberry, Vanilla, Halloween, Boston Creme, Powdered, French Cruller
    the number and type of toppings on the donut: None, Sprinkles, Chocolate Syrup, Vanilla Icing, Chocolate chips
    Style: no hole, hole
    All images compiled into one image
    Number of donuts is 6

    Example list --> Standard donut: [flavor, hole, topping]
    
    returns a list of donut values
    '''
    donuts = []         #List that will hold the user's preference for each donut

    # List of donut flavors and toppings
    donutFlavors = ["old fashioned", "chocolate", "strawberry", "vanilla", "halloween", "boston kreme", "powdered", "french cruller"]
    donutToppings = ["rainbow sprinkles", "chocolate sprinkles", "m&ms", "none"]

    # Gathers donut information from user
    donutbool = True
    while donutbool:
        flavor = input("What flavor do you want (Old Fashioned, Chocolate, Strawberry, Vanilla, Halloween, Boston Kreme, Powdered, French Cruller): ")
        flavor = flavor.lower()
        if flavor in donutFlavors:
            donuts.append(flavor)
            donutbool = False
        else:
            donutbool = True 

    #Donuts that are pre-made and should not have any toppings or holes. 
    if donuts[0] == "boston kreme" or donuts[0] == "powdered" or donuts[0] == "french cruller" or donuts[0] == "old fashioned":
        topValue = False
        holeValue = False 
        style = "no hole"
        donuts.append("None")
    else: 
        topValue = True
        holeValue = True

    # Input for hole or no hole
    while (holeValue): 
        hole = input("Would you like the donut to have a hole? [y/n]  ")
        if hole=="y":
            style = 'hole'
            holeValue = False
        elif hole=="n":
            style= 'no hole'
            holeValue = False
        else:
            holeValue = True    
    donuts.append(style)
        
    # Input for donut toppings
    while (topValue):
        toppings = input("What topping would you like (Rainbow Sprinkles, Chocolate Sprinkles, M&Ms, None)? ")
        toppings = toppings.lower()
        if(toppings in donutToppings):
            donuts.append(toppings)
            topValue = False
        else:
            topValue = True

    return donuts



