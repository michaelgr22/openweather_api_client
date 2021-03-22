from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'get weather data via the free API of https://openweathermap.org/'
LONG_DESCRIPTION = 'A package that uses the free API of https://openweathermap.org/ to get weather data'

# Setting up
setup(
    name="openweather_api_client",
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=['openweather_api_client'],
    install_requires=['requests'],
)
