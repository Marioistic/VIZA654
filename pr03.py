# ================================================================
# Garvin Beltz
# 10/11/2021
# VIZA 654 - Digital Image
# Project 3 - Complex Vector to Raster Conversion

# This program will create an image of a convex shape, star,
# and a line. These images will be 2 colors with the shape
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

# =========================
# Draws the convex shape
# =========================


def draw_convex(width, height, sides, radius):

    cx = width / 2
    cy = height / 2
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
                    number = 0
                    for k in range(sides):  # Determines how many half planes a point is inside
                        if (((i+(m+Ri)/s)-cx-r*math.cos((k/sides)*2*math.pi))*math.cos((k/sides)*2*math.pi) + (
                                (j+(n+Rj)/s)-cy-r*math.sin((k/sides)*2*math.pi))*math.sin((k/sides)*2*math.pi)) <= 0:
                            number += 1

                    if number == sides:  # If a point is inside all half planes, then it is in the shape
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

# =======================
# Draws the star shape
# =======================


def draw_star(width, height, sides, radius):

    cx = width / 2
    cy = height / 2
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
                    number = 0
                    for k in range(sides):  # Determines how many half planes a point is inside
                        if (((i+(m+Ri)/s)-cx-r*math.cos((k/sides)*2*math.pi))*math.cos((k/sides)*2*math.pi) + (
                                (j+(n+Rj)/s)-cy-r*math.sin((k/sides)*2*math.pi))*math.sin((k/sides)*2*math.pi)) <= 0:
                            number += 1

                    if number >= sides - 1:  # If a point is in all or all but 1 half plane, then it is in the shape
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
# Draws the line shape
# ==============================


def draw_line(width, height, angle0, angle1):

    x = width / 2
    y = height / 2
    a0 = angle0
    a1 = angle1
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
                for n in range(s):  # Determines if a point is between 2 half planes
                    if (math.cos(a0) * ((i + (m + Ri) / s) - x) + math.sin(a0) * ((j + (n + Rj) / s) - y)) >= 0:
                        if (math.cos(a1) * ((i + (m + Ri) / s) - x) +
                                math.sin(a1) * ((j + (n + Rj) / s) - y)) - 5 <= 0:
                            red += 138
                            green += 3
                            blue += 3
                        else:
                            red += 212
                            green += 175
                            blue += 55
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


colorConvex = draw_convex(500, 500, 8, 100)
colorStar = draw_star(500, 500, 5, 50)
colorLine = draw_line(500, 500, 15, 15)

# ============================================================================
# Calls the make file function that combines the header with the image data.
# ============================================================================
imageConvex = make_file("P3", "500", "500", "255", colorConvex)
imageStar = make_file("P3", "500", "500", "255", colorStar)
imageLine = make_file("P3", "500", "500", "255", colorLine)

# ==========================================
# Writes the combined image out to a file
# ==========================================
fileConvex = open("convex.ppm", "w")
fileConvex.write(imageConvex)
fileConvex.close()

fileStar = open("star.ppm", "w")
fileStar.write(imageStar)
fileStar.close()

fileLine = open("line.ppm", "w")
fileLine.write(imageLine)
fileLine.close()
