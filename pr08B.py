# ================================================================
# Garvin Beltz
# 11/15/2021
# VIZA 654 - Digital Image
# Project 8B - Compositing
#
# This program will composite one image on top of another
# by using a black and white alpha image. The program looks
# for black and white locations in the alpha file and will use
# those values to composite the foreground (white areas)
# onto the background (black areas). Any grey values will
# be calculated by taking the average of the two images.
# =================================================================

from PIL import Image

# Read in foreground image
over = Image.open("comp.png")
overData = over.load()
# Read in alpha image
alpha = Image.open("compAlpha.png")
alphaData = alpha.load
# Read in background image
under = Image.open("castle.jpeg")
underData = under.load()

# Obtain width and height (Both images must be the EXACT same size)
width, height = over.size

for x in range(width):
    for y in range(height):
        # Read in foreground color channels
        overPixel = over.getpixel((x, y))
        overRed = overPixel[0]
        overGreen = overPixel[1]
        overBlue = overPixel[2]
        # Read in one of the RGB channels to use as alpha
        alphaPixel = alpha.getpixel((x, y))
        alphaValue = alphaPixel[0]
        # Read in background color channels
        underPixel = under.getpixel((x, y))
        underRed = underPixel[0]
        underGreen = underPixel[1]
        underBlue = underPixel[2]
        # Determine if the pixel is in or out of the comp area
        if alphaValue == 0:
            finalRed = underRed
            finalGreen = underGreen
            finalBlue = underBlue
        elif alphaValue == 255:
            finalRed = overRed
            finalGreen = overGreen
            finalBlue = overBlue
        # Handles the edge case
        else:
            finalRed = (underRed + overRed) / 2
            finalGreen = (underGreen + overGreen) / 2
            finalBlue = (underBlue + overBlue) / 2

        over.putpixel((x, y), (int(finalRed), int(finalGreen), int(finalBlue)))

# Writes the image out to a new file
over.save("newComp.jpg")
