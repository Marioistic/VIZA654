# ========================================================
# Garvin Beltz
# 09/23/2020
# VIZA 654 - Digital Image
# Project 1B - Procedural PPM Generator
#
# This program will procedurally generate a random PPM
# image every time it is run. All the user needs to do
# is run the program and the code will do the rest!
#
# If you want to save out multiple images, then just
# change the file name where indicated below!
# ========================================================

import random  # Random function is used to randomize variables

# Create the PPM header data

mNumber = "P6"  # The magic number determines how the image is stored (P6 = Binary/P3 = ASCII)
width = random.randint(600, 900)  # Randomizes the image width
height = random.randint(600, 900)  # Randomizes the image height
maxval = 255  # Determines the maximum color value allowed. 255 supports all colors

ppmHeader = f'P6\n{width} {height}\n{maxval}\n'  # Combines the above info into the complete header

# Create the image data

image = []  # Creates an empty list to store raw RGB values
pixel = ""  # Creates empty string to store ASCII converted values
for i in range(width):  # Nested for loop that takes the RGB data
    image.append([])    # and converts it into ASCII form for writing out
    for j in range(height):
        image[i].append({"r": random.randint(0, 255), "g": random.randint(0, 255), "b": random.randint(0, 255)})
        redChannel = image[i][j]["r"]  # The dictionary above creates the RGB values in the form [R, G, B]
        greenChannel = image[i][j]["g"]  # These 3 lines separate the color values
        blueChannel = image[i][j]["b"]  # before they are converted to ASCII in the next line
        pixelString = str(chr(redChannel)) + str(chr(blueChannel)) + str(chr(greenChannel))
        pixel += pixelString  # All the ASCII characters are combined into the empty string from earlier

# This is where the ASCII data and the PPM header are written out to a file
# The first line opens a file in write mode with the name listed.
# If the file does not already exist it will be created.

file = open('genImage01.ppm', "wb")  # Change the green data in the '' BEFORE the , to make a new file
file.write(ppmHeader.encode())  # Writes the header data to the file as binary
file.write(pixel.encode())  # Writes the image data to the file as binary
file.close()  # Closes the file. Always close a file when done with it!
