# -*- coding: utf-8 -*-
from rest_framework import serializers

from imagesascii.models import AsciiImage, Gallery

__author__ = 'mateuszdargacz@gmail.com'
__date__ = '5/14/16 / 2:39 PM'
__git__ = 'https://github.com/mateuszdargacz'


class AsciiImageSerializer(serializers.ModelSerializer):
    ascii_art = serializers.ReadOnlyField()
    class Meta:
        model = AsciiImage
        fields = ('gallery', 'original_image', 'name', 'ascii_art')


class GallerySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    images = AsciiImageSerializer(many=True)

    class Meta:
        model = Gallery
