#File Header:
#Project Name: Project 4.3.5 Image Artist
#Authors: Varun G
#Date: 2/26/2023
#Description: Creates the box in which the donuts will be held and implements the userInput to place the donut

import PIL
import matplotlib.pyplot as plt
import os.path
import numpy as np
import random
from donut import Donut, CustomDonut
from options.flavors import TextureFlavor, GradientFlavor
from options.toppings import ParticleTopping
from userInput import donutInput
from options.donut_type import DonutType

#Dictionaries for the premade donuts, flavors, toppings, donut types, and locations
PREMADES = {
        'boston kreme': Donut.boston_kreme(),
        'french cruller': Donut.french_cruller(),
        'powdered': Donut.powdered(),
        'old fashioned': Donut.old_fashioned()
    }

FLAVORS = {
    'chocolate': GradientFlavor.chocolate(),
    'strawberry' : GradientFlavor.strawberry(),
    'vanilla': GradientFlavor.vanilla(),
    'halloween': GradientFlavor.halloween()  
}

HOLES = {
    'hole': DonutType.HOLE,
    'no hole': DonutType.NO_HOLE
}

TOPPINGS = {
    'chocolate sprinkles': ParticleTopping.chocolate_sprinkles(),
    'rainbow sprinkles': ParticleTopping.rainbow_sprinkles(),
    'm&ms': ParticleTopping.mnm(),
}

LOCATIONS = [
    (80, 40),
    (295, 40),
    (505, 40),
    (80, 260),
    (295, 260),
    (505, 260)
]

def createBox():
    '''Create a box for the donut to be placed in'''
    directory = os.path.dirname(os.path.abspath(__file__))
    box_filename = os.path.join(directory, 'images/donutBox.jpg')
    box = PIL.Image.open(box_filename)

    #Creates each donut based on the user input
    for i in range(6):
        print(f'Donut {i+1}:\n')
        options = donutInput()   #Calls the input statements for the user to answer

        #Alerts the user of the order they just placed
        if options[1] == "None":
            toppings = "no toppings"
        else: 
            toppings = options[1]
        print("Your order for Donut " + str(i+1) + " is now: " + options[0] + ", " + toppings + ", " + options[2])

        if options[0] in PREMADES:
            donut = PREMADES[options[0]]
        else:
            flavor = FLAVORS[options[0]]
            hole = HOLES[options[1]]
            try:
                toppings = [TOPPINGS[options[2]]]
            except KeyError:
                toppings = []

            donut = CustomDonut(flavor=flavor, donut_type=hole, toppings=toppings)

        image = donut.render().resize((200, 200))  #Resizes each donut to fit in the box
        box.paste(image, LOCATIONS[i], mask=image)  #Pastes the donut in the box



    box.show()                        #Renders the image
    box.save('poster_box.png')     #Saves the generated image to the program
