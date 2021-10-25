from datetime import date, timedelta
from .models import Images
from dotenv import dotenv_values
import requests


class PictureClient:

    def __init__(self):
        config = dotenv_values()
        self.api_key = config['NASA_API_KEY']

    def upload_data(self, number_of_days=None):
        if number_of_days:
            start_date = date.today() - timedelta(days=number_of_days)
            res = requests.get(
                f"https://api.nasa.gov/planetary/apod?api_key={self.api_key}&start_date={start_date}")
            data = res.json()

            for day_info in data:
                self.__process_category(day_info)

        else:
            res = requests.get(
                f"https://api.nasa.gov/planetary/apod?api_key={self.api_key}")
            data = res.json()
            self.__process_category(data)


    def __process_category(self, day_info):
        if day_info['media_type'] == 'image':
            image = Images()
            image.name = day_info['title']
            image.date = day_info['date']
            image.explanation = day_info['explanation']
            image.get_remote_image(day_info['url'])
            image.save()
