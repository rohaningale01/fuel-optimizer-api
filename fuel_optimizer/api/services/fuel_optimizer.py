from .fuel_data import get_cheapest_station
from .fuel_data import get_all_data

# Step 1: Split route into 500-mile segments
def split_route(distance):
    stops = []
    current = 0

    while current < distance:
        stops.append(current)
        current += 500

    return stops


# Step 2: Get cheapest fuel stop
def get_fuel_stops(stops):
    df = get_all_data()

    # sort by cheapest price
    df_sorted = df.sort_values(by="Retail Price")

    result = []
    used_cities = set()

    for i in range(len(stops)):
        for _, row in df_sorted.iterrows():
            city = row['City']

            if city not in used_cities:
                used_cities.add(city)

                result.append({
                    "city": city,
                    "price": row['Retail Price']
                })
                break   # move to next stop

    return result


# Step 3: Calculate total fuel cost
def calculate_total_cost(distance, price):
    gallons = distance / 10
    return gallons * price