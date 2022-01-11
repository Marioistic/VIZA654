# ================================================================
# Garvin Beltz
# 11/22/2021
# VIZA 654 - Digital Image
# Project 9A - Ordered Dither
#
# This program will apply a 4x4 Ordered Dither to an image.
# =================================================================

from PIL import Image
import numpy as np

base = Image.open("base.jpg")
baseData = base.load()
width, height = base.size

kernel = np.random.randint(255, size=(4, 4))

for x in range(width):
    for y in range(height):
        basePixel = base.getpixel((x, y))
        baseRed = basePixel[0]
        baseGreen = basePixel[1]
        baseBlue = basePixel[2]

        baseAvg = (baseRed + baseGreen + baseBlue) / 3

        if baseAvg < kernel[x % 4][y % 4]:
            baseRed = 0
            baseGreen = 0
            baseBlue = 0
        else:
            baseRed = basePixel[0]
            baseGreen = basePixel[1]
            baseBlue = basePixel[2]

        base.putpixel((x, y), (baseRed, baseGreen, baseBlue))

base.save("colorOrder.jpg")









