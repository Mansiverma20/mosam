from django.shortcuts import render
import requests

def home(request):
    try:
        context = {}
        if request.method == "POST":
            city = request.POST['city']
            key = '9a78977e8dad1665207a10c9a1c99b28'
            api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

            response = requests.get(api)
            if response.status_code == 200:
                data = response.json()
                temperature_kelvin = data["main"]["temp"]  # Use 'data' not 'weather_data'
                temperature_celsius = round(temperature_kelvin - 273.15, 2)
                context = {
                    'city': city,
                    'temperature_kelvin': temperature_kelvin,
                    'temperature': temperature_celsius,
                    "description": data["weather"][0]["description"],
                    "main": data["weather"][0]["main"],
                    "icon": data["weather"][0]["icon"],
                }
            return render(request, 'index.html', context)
        else:
            return render(request, 'index.html')
    except:
        return render(request, 'error.html')
