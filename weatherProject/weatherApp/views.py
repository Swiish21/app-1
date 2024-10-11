from django.shortcuts import render

# Create your views here.
import urllib.request
import json


def index (request):
    if request.method == 'POST':
        city = request.POST[çity]
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=953a8e1b9b3de15890807bb788d4602f').read(
            
        )
        list_of_data = json.loads(source)
        data = {
            'city' : city,
            'country_code' : list_of_data['sys']['country'],
            'temp' : list_of_data['main']['temp'],
            'pressure' : list_of_data['main']['pressure'],
            'humidity' : list_of_data['main']['humidity'],
            'description' : list_of_data['weather'][0]['description'],
            'icon' : list_of_data['weather'][0]['icon']
        }
        print(data)
    else:
        data = {}
        return render(request, 'main/index.html', {'city_name' : data})