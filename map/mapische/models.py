from django.contrib.gis.db import models


class Coordinates(models.Model):
    pointer = models.PointField(geography=True)


    def __str__(self):
        return str(self.pointer)
