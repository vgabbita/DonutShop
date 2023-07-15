#File Header:
#Project Name: Project 4.3.5 Image Artist
#Authors: Varun G, Nikhil O, Matthew B
#Date: 2/26/2023
#Description: Defines the various flavors that each donut can have

from PIL import Image, ImageColor, ImageChops
from options.donut_type import DonutType

class Flavor:
    def __init__(self):
        pass

    def add(self, image):
        pass

class GradientFlavor(Flavor):
    def __init__(self, hue, saturation, lightness):
        # Dictionaries of ranges for circular gradient
        # ex: {0.5: (0, 0), 0.75: (0.5, 0.75), 1: (1, 1))
        self._hue = hue
        self._saturation = saturation
        self._lightness = lightness

    def add(self, donut):
        gradient = Image.new('RGBA', donut.image.size)
        for r in range(gradient.size[1]):
            for c in range(gradient.size[0]):
                # Get the distance from the center of the image
                distance = ((r - donut.center[1]) ** 2 + (c - donut.center[0]) ** 2) ** 0.5

                # Normalize the distance to a value between 0 and 1
                percent = distance / (gradient.size[0] / 2)

                # Get the color for the current pixel
                ranges = [self._hue, self._saturation, self._lightness]
                values = []
                for color_val in ranges:
                    value = color_val[list(color_val.keys())[-1]][-1]
                    for block, val_range in color_val.items():
                        if percent <= block:
                            blocks = list(color_val.keys())
                            blocks.insert(0, 0)
                            percent_range = block - blocks[blocks.index(block)-1]
                            value = (((percent - blocks[blocks.index(block)-1]) / percent_range) * (val_range[1] - val_range[0])) + val_range[0]
                            break
                    values.append(value)
                
                color = ImageColor.getrgb('hsl({}, {}%, {}%)'.format(values[0], values[1], values[2]))
                # Set the pixel to the color
                gradient.putpixel((c, r), color)
        donut.image.paste(gradient, mask=donut.mask)

    @classmethod
    def chocolate(cls):
        return cls({2: (4, 4)}, {2: (48, 48)}, {0.6: (15, 30), 0.7: (30, 35), 1: (35, 15)})

    @classmethod
    def strawberry(cls):
        return cls({2: (2, 2)}, {2: (92, 92)}, {0.6: (70, 80), 0.7: (80, 83), 1: (83, 70)})
    
    @classmethod
    def vanilla(cls):
        return cls({2: (0, 0)}, {2: (0, 0)}, {0.6: (80, 95), 0.7: (95, 100), 1: (100, 80)})
    
    @classmethod
    def halloween(cls):
        return cls({2: (37, 37)}, {0.7: (70, 100), 1: (100, 70)}, {0.7: (0, 70), 1: (70, 0)})

# This function puts an image over the donut 
#Ex. An image of actual strawberry on top of the donut
#Not implemented in the actual program because it was not a realistic donut for the donut shop
class TextureFlavor(Flavor):
    def __init__(self, filename):
        self._texture = Image.open(filename).convert('RGBA')
    
    def add(self, donut):
        resized_texture = self._texture.copy()
        resized_texture = resized_texture.resize(donut.image.size)
        resized_texture = ImageChops.offset(resized_texture, donut.image.size[1] // 2 - donut.center[0], donut.image.size[0] // 2 - donut.center[1])
        donut.image.paszte(resized_texture, mask=donut.mask)

    @classmethod
    def strawberry(cls):
        return cls('./textures/strawberry.webp')

