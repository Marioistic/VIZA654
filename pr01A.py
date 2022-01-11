# ========================================================
# Garvin Beltz
# 09/23/2020
# VIZA 654 - Digital Image
# Project 1A - PPM Reader
#
# This program will read in any P3 PPM file and
# read it back out as an exact copy. All the user has
# to do is indicate the input file and output file!
#
# The places the user needs to change will
# be marked below!
# ========================================================

file = open("blackbuck.ppm", "r")  # Opens the PPm file in read mode
mNumber = file.readline()  # Reads in the magic number from the file and stores it
if mNumber[0] != "P" and mNumber[1] != "3":  # Checks to see if the magic number is P3
    print("Error! You did not use a P3 PPM file!")  # and gives a warning and exits
    exit()                                          # program if it is not.

w_and_h = file.readline()  # Reads in the width and height as a combined value
while w_and_h.startswith("#"):  # Skips over any comments in the PPM header
    w_and_h = file.readline()

w_and_hList = w_and_h.split()  # Splits the combined width and height into a list
width = int(w_and_hList[0])  # Reads in first list index to get width
height = int(w_and_hList[1])  # Reads in 2nd index for height
maxval = int(file.readline())  # Reads in the max color value allowed for the image

image = file.readlines()  # The image data is read in as one large list
file.close()  # Closes the original file

ppmHeader = f'P3\n{width} {height}\n{maxval}\n'  # Compiles the new PPM header together

newFile = open("readImage.ppm", "w")  # Opens or creates the new output PPM
newFile.write(ppmHeader)  # Writes the PPM header to the new file
for element in image:  # Takes the list elements from the image data and copies it
    newFile.write(element)  # over to new file.
newFile.close()  # Closes new file. Always close your files!
