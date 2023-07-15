#File Header:
#Project Name: Project 4.3.5 Image Artist
#Authors: Varun G, Nikhil O, Matthew B
#Date: 2/26/2023
#Description: 
# At each pixel interval, put the center of one sprinkle
# Adjust it randomly by a bit
# Also add a random dropout chance
# Random rotation

from PIL import Image, ImageChops
import random
import os
import matplotlib.pyplot as plt

class ParticleTopping:
    '''Randomly add the sprinkles onto a particular donut'''
    def __init__(self, dir_path, files, colors, size_factor=0.21, topping_density=20):
        self._dir_path = dir_path
        self._files = files
        self._colors = colors
        self._size_factor = size_factor
        self._topping_density = topping_density

    def add(self, donut):
        interval = donut.image.size[0] // self._topping_density
        for r in range(0, donut.image.size[1], interval):
            for c in range(0, donut.image.size[0], interval):
                r += random.randint(-interval // 4, interval // 4)
                c += random.randint(-interval // 4, interval // 4)
                # Get a random sprinkle image and resize it appropriately
                sprinkle = Image.open(self._dir_path + '/' + random.choice(self._files)).convert('RGBA')
                sprinkle = sprinkle.resize((int(sprinkle.size[0] * self._size_factor), int(sprinkle.size[1] * self._size_factor)))

                # Rotate the sprinkle randomly
                sprinkle = sprinkle.rotate(random.randint(0, 360), expand=True)

                # Choose a random color for the sprinkle
                sprinkle_color = random.choice(self._colors)

                sprinkle_mask = Image.new('RGBA', donut.mask.size, (255, 255, 255, 0))
                sprinkle_mask.paste(sprinkle, (c - sprinkle.size[0] // 2, r - sprinkle.size[1] // 2))
                intersected_mask = ImageChops.multiply(donut.mask, sprinkle_mask)
                # plt.imshow(intersected_mask)
                # plt.show()
                if random.randint(0, 300) == 55:
                    donut.mask.save('donut_mask.png')
                    intersected_mask.save('intersected_mask.png')
                    sprinkle_mask.save('sprinkle_mask.png')

                color_layer = Image.new('RGBA', donut.image.size, sprinkle_color)
                donut.image.paste(color_layer, mask=intersected_mask)

    #The different topping that can be added to a donut
    @classmethod
    def chocolate_sprinkles(cls):
        return cls('./masks/sprinkles', [str(i) + '.png' for i in range(1, 7)], [(61, 42, 21), (65, 34, 34), (59, 30, 29), (39, 7, 5)])
    
    @classmethod
    def rainbow_sprinkles(cls):
        return cls('./masks/sprinkles', [str(i) + '.png' for i in range(1, 7)], [(255, 200, 200), (255, 200, 128), (255, 255, 200), (200, 255, 200), (200, 200, 255), (200, 128, 255), (148, 78, 211)])
    
    @classmethod
    def mnm(cls):
        return cls('./masks/mnm', [str(i) + '.png' for i in range (1, 4)], [(253, 108, 45), (44, 145, 251), (31, 194, 67), (119, 84, 91), (252, 58, 85), (247, 231, 11)], size_factor=0.1, topping_density=10)
    
