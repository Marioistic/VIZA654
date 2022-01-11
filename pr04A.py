# ================================================================
# Garvin Beltz
# 10/18/2021
# VIZA 654 - Digital Image
# Project 4A - Piecewise-linear Curve Color Manipulation

# This program will manipulate the color of an image by using a
# piecewise-linear curve. The RGB values are split into 3 channels
# and can all be adjusted individually to produce different results.
#
# Note: Changing the values can be done where marked below!
# =================================================================

from PIL import Image

# =============================================================
# Read in RGB values, edit them, and write out to a new file
# ==============================================================
base = Image.open("base.JPG")
basePixel = base.load()  # Load in image data and then find width and height
Width, Height = base.size

for x in range(Width):
    for y in range(Height):
        # Getting the RGB pixel value
        baseColor = base.getpixel((x, y))  # (R, G, B)
        #  Initialize the new values with the old ones
        red = baseColor[0]
        green = baseColor[1]
        blue = baseColor[2]
        #  Each if statement handles a particular color
        #  All numbers other than the 1 or index positions can be changed.
        #  The if statement values and the values in the "shift" variable must match.
        if baseColor[0] > 50 and baseColor[0] <= 200:
            shift = (baseColor[0] - 50) / (200 - 50)
            red = int((1 - shift) * 50 + shift * 75)
        if baseColor[1] > 50 and baseColor[1] <= 200:
            shift = (baseColor[1] - 50) / (200 - 100)
            green = int((1 - shift) * 50 + shift * 75)
        if baseColor[2] > 50 and baseColor[2] <= 200:
            shift = (baseColor[2] - 50) / (200 - 50)
            blue = int((1 - shift) * 25 + shift * 75)

        base.putpixel((x, y), (red, green, blue))

base.save("test3.jpg")  # Writes out a new file.
