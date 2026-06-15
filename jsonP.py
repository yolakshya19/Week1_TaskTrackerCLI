import json
from pprint import pprint

with open("european-countries.json", "r") as f:
    data = json.load(f)

pprint(data['countries'], indent=1)

for country in data['countries']:
    if country['eu_member'] == True:
        print(country['name'], country.get('capital'))

    del country['code']
    del country['area_km2']

with open('eu-countries.json', 'w') as f:
    json.dump(data, f, indent=2)
    
    
max_pop = 0
count = None
for country in data["countries"]:
    if country["population"] > max_pop:
        max_pop = country["population"]
        count = country["name"]

print(f"{count} has max population of {max_pop}")


eur_c = 0
for country in data["countries"]:
    if country["currency"] == "EUR":
        eur_c += 1

print(f"{eur_c} countries have EUR as their currency")

eur_p = 0
for country in data["countries"]:
    if country["eu_member"] == True:
        eur_p += country["population"]

print(f"{eur_p} population in eu_member countries")

max_D = 0
maxDC = data["countries"][0]
for country in data["countries"]:
    density = country["population"] * 1.0 / country["area_km2"]
    print(f"{country['name']} has {density:.2f} density")

    if density > max_D:
        maxDC = country
        max_D = density

print(f"most dense country is {maxDC['name']} with a density of {max_D}")

eu_countries = []
for country in data["countries"]:
    if country["eu_member"]:
        eu_countries.append(country)

with open("eu_country.json", "w") as f:
    json.dump(eu_countries, f, indent=2)

currencies = {}
for country in data["countries"]:
    currency = country["currency"]
    currencies.setdefault(currency, []).append(country["name"])

# print(currencies)
with open("currencies.json", "w") as f:
    json.dump(currencies, f, indent=2)


summary = {}
for country in data["countries"]:
    currency = country["currency"]
    summary.setdefault(
        currency,
        {
            "country_count": 0,
            "total_population": 0,
            "largest_country": "",
            "largest_population": 0,
        },
    )

    summary[currency]["country_count"] += 1
    summary[currency]["total_population"] += country["population"]
    if country["population"] > summary[currency]["largest_population"]:
        summary[currency]["largest_population"] = country["population"]
        summary[currency]["largest_country"] = country["name"]

sorted_summary = dict(  # important
    sorted(summary.items(), key=lambda item: item[1]["country_count"], reverse=True)
)

with open("currency_summ.json", "w") as f:
    json.dump(sorted_summary, f, indent=2)
