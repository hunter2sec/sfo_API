# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    kind = models.CharField(max_length=255)

    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    LEGENDARY = 3

    RARITY_CHOICES = [
        (COMMON, 'Common'),
        (UNCOMMON, 'Uncommon'),
        (RARE, 'Rare'),
        (LEGENDARY, 'Legendary'),
    ]
    rarity = models.IntegerField(
        choices=RARITY_CHOICES,
        default=UNCOMMON,
    )

    avg_price = models.FloatField()
    max_price = models.FloatField()
    min_price = models.FloatField()