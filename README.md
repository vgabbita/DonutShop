# ImageProcessing
Project Name: Project 4.3.5 Image Artist
Authors: Varun G

Instructions: 
Run `python main.py`
You will be asked to order 6 donuts from the shop
Each donut has different preferences that you will be asked about
After the full order is placed, you will recieve an image containing all 6 of your donuts with your specified preferences

Changelog

Files: 

User Input: 
Asks the user to input their desired flavor, style, and topping for a singular donut
This function is called 6 times in a separate file for each of the donuts that the box will hold
Returns a list of three values fora singular donut.

Changes: 
Initially had while loops and if conditions inside one large for loop to allow the user to input their desired flavors, tppings, and style for all 6 donuts
Removed the large for loop and instead had the entire function itself be called 6 times in a separate file. 
 


Donut: 
The Donut Class handles the pre made donuts
Pre-made donuts - Any donuts that do not require the creation of a mask and will not contain any style or toppings (Old fashioned, Boston Kreme, Powdered, French Cruller)
Images taken from the images folder

The CustomDonut Class handles the custom donuts that are created based on the user's inputs
Takes into accout the user's preferences - whether the donut should have a hole and what flavor it should be


Flavors: 
Gradient Flavor class handles the color of the custom donuts
The single color flavors are created using a gradient, where the lightness of the color in the center of the ring is different from the inside and outside of the circle
The four possible color flavors are chocolate (brown gradient), strawberry (pink gradient), vanilla (white gradient), and halloween (orange gradient)

Changes: 
We initially wanted to implement the Texture flavor class but figured that it was not a realistic option that a customer would have at a donut shop
The class takes an already inputted image, and pastes it onto the donut in place of the icing and toppings - in this case, the image would be an image of strawberries from the textures folder

Toppings: 
The ParticleToppings class creates the three different toppings that are available for the custom donuts
These toppings include chocolate sprinkles, rainbow sprinkles, and M&Ms
The masks folder holds the specific masks used for the random creation of these toppings, and the color was randomly changed for each one. 

Changes: 
We initially wanted to have more toppings, including chocolate drizzle, and chocolate chips. However, we decided against it because the creation of these toppings were vey complicated and tedious. For example, the implementation of the chocolate drizzle was much harder than we originally thought. Instead, we just created multiple types of sprinkles, including chocolate sprinkles and rainbow sprinkles. 


Donut_type: 
This function sets the style value of a particular donut to either HOLE or NO_HOLE
Determines whether that particular donut should have a hole in it or not. 

Box:
The createBox function puts all the files and functions together to create the final product of an image of the six donuts in a box. Using a for loop, it calls the user input 6 times and then takes those user inputs and uses it as arguments for the functions that create the donut. Each donut is then placed in its corresponding place in the box. The final image is then rendered and save to the program. 

Main: 
This is the main python file
Run this in order to be prompted for donut preferences and get the desired output image



List of Commits:
1. Add resized donutBox
2. create donutBox
3. small update
4. finish Texture Flavor
5. add 6 test donuts to the box
6. first iteration of sprinkles
7. update userinput
8. finish particle topping work
9. donut pics added
10. make changes to user input and main
11. background burned all prebuilt images
12. test donut box
13. edit box to create donut
14. add predefined flavors and sprinkles
15. combine donut function with box function
16. add m&ms, fixes
17. add m&ms, fixes
18. add no-hole donut
19. clean up box generation
20. add comments and fix user Input
21. remove extraneous files
22. start implementing new flavor and normal donut
23. edit pictures
24. implement halloween flavor
25. remove debug files
26. resize old fashioned image
27. add comments and make some final edits
28. final edits
29. create README.md
30. create a readme file for the changelog
31. last edit before submission

