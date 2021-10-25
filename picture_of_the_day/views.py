from django.shortcuts import render
from .models import Images
from .picture_client import PictureClient


if Images.objects.first() is None:
    client = PictureClient()
    client.upload_data(14)


def index(request):
    images = Images.objects.all().order_by('-date')
    return render(request, 'picture_of_the_day/index.html', {'images': images})


def show(request, id):
    image = Images.objects.filter(id__exact=id).first()
    return render(request, 'picture_of_the_day/show.html', {'image': image})
