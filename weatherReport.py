import requests,json

def getting_report(name,apiKey = "ENTER YOUR API KEY"):
    baseUrl = "https://api.openweathermap.org/data/2.5/weather?q="
    complete_base_url = baseUrl+name+"&appid="+apiKey
    response = requests.get(complete_base_url)
    data = response.json()

    if data["cod"]==200 and "main" in data:
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]-273.15
        feels_like = data["main"]["feels_like"]-273.15
        pressure = data["main"]["humidity"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
 
        return country,temperature,feels_like,pressure,humidity,wind_speed
    else:
        return "Unable to Fetch data!! Please Try Again"

    




def main():
    try:
        place = input("City Name : ")
        country,temperature,feels_like,pressure,humidity,wind_speed = getting_report(place)
        print(f"COUNTRY : {country}\nTEMPERATURE : {round(temperature,2)}\nFEELS LIKE : {round(feels_like,2)}\nPRESSURE : {pressure}\nHUMIDITY : {humidity}\nWIND SPEED : {wind_speed}")

    except Exception as e:
        print(str(e))
    

if __name__ == "__main__":
    main()
