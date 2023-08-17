from flask import Flask,jsonify,request
from flask_cors import CORS
import requests
import requests
import datetime

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "done"

@app.route('/date')
def code():
    time = datetime.datetime.current()
    print(time)
    return time
  

def check_Uv(uv):
    if uv < 2:
        return f"with the given Uv index that is {uv} you might need not apply sunscreen"
    elif uv > 3 and uv< 6:
        return f"Since the UV Index is {uv}, applying sunscreen is recommended to safeguard your skin from moderate sun exposure."
    else:
        return f"Given the high UV Index of {uv}, it's advisable to apply sunscreen and take sun protection measures before heading outdoors to protect your skin from the strong sun"

def check_weather(current_weather_condition):
    if current_weather_condition.lower() == "clear":
        return "Clear skies and sunny weather! Enjoy the outdoors."
    elif current_weather_condition.lower() == "partly cloudy":
        return "It's cloudy today. You might not need sunglasses, but keep an umbrella handy."
    elif current_weather_condition.lower() == "partly_cloudy" or current_weather_condition.lower() == 'overcast':
        return "A mix of clouds and sun. A light jacket might be useful."
    elif current_weather_condition.lower() == "rainy":
        return "Rainy day ahead. Remember your umbrella and raincoat."
    elif current_weather_condition.lower() == "patchy rain possible":
        return "there may be rain so it's better you carry your umbrella"
    elif current_weather_condition.lower() == "snowy":
        return "Snowfall expected. Bundle up and stay warm."
    elif current_weather_condition.lower() == "sunny":
        return "Bright and sunny!"
    elif current_weather_condition.lower() == "windy":
        return "Windy conditions. Secure loose items and be cautious outdoors."
    elif current_weather_condition.lower() == "mist":
        return "due to foggy weather, Drive carefully and use fog lights if necessary."
    elif current_weather_condition.lower() == "hazy":
        return "Hazy conditions. Limit outdoor exposure, especially if you have respiratory issues."
    elif current_weather_condition.lower() == "thunderstorm":
        return "Thunderstorm alert! Stay indoors and avoid electrical appliances."
    elif current_weather_condition.lower() == "hail":
        return "Hail can be dangerous. Park your car in a garage or covered area."
    elif current_weather_condition.lower() == "tornado":
        return "Tornado warning! Seek shelter in a sturdy building or basement."
    elif current_weather_condition.lower() == "hurricane":
        return "Hurricane warning! Follow evacuation orders and stay safe."
    elif current_weather_condition.lower() == "drought":
        return "Drought conditions. Conserve water and follow local water use regulations."
    elif current_weather_condition.lower() == "heatwave":
        return "Heatwave alert! Stay hydrated and avoid strenuous activities outdoors."
    elif current_weather_condition.lower() == "cold_snap":
        return "Cold snap! Dress in warm layers and protect yourself from frostbite."
    else:
        return "Unknown weather condition."


@app.route("/w")
def weather():

    API_KEY = '57fba51795c34dd3b73115524230908'

    # API endpoint and parameters
    base_url = 'http://api.weatherapi.com/v1/current.json'
    
    location = request.args.get('location')
    print("locatoin",location)
    
    params = {
        'key': API_KEY,
        'q': location  
    }

    # Make the API request
    response = requests.get(base_url, params=params)
    print(response.status_code)
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        print("data",data)

        # Extract relevant weather information
        temperature = data['current']['temp_c']
        weather_condition = data['current']['condition']
        uv = data['current']['uv']
        country = data['location']['country']

        uv_status = check_Uv(uv)
        weather_status = check_weather(weather_condition['text'])
        suggestion = 'My forecast suggest that '+uv_status + ' also ' + weather_status
        
        res_data ={
            'temperature':temperature,
            'weather':weather_condition,
            'uv':uv,
            'suggestion': suggestion,
            'country' : country
        }
        print(f"Temperature: {temperature}°C")
        print(f"Weather Condition: {weather_condition}")
    else:
        print("Request failed:", response.status_code)
        res_data = 'error'    
    return res_data

if __name__=='__main__':
    app.run()