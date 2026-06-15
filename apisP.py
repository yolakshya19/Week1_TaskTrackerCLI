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
                'id': user['id'],
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

print(f"User in largest city name is in city: {large_C}, user: {large_U}")



response2 = requests.get(base_url2)

todos = response2.json()

ids={}
for todo in todos:
    print(todo['title'])

    ids.setdefault(todo['userId'], []).append(todo)
    
with open('todos.json', 'w') as fi:
    json.dump(ids, fi, indent=2)
    
stats = {}
for todo in todos:
    uid = todo['userId']
    
    stats.setdefault(uid, {
        'total': 0,
        'completed': 0
    })
    
    stats[uid]['total'] += 1
    
    if todo['completed']:
        stats[uid]['completed'] +=1
        
with open('todos_stats.json', 'w') as fileS:
    json.dump(stats, fileS, indent=2)