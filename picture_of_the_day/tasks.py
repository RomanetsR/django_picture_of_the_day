from celery import shared_task
from .picture_client import PictureClient


@shared_task
def add_image():
    client = PictureClient()
    client.upload_data()
    return True
