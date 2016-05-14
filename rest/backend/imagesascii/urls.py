# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from imagesascii.views import AsciiImageViewset, GalleryViewset

__author__ = 'mateuszdargacz@gmail.com'
__date__ = '5/14/16 / 2:40 PM'
__git__ = 'https://github.com/mateuszdargacz'

router = SimpleRouter()

router.register(r'images', AsciiImageViewset, base_name='images')
router.register(r'galleries', GalleryViewset, base_name='gallery')

urlpatterns = [
    url(r'^', include(router.urls)),

]
