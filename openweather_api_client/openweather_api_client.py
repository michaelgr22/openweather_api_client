import requests
import json


class OpenWeatherApiClient:

    def __init__(self, lat, lon, units, appid):
        self.lat = lat
        self.lon = lon
        self.units = units
        self.appid = appid
        self.openweathermap_url = "https://api.openweathermap.org/data/2.5/onecall?"

    def __get_raw_data(self):
        response = requests.get(self.openweathermap_url +
                                "lat=" + self.lat +
                                "&lon=" + self.lon +
                                "&units=" + self.units +
                                "&appid=" + self.appid)

        return response.json()

    def get_weather_for_day(self, days_from_today):
        raw_data = self.__get_raw_data()
        return raw_data['daily'][days_from_today]
