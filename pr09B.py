# ================================================================
# Garvin Beltz
# 11/22/2021
# VIZA 654 - Digital Image
# Project 9A - Floyd-Steinberg Dither
#
# This program will apply a Floyd-Steinberg Dither operation
# to an image.
# =================================================================

import cv2
import numpy as np

# Read in base image and get width and height
base = cv2.imread("base.jpg")

height = base.shape[0]
width = base.shape[1]


def minmax(pixel):
    if pixel > 255:
        pixel = 255
    if pixel < 0:
        pixel = 0
    return pixel


def color(base, newarray):
    for y in range(0, height - 1):
        for x in range(1, width - 1):
            # Initial pixel in form b, g, r
            oldBlue = base[y, x, 0]
            oldGreen = base[y, x, 1]
            oldRed = base[y, x, 2]

            # New pixel in form b, g, r
            newBlue = np.round(newarray * oldBlue/255.0) * (255/newarray)
            newGreen = np.round(newarray * oldGreen/255.0) * (255/newarray)
            newRed = np.round(newarray * oldRed/255.0) * (255/newarray)

            # Apply the new color values to base array
            base[y, x, 0] = newBlue
            base[y, x, 1] = newGreen
            base[y, x, 2] = newRed

            errorBlue = oldBlue - newBlue
            errorGreen = oldGreen - newGreen
            errorRed = oldRed - newRed

            # Calculate using: 7/16, 3/16, 5/16, 1/16
            # I(x,y+1)
            # I(x+1,y-1)
            # I(x+1,y)
            # I(x+1,y+1)

            base[y, x + 1, 0] = minmax(base[y, x + 1, 0] + errorBlue * 7 / 16)
            base[y, x + 1, 1] = minmax(base[y, x + 1, 1] + errorGreen * 7 / 16)
            base[y, x + 1, 2] = minmax(base[y, x + 1, 2] + errorRed * 7 / 16)

            base[y + 1, x - 1, 0] = minmax(base[y + 1, x - 1, 0] + errorBlue * 3 / 16)
            base[y + 1, x - 1, 1] = minmax(base[y + 1, x - 1, 1] + errorGreen * 3 / 16)
            base[y + 1, x - 1, 2] = minmax(base[y + 1, x - 1, 2] + errorRed * 3 / 16)

            base[y + 1, x, 0] = minmax(base[y + 1, x, 0] + errorBlue * 5 / 16)
            base[y + 1, x, 1] = minmax(base[y + 1, x, 1] + errorGreen * 5 / 16)
            base[y + 1, x, 2] = minmax(base[y + 1, x, 2] + errorRed * 5 / 16)

            base[y + 1, x + 1, 0] = minmax(base[y + 1, x + 1, 0] + errorBlue * 1 / 16)
            base[y + 1, x + 1, 1] = minmax(base[y + 1, x + 1, 1] + errorGreen * 1 / 16)
            base[y + 1, x + 1, 2] = minmax(base[y + 1, x + 1, 2] + errorRed * 1 / 16)

    return base


# Output the dithered image
colorImage = color(base.copy(), 1)
cv2.imwrite("floydStein.jpg", colorImage)
