# ================================================================
# Garvin Beltz
# 11/15/2021
# VIZA 654 - Digital Image
# Project 8A - Compositing
#
# This program will composite two images together using
# different compositing operators. The color channels of both
# images are read in, and then they are edited into a final
# color value using various formulas.
#
# Operators included in this code are: Normal, Darken, Multiply
# Add, Lighten, Difference, and Exclusion

# To switch between the varying operators you just have to change
# which lines are commented out at the bottom of this code.
# =================================================================

from PIL import Image

# Read in foreground image
over = Image.open("over.jpg")
overData = over.load()
# Read in background image
under = Image.open("under.jpeg")
underData = under.load()
# Obtain width and height (Both images must be the EXACT same size)
width, height = over.size


# Normal operator
def normal():
    # Apply the operator to each pixel in the image
    for x in range(width):
        for y in range(height):
            overAlpha = 0.75  # Alpha needs to be less than 1 to be able to see the result
            # Read in foreground color channels
            overPixel = over.getpixel((x, y))
            overRed = overPixel[0]
            overGreen = overPixel[1]
            overBlue = overPixel[2]
            # Read in background color channels
            underPixel = under.getpixel((x, y))
            underRed = underPixel[0]
            underGreen = underPixel[1]
            underBlue = underPixel[2]
            # Perform operation on color channels
            normalRed = overRed
            normalGreen = overGreen
            normalBlue = overBlue
            # Apply new color channel values to the image
            finalRed = overAlpha * normalRed + (1 - overAlpha) * underRed
            finalGreen = overAlpha * normalGreen + (1 - overAlpha) * underGreen
            finalBlue = overAlpha * normalBlue + (1 - overAlpha) * underBlue
            over.putpixel((x, y), (int(finalRed), int(finalGreen), int(finalBlue)))


# Darken operator
def darken():

    for x in range(width):
        for y in range(height):
            overAlpha = 1  # Can be changed on a scale of 0-1
            # Read in foreground color channels
            overPixel = over.getpixel((x, y))
            overRed = overPixel[0]
            overGreen = overPixel[1]
            overBlue = overPixel[2]
            # Read in background color channels
            underPixel = under.getpixel((x, y))
            underRed = underPixel[0]
            underGreen = underPixel[1]
            underBlue = underPixel[2]
            # Perform operation on color channels
            darkenRed = min(underRed, overRed)
            darkenGreen = min(underGreen, overGreen)
            darkenBlue = min(underBlue, overBlue)
            # Apply new color channel values to the image
            finalRed = overAlpha * darkenRed + (1 - overAlpha) * underRed
            finalGreen = overAlpha * darkenGreen + (1 - overAlpha) * underGreen
            finalBlue = overAlpha * darkenBlue + (1 - overAlpha) * underBlue
            over.putpixel((x, y), (int(finalRed), int(finalGreen), int(finalBlue)))


def multiply():

    for x in range(width):
        for y in range(height):
            overAlpha = 1  # Can be changed on a scale of 0-1
            # Read in foreground color channels
            overPixel = over.getpixel((x, y))
            overRed = overPixel[0]
            overGreen = overPixel[1]
            overBlue = overPixel[2]
            # Read in background color channels
            underPixel = under.getpixel((x, y))
            underRed = underPixel[0]
            underGreen = underPixel[1]
            underBlue = underPixel[2]
            # Perform operation on color channels
            # Values need to be divided by 255 to ensure they stay within 0-255
            multiplyRed = underRed * overRed / 255
            multiplyGreen = underGreen * overGreen / 255
            multiplyBlue = underBlue * overBlue / 255
            # Apply new color channel values to the image
            finalRed = overAlpha * multiplyRed + (1 - overAlpha) * underRed
            finalGreen = overAlpha * multiplyGreen + (1 - overAlpha) * underGreen
            finalBlue = overAlpha * multiplyBlue + (1 - overAlpha) * underBlue
            over.putpixel((x, y), (int(finalRed), int(finalGreen), int(finalBlue)))


def add():

    for x in range(width):
        for y in range(height):
            overAlpha = 1  # Can be changed on a scale of 0-1
            # Read in foreground color channels
            overPixel = over.getpixel((x, y))
            overRed = overPixel[0]
            overGreen = overPixel[1]
            overBlue = overPixel[2]
            # Read in background color channels
            underPixel = under.getpixel((x, y))
            underRed = underPixel[0]
            underGreen = underPixel[1]
            underBlue = underPixel[2]
            # Perform operation on color channels
            # The if statements are needed to ensure the values do not go over 255
            addRed = underRed + overRed
            if addRed > 255:
                addRed = 255
            addGreen = underGreen + overGreen
            if addGreen > 255:
                addGreen = 255
            addBlue = underBlue + overBlue
            if addBlue > 255:
                addBlue = 255
            # Apply new color channel values to the image
            finalRed = overAlpha * addRed + (1 - overAlpha) * underRed
            finalGreen = overAlpha * addGreen + (1 - overAlpha) * underGreen
            finalBlue = overAlpha * addBlue + (1 - overAlpha) * underBlue
            over.putpixel((x, y), (int(finalRed), int(finalGreen), int(finalBlue)))


def lighten():

    for x in range(width):
        for y in range(height):
            overAlpha = 1  # Can be changed on a scale of 0-1
            # Read in foreground color channels
            overPixel = over.getpixel((x, y))
            overRed = overPixel[0]
            overGreen = overPixel[1]
            overBlue = overPixel[2]
            # Read in background color channels
            underPixel = under.getpixel((x, y))
            underRed = underPixel[0]
            underGreen = underPixel[1]
            underBlue = underPixel[2]
            # Perform operation on color channels
            lightenRed = max(underRed, overRed)
            lightenGreen = max(underGreen, overGreen)
            lightenBlue = max(underBlue, overBlue)
            # Apply new color channel values to the image
            finalRed = overAlpha * lightenRed + (1 - overAlpha) * underRed
            finalGreen = overAlpha * lightenGreen + (1 - overAlpha) * underGreen
            finalBlue = overAlpha * lightenBlue + (1 - overAlpha) * underBlue
            over.putpixel((x, y), (int(finalRed), int(finalGreen), int(finalBlue)))


def difference():

    for x in range(width):
        for y in range(height):
            overAlpha = 1  # Can be changed on a scale of 0-1
            # Read in foreground color channels
            overPixel = over.getpixel((x, y))
            overRed = overPixel[0]
            overGreen = overPixel[1]
            overBlue = overPixel[2]
            # Read in background color channels
            underPixel = under.getpixel((x, y))
            underRed = underPixel[0]
            underGreen = underPixel[1]
            underBlue = underPixel[2]
            # Perform operation on color channels
            # The abs() ensures that the value is not negative
            diffRed = abs(overRed - underRed)
            diffGreen = abs(overGreen - underGreen)
            diffBlue = abs(overBlue - underBlue)
            # Apply new color channel values to the image
            finalRed = overAlpha * diffRed + (1 - overAlpha) * underRed
            finalGreen = overAlpha * diffGreen + (1 - overAlpha) * underGreen
            finalBlue = overAlpha * diffBlue + (1 - overAlpha) * underBlue
            over.putpixel((x, y), (int(finalRed), int(finalGreen), int(finalBlue)))


def exclusion():

    for x in range(width):
        for y in range(height):
            overAlpha = 1  # Can be changed on a scale of 0-1
            # Read in foreground color channels
            overPixel = over.getpixel((x, y))
            overRed = overPixel[0]
            overGreen = overPixel[1]
            overBlue = overPixel[2]
            # Read in background color channels
            underPixel = under.getpixel((x, y))
            underRed = underPixel[0]
            underGreen = underPixel[1]
            underBlue = underPixel[2]
            # Perform operation on color channels
            # Values need to be positive and divided by 255 to stay in range
            exRed = abs(1 - (underRed * overRed / 255))
            exGreen = abs(1 - (underGreen * overGreen / 255))
            exBlue = abs(1 - (underBlue * overBlue / 255))
            # Apply new color channel values to the image
            finalRed = overAlpha * exRed + (1 - overAlpha) * underRed
            finalGreen = overAlpha * exGreen + (1 - overAlpha) * underGreen
            finalBlue = overAlpha * exBlue + (1 - overAlpha) * underBlue
            over.putpixel((x, y), (int(finalRed), int(finalGreen), int(finalBlue)))


normal()
over.save("normal.jpg")

# darken()
# over.save("darken.jpg")

# multiply()
# over.save("multiply.jpg")

# add()
# over.save("add.jpg")

# lighten()
# over.save("lighten.jpg")

# difference()
# over.save("difference.jpg")

# exclusion()
# over.save("exclusion.jpg")
