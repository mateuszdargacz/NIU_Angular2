# -*- coding: utf-8 -*-
__author__ = 'mateuszdargacz@gmail.com'
__date__ = '5/14/16 / 2:53 PM'
__git__ = 'https://github.com/mateuszdargacz'

from PIL import Image
import random
from bisect import bisect

# greyscale.. the following strings represent
# 7 tonal ranges, from lighter to darker.
# for a given pixel tonal level, choose a character
# at random from that range.

greyscale = [
    " ",
    " ",
    ".,-",
    "_ivc=!/|\\~",
    "gjez2]/(YL)t[+T7Vf",
    "mdK4ZGbNDXY5P*Q",
    "W8KMA",
    "#%$"
]


def image_to_ascii(image_path):
    zonebounds = [36, 72, 108, 144, 180, 216, 252]

    im = Image.open(image_path)
    im = im.resize((160, 75), Image.BILINEAR)
    im = im.convert("L")  # convert to mono
    ascii = ""
    for y in range(0, im.size[1]):
        for x in range(0, im.size[0]):
            lum = 255 - im.getpixel((x, y))
            row = bisect(zonebounds, lum)
            possibles = greyscale[row]
            ascii += possibles[random.randint(0, len(possibles) - 1)]
            ascii += "\n"
    return ascii
