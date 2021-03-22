# OpenWeatherApiClient

Python Package which uses the free Api from https://openweathermap.org/ to get the weather forecast of a specific location.

**How to use:**

    import openweather_api_client as wc
    
*set coordinates, unit and your apikey:*

    lat = "37.7749"
    lon = "-122.4194"
    units = "metric"
    appid = apikey
    
    weather_client = wc.OpenWeatherApiClient(lat,lon,units,appid)

*Available units:*

> Temperature is available in Fahrenheit, Celsius and Kelvin units.
> 
> Wind speed is available in miles/hour and meter/sec.
> 
> -   For temperature in Fahrenheit and wind speed in miles/hour, use  `units=imperial`
> -   For temperature in Celsius and wind speed in meter/sec, use  `units=metric`

**Current Functions:**

*Get daily data for a specific day:*

    weather_client.get_weather_for_day(0)

0 = today, 
1 = tomorrow, 
2 = day after tomorrow, 
..., 
5

*Output:*

    {'dt': 1616443200, 'sunrise': 1616422173, 'sunset': 1616466192, 'temp': {'day': 12.86, 'min': 8.33, 'max': 13.62, 'night': 10.1, 'eve': 11.76, 'morn': 8.33}, 'feels_like': {'day': 9.09, 'night':
    3.71, 'eve': 6.09, 'morn': 5.41}, 'pressure': 1023, 'humidity': 60, 'dew_point': 5.29, 'wind_speed': 3.86, 'wind_deg': 306, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': 73, 'pop': 0, 'uvi': 5.45}






