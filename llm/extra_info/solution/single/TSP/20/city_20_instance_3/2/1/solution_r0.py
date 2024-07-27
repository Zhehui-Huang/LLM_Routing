import math

# Define the cities' coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def nearest_neighbor(start_city):
    unvisited = set(cities.keys())
    current_city = start_city
    tour = [current_city]
    total_cost = 0

    while unvisited:
        unvisited.remove(current_city)
        if unvisited:
            next_city = min(unvisited, key=lambda city: euclidean_distance(current_city, city))
            total_cost += euclidean_distance(current_city, next_city)
            tour.append(next_city)
            current_city = next_city

    # Returning to the start city
    total_cost += euclidean_distance(current_city, start_city)
    tour.append(start_city)
    
    return tour, total_cost

# Find the tour starting and ending at the depot city 0
tour, total_cost = nearest_neighbor(0)

print("Tour:", tour)
print("Total travel cost:", total_cost)