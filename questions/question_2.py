import requests

response = requests.get(
'http://api.openweathermap.org/data/2.5/weather',
    params={
        "q": "Toronto", "units": "metric", "appid": "c7345a6839c51552b824e975a3b068e9"
    }
)

if response.status_code == 200:
    print("Current temperature in Toronto: {}".format(response.json()["main"]["temp"]))
    print("API response status: {}".format(response.status_code))
else:
    print("API response status: {}. An error occurred while retrieving the data".format(response.status_code))

# Output:
# Current temperature in Toronto: 6.41
# API response status: 200
