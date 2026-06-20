import requests
import csv
import json

base_url = "https://jsonplaceholder.typicode.com/users"
base_url2 = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(base_url)

data = response.json()

city_name = 0
large_C = None
large_U = None

with open("jsonplaceholderUsers.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "email", "city"])

    writer.writeheader()

    for user in data:
        writer.writerow(
            {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "city": user["address"]["city"],
            }
        )

        city = user["address"]["city"]
        if len(city) > city_name:
            city_name = len(city)
            large_C = city
            large_U = user["name"]

# print(f"User in largest city name is in city: {large_C}, user: {large_U}")


response2 = requests.get(base_url2)

todos = response2.json()

ids = {}
for todo in todos:
    # print(todo["title"])

    ids.setdefault(todo["userId"], []).append(todo)

with open("todos.json", "w") as fi:
    json.dump(ids, fi, indent=2)

stats = {}
for todo in todos:
    uid = todo["userId"]

    stats.setdefault(uid, {"total": 0, "completed": 0})

    stats[uid]["total"] += 1

    if todo["completed"]:
        stats[uid]["completed"] += 1

with open("todos_stats.json", "w") as fileS:
    json.dump(stats, fileS, indent=2)


# Day 2 - Rest Countries

import requests

base_url3 = "https://api.restcountries.com/countries/v5"
# headers = {"Authorization": "Bearer rc_live_35e0adc91c594cbe906c38cd5d943e48"}

response3 = requests.get(base_url3, headers=headers)

# print(response3)
dataCountries = response3.json()
# print(dataCountries)

# with open('restcountries.json', 'w', encoding='utf-8') as f:
#     json.dump(dataCountries, f, indent=2, ensure_ascii=False)

count = 0
region_data = {}
with open("restCountriesData.csv", "w", newline="") as fcsv:
    writer = csv.DictWriter(
        fcsv, fieldnames=["Country", "Capital", "Region", "Population"]
    )
    writer.writeheader()
    for country in dataCountries["data"]["objects"]:
        name = country["names"]["official"]
        capital = country["capitals"][0]["name"] if country["capitals"] else "N/A"
        region = country["region"]
        population = country["population"]
        count += 1
        
        region_data[region] = region_data.get(region, 0) + 1

        writer.writerow(
            {
                "Country": name,
                "Capital": capital,
                "Region": region,
                "Population": population,
            }
        )

print(count)
print(sorted(region_data.items(), key=lambda item: item[1], reverse=True))
# ------------- or 
print("Region      Countries")
print("-" * 25)
for region, count in sorted(
    region_data.items(), key=lambda item: item[1], reverse=True
):
    print(f"{region:<12}{count}")
    
    
with open("top10byPopulation.csv", "w", newline="") as fcsv:
    writer = csv.DictWriter(
        fcsv, fieldnames=["Country", "Capital", "Region", "Population"]
    )
    writer.writeheader()

    for country in sorted(
        dataCountries["data"]["objects"],
        key=lambda item: item["population"],
        reverse=True,
    )[:10]:
        writer.writerow(
            {
                "Country": country["names"]["official"],
                "Capital": (
                    country["capitals"][0]["name"] if country["capitals"] else "N/A"
                ),
                "Region": country["region"],
                "Population": country["population"],
            }
        )
