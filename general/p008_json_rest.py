import requests
import json

url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    filtered_data = [item for item in data if not item["completed"]]

    # Example: filter incomplete tasks
    for item in filtered_data:
        print("Pending Task:", item["title"])

    # Save snapshot
    with open("to_dos.json", "w") as f:
        json.dump(filtered_data, f, indent=4)
else:
    print("Api Failed")



