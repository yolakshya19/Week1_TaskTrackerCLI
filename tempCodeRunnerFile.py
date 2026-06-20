
import requests

base_url3 = "https://api.restcountries.com/countries/v5"
headers = {"Authorization": "Bearer rc_live_35e0adc91c594cbe906c38cd5d943e48"}

response3 = requests.get(base_url3, headers=headers)

print(response3)
dataCountries = response3.json()
print(len(dataCountries))