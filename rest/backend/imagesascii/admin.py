# -*- coding: utf-8 -*-
from django.contrib import admin
from imagesascii.models import AsciiImage, Gallery
__author__ = 'mateuszdargacz@gmail.com'
__date__ = '5/14/16 / 3:01 PM'
__git__ = 'https://github.com/mateuszdargacz'



@admin.register(AsciiImage)
class ASCIIAdmin(admin.ModelAdmin):
    pass


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass



