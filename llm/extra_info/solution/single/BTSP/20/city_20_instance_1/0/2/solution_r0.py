import math

# City coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initialize the tour starting at the depot
current_city = 0
remaining_cities = set(cities.keys()) - {current_city}
tour = [current_city]
max_distance = 0
total_cost = 0

def find_next_city(current_city, remaining_cities):
    # Find the next city to minimize the max distance between consecutive cities
    min_next_city = None
    min_next_distance = float('inf')
    for next_city in remaining_cities:
        distance = euclidean_distance(current_city, next_city)
        if distance < min_next_distance:
            min_next_distance = distance
            min_next_city = next_city
    return min_next_city, min_next_distance

while remaining_cities:
    next_city, next_distance = find_next_city(current_city, remaining_cities)
    tour.append(next_city)
    max_distance = max(max_distance, next_distance)
    total_cost += next_distance
    current_city = next_city
    remaining_cities.remove(current_city)

# Close the tour by returning to the depot
return_to_depot_distance = euclidean_distance(current_city, 0)
tour.append(0)
total_cost += return_to_depot_distance
max_distance = max(max_distance, return_to_depot_distance)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)