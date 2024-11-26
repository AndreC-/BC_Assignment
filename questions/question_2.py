import requests

response = requests.get(
'http://api.openweathermap.org/data/2.5/weather',
    params={
        "q": "Toronto", "units": "metric", "APPID": "c7345a6839c51552b824e975a3b068e9"
    }
)

assert 200 == response.status_code
print(response.json()["main"]["temp"])
print(response.status_code)

# Output
# 5.19
# 200
