# ================================================================
# Garvin Beltz
# 11/08/2021
# VIZA 654 - Digital Image
# Project 7 - Transformations and Warping
#
# This program will apply the following transformations to an
# image: Rotation, Scaling, Shear, Mirror, Translation,
# and perspective. Bilinear Warping and an additional
# bonus transformation have not been implemented.

# Please note that, while the functions do technically
# produce the required transformation, they do so in
# a generally undesirable way.

# To switch between functions just adjust what lines are commented
# out at the bottom of this code. It is not recommended to run
# more than one at a time.
# =================================================================

from PIL import Image
import math

# Loads base image
img = Image.open("base.jpg")
imgData = img.load()
width, height = img.size

# Rotation function
def rotation():
    # Loops through each pixel in the image
    for x in range(width):
        for y in range(height):
            # Formula for rotation
            u = x * math.cos(math.radians(45)) + y * math.sin(math.radians(45))
            v = y * math.cos(math.radians(45)) - x * math.sin(math.radians(45))

            # Makes sure that the resulting u/v value is inside the image
            if u < 0:
                u = width - (u % width) - 1
            elif u > width - 1:
                u = width - (u % width) - 1

            if v < 0:
                v = height - (v % height) - 1
            elif v > height - 1:
                v = height - (v % height) - 1
            # Applies the u and v value to the x and y positions in the image
            pixel = img.getpixel((u, v))
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            # Sets the new RGB value based upon the kernel
            img.putpixel((int(x), int(y)), (red, green, blue))


# Scale function
def scale():
    # Loops through each pixel in the image
    for x in range(width):
        for y in range(height):
            # Formula for scale
            u = x / 0.5
            v = y / 0.5
            # Makes sure that the resulting u/v value is inside the image
            if 0 < u < width - 1 and 0 < v < height - 1:
                # Applies the u and v value to the x and y positions in the image
                pixel = img.getpixel((u, v))
                red = pixel[0]
                green = pixel[1]
                blue = pixel[2]
                # Sets the new RGB value based upon the kernel
                img.putpixel((int(x), int(y)), (red, green, blue))


def translation():
    # Loops through each pixel in the image
    for x in range(width):
        for y in range(height):
            # Formula for translation
            pixel = img.getpixel((x, y))
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            u = x - 50
            v = y - 150
            # Makes sure that the resulting u/v value is inside the image
            if 0 < u < width - 1 and 0 < v < height - 1:
                # Applies the u and v value to the x and y positions in the image
                # Sets the new RGB value based upon the kernel
                img.putpixel((int(u), int(v)), (red, green, blue))


def mirror():
    # Loops through each pixel in the image
    for x in range(width):
        for y in range(height):
            # Formula for mirror
            u = width - x
            v = y
            # Makes sure that the resulting u/v value is inside the image
            if 0 < u < width and 0 < v < height:
                # Applies the u and v value to the x and y positions in the image
                pixel = img.getpixel((u, v))
                red = pixel[0]
                green = pixel[1]
                blue = pixel[2]
                # Sets the new RGB value based upon the kernel
                img.putpixel((int(x), int(y)), (red, green, blue))


def shear():
    # Loops through each pixel in the image
    for x in range(width):
        for y in range(height):
            # Formula for shear
            u = x - y * 2
            v = y
            # Makes sure that the resulting u/v value is inside the image
            if u < 0:
                u = width - (u % width) - 1
            elif u > width - 1:
                u = width - (u % width) - 1

            if v < 0:
                v = height - (v % height) - 1
            elif v > height - 1:
                v = height - (v % height) - 1
            # Applies the u and v value to the x and y positions in the image
            pixel = img.getpixel((u, v))
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            # Sets the new RGB value based upon the kernel
            img.putpixel((int(x), int(y)), (red, green, blue))


def perspective():
    # Loops through each pixel in the image
    for x in range(width):
        for y in range(height):
            # Formula for perspective
            u = (x / 2) / ((x * - 0.0015) + (y * - 0.0015) + 1)
            v = (y / 2) / ((x * - 0.0015) + (y * - 0.0015) + 1)

            # Makes sure that the resulting u/v value is inside the image
            if u < 0:
                u = width - (u % width) - 1
            elif u > width - 1:
                u = width - (u % width) - 1

            if v < 0:
                v = height - (v % height) - 1
            elif v > height - 1:
                v = height - (v % height) - 1
            # Applies the u and v value to the x and y positions in the image
            pixel = img.getpixel((u, v))
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            # Sets the new RGB value based upon the kernel
            img.putpixel((int(x), int(y)), (red, green, blue))


# rotation()
# img.save("rotation.jpg")  # Saves out a new image

# scale()
# img.save("scale.jpg")  # Saves out a new image

# translation()
# img.save("translation.jpg")  # Saves out a new image

# mirror()
# img.save("mirror.jpg")  # Saves out a new image

# shear()
# img.save("shear.jpg")  # Saves out a new image

perspective()
img.save("perspective.jpg")  # Saves out a new image
