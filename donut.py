#File Header:
#Project Name: Project 4.3.5 Image Artist
#Authors: Varun G
#Date: 2/26/2023
#Description: Creates each singular donut depending on whether the donut is a premade donut or a donut with a topping and flavor

from PIL import Image
from options.flavors import Flavor, GradientFlavor, TextureFlavor
from options.toppings import ParticleTopping
from options.donut_type import DonutType

class Donut:
    '''Handles the premade donuts - Boston Kreme, French Cruller, and Powdered, Old Fashioned
       Renders an already inputted image'''
    def __init__(self, *, file_name=None):
        self._image = Image.open(f'./images/{file_name}').convert('RGBA').resize((512, 512))

    @property
    def image(self):
        return self._image

    def render(self):
        return self._image
    
    @classmethod
    def boston_kreme(cls):
        return cls(file_name='bostonkreme.png')
    
    @classmethod
    def french_cruller(cls):
        return cls(file_name='frenchcruller.png')
    
    @classmethod
    def powdered(cls):
        return cls(file_name='powdered.png')
    
    @classmethod
    def old_fashioned(cls):
        return cls(file_name='oldfashioned.png')

    
class CustomDonut(Donut):
    '''Donut is the superclass
       Handles the custom donuts - any donut that is not a frnech cruller, powdered, or boston kreme
       Factors the other donut list values into the creation of the rendering'''
    def __init__(self, *, flavor=None, donut_type=DonutType.HOLE, toppings=[]):
        file_name = {DonutType.HOLE: 'donut.png', DonutType.NO_HOLE: 'no_hole.png'}[donut_type]
        super().__init__(file_name=file_name)

        self._flavor = flavor
        self._donut_type = donut_type
        self._toppings = toppings

        self._mask = Image.open(f'./masks/{file_name}').convert('RGBA').resize((512, 512))
        self._center = (self._image.size[0] // 2, self._image.size[1] // 2)

    @property
    def mask(self):
        return self._mask

    @property
    def center(self):
        return self._center
    
    def render(self):
        self._flavor.add(self)
        for topping in self._toppings:
            topping.add(self)
        self._image.save('testend3.png')
        return self._image


if __name__ == "__main__":
    #Creates a donut with custom parameters
    d = CustomDonut(flavor=GradientFlavor.halloween(), toppings=[ParticleTopping.rainbow_sprinkles()], donut_type=DonutType.HOLE)
    d.render()

