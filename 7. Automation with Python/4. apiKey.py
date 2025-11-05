import requests
baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'lat': '16.871311', 'lon' : '96.199379', 'appid': '09cf540c9793fe97520c2bdbc81340ca'}
response = requests.get(baseUrl, params = parameters)
print(response.content)