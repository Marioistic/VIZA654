# ================================================================
# Garvin Beltz
# 10/25/2021
# VIZA 654 - Digital Image
# Project 5 - Basic Convolution Filters
#
# This program will apply 3 filters to a photo. Filters used are
# a blur filter, a emboss filter, and a dilation/erosion filter.
# To save run time, be sure to comment out 2 of the output
# sections under the functions, and only run 1 at a time.

# To switch between dilation and erosion you just have to change
# the max to min or min to max at the bottom of the 3rd function.
# =================================================================

from PIL import Image
import numpy as np

img = Image.open("base.jpg")
data = np.asarray(img)  # Convert the image into an array

# Array is in the form: [width, height, color channels] = [w, h, 3]
width = data.shape[0]
height = data.shape[1]

# Get new array - [width, height, (R, G, B)]
blurArray = np.zeros([width, height, 3], dtype=np.uint8)  # Array is created filled with zeros
embossArray = np.zeros([width, height, 3], dtype=np.uint8)  # Array is created filled with zeros
dilationArray = np.zeros([width, height, 3], dtype=np.uint8)  # Array is created filled with zeros


def blur_filter():

    # Creates the kernel used for filtering
    kernel = 10
    w = kernel * kernel

    # Loops through each pixel in the image
    for x in range(width):
        for y in range(height):

            # Variable initialization
            blurArray[x, y] = 0
            red = 0
            green = 0
            blue = 0

            # Loops through every position surrounding the pixel
            for i in range(kernel):
                for j in range(kernel):
                    u = x + i - int(kernel / 2)
                    v = y + j - int(kernel / 2)

                    # Makes sure that the resulting u/v value is inside the image
                    if u < 0:
                        u = width - (u % width) - 1
                    elif u > width - 1:
                        u = width - (u % width) - 1

                    if v < 0:
                        v = height - (v % height) - 1
                    elif v > height - 1:
                        v = height - (v % height) - 1

                    # Sets the new RGB value based upon the kernel
                    red += data[u, v, 0] / w
                    green += data[u, v, 1] / w
                    blue += data[u, v, 2] / w
            # Assigns new RGB value to output array
            blurArray[x, y] = [red, green, blue]


def emboss_filter():

    # Creates a 3x3 array for the x and y emboss kernels
    xKernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    yKernel = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

    # Loops through each pixel in the image
    for x in range(width):
        for y in range(height):

            # Variable initialization
            embossArray[x, y] = 0
            red = 0
            green = 0
            blue = 0

            # Loops through every position surrounding the pixel
            for i in range(3):
                for j in range(3):
                    u = x + i - 1
                    v = y + j - 1

                    # Makes sure that the resulting u/v value is inside the image
                    if u < 0:
                        u = width - (u % width) - 1
                    elif u > width - 1:
                        u = width - (u % width) - 1

                    if v < 0:
                        v = height - (v % height) - 1
                    elif v > height - 1:
                        v = height - (v % height) - 1

                    # Calculates the new x and y position for each RGB value
                    resultx = (xKernel[i][j]*data[u, v, 0], xKernel[i][j]*data[u, v, 1], xKernel[i][j]*data[u, v, 2])
                    resulty = (yKernel[i][j]*data[u, v, 0], yKernel[i][j]*data[u, v, 1], yKernel[i][j]*data[u, v, 2])

                    # Assigns new RGB value
                    red += ((resultx[0] + resulty[0]) + 255) / 18
                    green += ((resultx[1] + resulty[1]) + 255) / 18
                    blue += ((resultx[2] + resulty[2]) + 255) / 18

            # Assign new values to output array
            embossArray[x, y] = [int(red), int(green), int(blue)]


def dilation_filter():

    # Creates the kernel used for filtering
    kernel = 15

    # Loops through each pixel in the image
    for x in range(width):
        for y in range(height):

            # Variable initialization
            dilationArray[x, y] = data[x, y]
            red = 0
            green = 0
            blue = 0

            # Loops through every position surrounding the pixel
            for i in range(kernel):
                for j in range(kernel):
                    u = x + i - int(kernel / 2)
                    v = y + j - int(kernel / 2)

                    # Makes sure that the resulting u/v value is inside the image
                    if u < 0:
                        u = width - (u % width) - 1
                    elif u > width - 1:
                        u = width - (u % width) - 1

                    if v < 0:
                        v = height - (v % height) - 1
                    elif v > height - 1:
                        v = height - (v % height) - 1

                    # Calculates the max or min value of each color (Swap max with min or vice versa as needed)
                    red = max(data[u, v, 0], red)
                    green = max(data[u, v, 1], green)
                    blue = max(data[u, v, 2], blue)

            # Outputs new values to output array
            dilationArray[x, y] = [red, green, blue]

# ==========================================
# Runs the Blur Filter and outputs image
# ==========================================
# blur_filter()
# blurImg = Image.fromarray(blurArray)
# blurImg.save("blur.jpg")

# ==========================================
# Runs Emboss Filter and outputs image
# ==========================================
# emboss_filter()
# embossImg = Image.fromarray(embossArray)
# embossImg.save("emboss.jpg")

# ===========================================
# Runs Dilation Filter and outputs image
# ===========================================
dilation_filter()
dilationImg = Image.fromarray(dilationArray)
dilationImg.save("dilation.jpg")
