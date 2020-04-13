# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from django.db import models

# Create your models here.


class Image(models.Model):
    img = models.ImageField(upload_to='Images/files', blank=True)
    img_url = models.URLField(blank=True, default='')

    def save(self, *args, **kwargs):
        if self.img_url:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.img_url).read())
            img_temp.flush()
            self.img_url = ''
            self.img.save(f"image_{self.pk}", File(img_temp))
            super(Image, self).save(*args, **kwargs)
        else:
            super(Image, self).save(*args, **kwargs)