# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from imagesascii.serializers import GallerySerializer, AsciiImageSerializer

__author__ = 'mateuszdargacz@gmail.com'
__date__ = '5/14/16 / 2:39 PM'
__git__ = 'https://github.com/mateuszdargacz'


class GalleryViewset(viewsets.ModelViewSet):
    serializer_class = GallerySerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = [IsAuthenticated]


class AsciiImageViewset(viewsets.ModelViewSet):
    serializer_class = AsciiImageSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = [IsAuthenticated]
