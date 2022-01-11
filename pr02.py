# ================================================================
# Garvin Beltz
# 10/04/2021
# VIZA 654 - Digital Image
# Project 2 - Simple Vector to Raster Conversion and Antialiasing

# This program will create an image of a half plane, circle,
# and polynomial. These images will be 2 colors with the shape
# being one color and the background the other. The program will
# then blend the border between the colors with antialiasing.
#
# Note: You may wish to run the shape functions 1 at a time
# as it can take quite some time to do all of them at once
# on slower machines. Just comment out the shapes you don't
# want to run in the bottom 3 sections!
# =================================================================

import math
import random

# ==========================================
# Makes the header file for the PPM image
# ==========================================


def make_file(mnumber, width, height, maxval, data):

    filedata = "{0}\n{1} {2}\n{3}\n{4}\n".format(mnumber, width, height, maxval, data)

    return filedata

# ==============================
# Draws the half plane shape
# ==============================


def draw_plane(width, height, angle):

    x = 250
    y = 250
    a = angle
    pixel = ""
    s = 10  # Sample size for sub pixels
    for i in range(width):
        for j in range(height):
            red = 0
            green = 0
            blue = 0
            Ri = random.random()  # Randomizes jitter from 0 to 1
            Rj = random.random()
            for m in range(s):
                for n in range(s):
                    if (math.cos(a) * ((i + (m + Ri) / s) - x) + math.sin(a) * ((j + (n + Rj) / s) - y)) <= 0:
                        red += 138
                        green += 3
                        blue += 3
                    else:
                        red += 212
                        green += 175
                        blue += 55

            red = red / (s * s)  # Averages out color based on sub pixel samples
            green = green / (s * s)
            blue = blue / (s * s)

            pixel += str(int(red)) + " " + str(int(green)) + " " + str(int(blue)) + " "

    return pixel

# =========================
# Draws the circle shape
# =========================


def draw_circle(width, height, radius):

    x = 250
    y = 250
    r = radius
    pixel = ""
    s = 10  # Sample size for sub pixels
    for i in range(width):
        for j in range(height):
            red = 0
            green = 0
            blue = 0
            Ri = random.random()  # Randomizes jitter from 0 to 1
            Rj = random.random()
            for m in range(s):
                for n in range(s):
                    if ((x - (i + (m + Ri) / s)) ** 2 + (y - (j + (n + Rj) / s)) ** 2 - r ** 2) <= 0:
                        red += 138
                        green += 3
                        blue += 3
                    else:
                        red += 212
                        green += 175
                        blue += 55

            red = red / (s * s)  # Averages out color based on sub pixel samples
            green = green / (s * s)
            blue = blue / (s * s)

            pixel += str(int(red)) + " " + str(int(green)) + " " + str(int(blue)) + " "

    return pixel

# ==============================
# Draws the polynomial shape
# ==============================


def draw_polynom(width, height, angle, radius):

    x = 250
    y = 250
    a = angle
    r = radius
    pixel = ""
    s = 10  # Sample size for sub pixels
    for i in range(width):
        for j in range(height):
            red = 0
            green = 0
            blue = 0
            Ri = random.random()  # Randomizes jitter from 0 to 1
            Rj = random.random()
            for m in range(s):
                for n in range(s):
                    if ((x - (i + (m + Ri) / s)) ** 2 + (y - (j + (n + Rj) / s)) ** 2 - r ** 2) <= 0 and (math.cos(a) * ((i + (m + Ri) / s) - x) + math.sin(a) * ((j + (n + Rj) / s) - y)) <= 0:
                        red += 138
                        green += 3
                        blue += 3
                    else:
                        red += 212
                        green += 175
                        blue += 55

            red = red / (s * s)  # Averages out color based on sub pixel samples
            green = green / (s * s)
            blue = blue / (s * s)

            pixel += str(int(red)) + " " + str(int(green)) + " " + str(int(blue)) + " "

    return pixel

# ================================================================
# Calls each draw function and assigns image data to a variable
# ================================================================


colorPlane = draw_plane(500, 500, 15)
colorCircle = draw_circle(500, 500, 200)
colorPolynom = draw_polynom(500, 500, 15, 200)

# ============================================================================
# Calls the make file function that combines the header with the image data.
# ============================================================================
imagePlane = make_file("P3", "500", "500", "255", colorPlane)
imageCircle = make_file("P3", "500", "500", "255", colorCircle)
imagePolynom = make_file("P3", "500", "500", "255", colorPolynom)

# ==========================================
# Writes the combined image out to a file
# ==========================================
filePlane = open("halfPlane.ppm", "w")
filePlane.write(imagePlane)
filePlane.close()

fileCircle = open("circle.ppm", "w")
fileCircle.write(imageCircle)
fileCircle.close()

filePolynom = open("polynom.ppm", "w")
filePolynom.write(imagePolynom)
filePolynom.close()
