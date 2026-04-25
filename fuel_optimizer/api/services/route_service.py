import requests

API_KEY = "YOUR_API_KEY"

def get_route(start, end):
    url = "https://api.openrouteservice.org/v2/directions/driving-car"

    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "coordinates": [start, end]
    }

    response = requests.post(url, json=body, headers=headers)
    data = response.json()

    print(data)  # debug

    if "routes" not in data:
        return {"error": data}

    distance = data['routes'][0]['summary']['distance'] / 1609

    return {
        "distance": distance,
        "geometry": data['routes'][0]['geometry']
    }
