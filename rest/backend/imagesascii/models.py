# -*- coding: utf-8 -*-
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
    name = models.CharField(max_length=128)
    original_image = models.ImageField(upload_to='images/')
    ascii_art = models.TextField(blank=True, null=True)
    gallery = models.ForeignKey(Gallery)

    def save(self, **kwargs):
        self.ascii_art = image_to_ascii(self.original_image.path)
        super(AsciiImage, self).save(**kwargs)
