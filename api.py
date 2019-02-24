import configparser
import requests
import sys
 
def get_ip():
    url = 'http://ipinfo.io/json'
    response = requests.get(url)
    data = response.json()

    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']
    return city
def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']
 
def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, api_key)
    r = requests.get(url)
    return r.json()
 
def main():
    if len(sys.argv) == 2:
        location = sys.argv[1]
        api_key = get_api_key()
        weather = get_weather(api_key, location)
        print(str(weather['main']['temp']) + "C")
        if weather['main']['temp'] < -5:
            print("you will die if you walk outside" + " and there may be " +str (weather['weather'][0]['main']))
        else:
            print("you will live if you walk outside"+" and there may be " +str (weather['weather'][0]['main']))
    else:
        location = get_ip()
        api_key = get_api_key()
        weather = get_weather(api_key, location)
        print(str(weather['main']['temp']) + "C")
        if weather['main']['temp'] < -5:
            print("you will die if you walk outside" + " and there may be " +str (weather['weather'][0]['main']))
        else:
            print("you will live if you walk outside"+" and there may be " +str (weather['weather'][0]['main']))
if __name__ == '__main__':
    main()