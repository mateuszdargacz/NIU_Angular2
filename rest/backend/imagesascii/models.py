# -*- coding: utf-8 -*-
import pyfiglet as pyfiglet

from django.db import models

from imagesascii.convert import image_to_ascii

__author__ = 'mateuszdargacz@gmail.com'
__date__ = '5/14/16 / 2:39 PM'
__git__ = 'https://github.com/mateuszdargacz'


class Gallery(models.Model):
    name = models.CharField(max_length=128)
    desc = models.CharField(max_length=256)

    user = models.ForeignKey('users.User', related_name='images')


class AsciiImage(models.Model):
    IMAGE_CHOICE = 'i'
    TEXT_CHOICE = 't'
    CHOICES = (
        (IMAGE_CHOICE, 'Image'),
        (TEXT_CHOICE, 'Text'),
    )
    fonts = pyfiglet.FigletFont.getFonts()
    FONT_CHOICES = zip(list(map(str, range(len(fonts)))), fonts)

    # fields
    name = models.CharField(max_length=128)
    name_or_image = models.CharField(max_length=2, choices=CHOICES)
    original_image = models.ImageField(upload_to='images/', null=True, blank=True)
    font = models.CharField(max_length=128, null=True, blank=True, choices=FONT_CHOICES)
    gallery = models.ForeignKey(Gallery, related_name='images')

    @property
    def ascii_art(self):
        if self.name_or_image == self.IMAGE_CHOICE:
            ascii_art = image_to_ascii(self.original_image.path)
        else:
            ascii_art = self.text_to_ascii()

        return ascii_art

    def text_to_ascii(self):
        return pyfiglet.figlet_format(self.name, self.fonts[int(self.font)])

