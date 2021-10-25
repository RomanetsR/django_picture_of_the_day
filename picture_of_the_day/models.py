from django.db import models
from django.core.files import File
from urllib import request
import os


class Images(models.Model):
    name = models.CharField('img_name', max_length=255, default=None)
    date = models.DateField('date')
    explanation = models.TextField('explanation')
    url = models.ImageField(upload_to='static/img')

    def get_remote_image(self, url):
        result = request.urlretrieve(url)
        self.url.save(
            os.path.basename(url),
            File(open(result[0], 'rb'))
        )

    def __str__(self):
        return self.name
