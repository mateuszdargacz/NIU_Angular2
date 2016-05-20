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


def image_to_ascii(image_name):
    # image to ascii adopted from Steven Kay's implementation:
    # http://stevendkay.wordpress.com/2009/09/08/generating-ascii-art-from-photographs-in-python/

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

    # using the bisect class to put luminosity values
    # in various ranges.
    # these are the luminosity cut-off points for each
    # of the 7 tonal levels. At the moment, these are 7 bands
    # of even width, but they could be changed to boost
    # contrast or change gamma, for example.

    zonebounds = [36, 72, 108, 144, 180, 216, 252]

    # open image and resize
    # experiment with aspect ratios according to font

    im=Image.open(image_name)
    width, height = im.size
    new_width = 80
    new_height = int((height * new_width) / width)
    im = im.resize((new_width, new_height))
    im = im.convert("L") # convert to mono

    # now, work our way over the pixels

    ascii_img=""
    for y in range(0,im.size[1]):
        for x in range(0,im.size[0]):
            lum=255-im.getpixel((x,y))
            row=bisect(zonebounds,lum)
            possibles=greyscale[row]
            ascii_img=ascii_img+possibles[random.randint(0,len(possibles)-1)]
        ascii_img=ascii_img+"\n"

    return (ascii_img)

