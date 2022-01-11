# ================================================================
# Garvin Beltz
# 10/18/2021
# VIZA 654 - Digital Image
# Project 4B - Hue Replacement

# This program will replace the Hue values of 1 image
# with another. This is done by converting 2 images of the same
# width and height from RGB into HSV, setting the hue values
# of the 1st image with the hue values of the 2nd image, and
# then converting the 1st image back to RGB and writing it out.
#
# Note: Depending on the size of the image, this program may
# take some time to run.
# Note: The images MUST be exactly the same size or you will get
# an "out of index" error. Resize in Photoshop if needed!
# =================================================================

from PIL import Image

# ==========================================================
# Converts RGB to HSV (Taken from Python Colorsys module)
# ==========================================================


def rgb_to_hsv(r, g, b):
    maxc = max(r, g, b)
    minc = min(r, g, b)
    v = maxc
    if minc == maxc:
        return 0.0, 0.0, v
    s = (maxc-minc) / maxc
    rc = (maxc-r) / (maxc-minc)
    gc = (maxc-g) / (maxc-minc)
    bc = (maxc-b) / (maxc-minc)
    if r == maxc:
        h = bc-gc
    elif g == maxc:
        h = 2.0+rc-bc
    else:
        h = 4.0+gc-rc
    h = (h/6.0) % 1.0
    return h, s, v


# ==========================================================
# Converts HSV to RGB (Taken from Python Colorsys module)
# ==========================================================
def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return v, v, v
    i = int(h*6.0)  # XXX assume int() truncates!
    f = (h*6.0) - i
    p = v*(1.0 - s)
    q = v*(1.0 - s*f)
    t = v*(1.0 - s*(1.0-f))
    i = i % 6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q


# ====================
# Hue Replacement
# ====================
base = Image.open("base.JPG")
basePixel = base.load()  # Load in image data and then find width and height
Width, Height = base.size

grad = Image.open("gradient.JPG")
gradPixel = grad.load()  # Load in image data and then find width and height

for x in range(Width):
    for y in range(Height):
        # Getting the RGB pixel value
        baseColor = base.getpixel((x, y))
        gradColor = grad.getpixel((x, y))
        # Convert RGB values to HSV
        baseConvertHSV = rgb_to_hsv(baseColor[0], baseColor[1], baseColor[2])
        gradConvertHSV = rgb_to_hsv(gradColor[0], gradColor[1], gradColor[2])
        # Replace hue value and convert back to RGB
        newRGB = hsv_to_rgb(gradConvertHSV[0], baseConvertHSV[1], baseConvertHSV[2])
        base.putpixel((x, y), (int(newRGB[0]), int(newRGB[1]), int(newRGB[2])))

base.save("newImage.jpg")  # Saves out a new image
