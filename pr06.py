# ================================================================
# Garvin Beltz
# 11/01/2021
# VIZA 654 - Digital Image
# Project 6 - Filtering with Non-stationary Kernels
#
# This program will apply a motion blur filter or a
# dilation/erosion filter using a kernel created
# from a 2nd image. The kernel is determined by the
# red value of each pixel of the filter image.

# To switch between dilation and erosion you just have to change
# the max to min or min to max at the bottom of the 2nd function.
# =================================================================

from PIL import Image
import numpy as np
import math

img = Image.open("base.jpg")
data = np.asarray(img)  # Convert the image into an array

fil = Image.open("filter.jpeg")
filData = np.asarray(fil)

# Array is in the form: [width, height, color channels] = [w, h, 3]
width = data.shape[0]
height = data.shape[1]

# Get new array - [width, height, (R, G, B)]
blurArray = np.zeros([width, height, 3], dtype=np.uint8)  # Array is created filled with zeros
dilationArray = np.zeros([width, height, 3], dtype=np.uint8)  # Array is created filled with zeros


def blur_filter():
    # Loops through each pixel in the image
    for x in range(width):
        for y in range(height):

            # Variable initialization
            blurArray[x, y] = 0
            red = 0
            green = 0
            blue = 0

            # Creates the kernel shape used for filtering
            kernel = 10
            weight = [[0] * kernel] * kernel
            m = kernel // 2  # Truncates decimal
            sum = 0

            # Calculates the sum of all kernel values
            for i in range(m):
                for j in range(m):
                    theta = filData[x, y, 0]
                    # Make sure to convert to radians
                    sin = math.sin(math.radians(theta))
                    cos = math.cos(math.radians(theta))

                    L = -sin * (i - m / 2) + cos * (j - m / 2)
                    weight[i][j] = math.exp(-abs(L) / m)
                    sum += weight[i][j]

            # Finds the normalized weight values
            for i in range(m):
                for j in range(m):
                    normWeight = weight[i][j] / sum

            # Loops through every position surrounding the pixel
            for i in range(m):
                for j in range(m):

                    u = x + i - int(m / 2)
                    v = y + j - int(m / 2)

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
                    red += data[u, v, 0] * normWeight
                    green += data[u, v, 1] * normWeight
                    blue += data[u, v, 2] * normWeight
            # Assigns new RGB value to output array
            blurArray[x, y] = [red, green, blue]


def dilation_filter():
    # Loops through each pixel in the image
    for x in range(width):
        for y in range(height):

            # Determines filter value used to create kernel based on R value
            filter = filData[x, y, 0]

            # Variable initialization
            dilationArray[x, y] = data[x, y]
            red = 0
            green = 0
            blue = 0

            # Determines kernel size based upon color of filter image
            if 0 <= filter <= 85:
                kernel = 10
            elif 85 < filter <= 170:
                kernel = 15
            elif x > 170:
                kernel = 20

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
blur_filter()
blurImg = Image.fromarray(blurArray)
blurImg.save("blur.jpg")

# =====================================================
# Runs the Dilation/Erosion Filter and outputs image
# =====================================================
# dilation_filter()
# dilationImg = Image.fromarray(dilationArray)
# dilationImg.save("dilation.jpg")
