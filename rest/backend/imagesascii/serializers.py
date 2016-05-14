# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer, HiddenField, CurrentUserDefault

from imagesascii.models import AsciiImage, Gallery

__author__ = 'mateuszdargacz@gmail.com'
__date__ = '5/14/16 / 2:39 PM'
__git__ = 'https://github.com/mateuszdargacz'


class AsciiImageSerializer(ModelSerializer):
    class Meta:
        model = AsciiImage
        fields = ('gallery', 'original_image', 'name')


class GallerySerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())
    images = AsciiImageSerializer(many=True)

    class Meta:
        model = Gallery
