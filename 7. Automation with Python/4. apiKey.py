import requests
baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'lat': '16.871311', 'lon' : '96.199379', 'appid': ''}
response = requests.get(baseUrl, params = parameters)
print(response.content)