# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=64)
    active = models.BooleanField(default=True)


class Album(models.Model):
    artist = models.ForeignKey(Artist)
    name = models.CharField(max_length=64)


class Link(models.Model):
    artist = models.ForeignKey(Artist)
    name = models.CharField(max_length=64)
    url = models.URLField(max_length=2083)
