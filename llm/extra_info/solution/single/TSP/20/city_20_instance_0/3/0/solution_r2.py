import math

# Coordinates for the cities
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Helper function to calculate the Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Nearest Neighbor heuristic to determine the path
def nearest_neighbor(start_city):
    tour = [start_city]
    total_cost = 0
    current_city = start_city
    remaining_cities = set(cities.keys()) - {start_city}

    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: distance(cities[current_city], cities[x]))
        total_cost += distance(cities[current_city], cities[next_city])
        tour.append(next_city)
        current_city = next_city
        remaining_cities.remove(next_city)

    # Return to the depot city
    total_cost += distance(cities[current_city], cities[start_city])
    tour.append(start_city)
    
    return tour, total_cost

# Finding the shortest path using the Nearest Neighbor heuristic
tour, total_cost = nearest_neighbor(0)

print("Tour:", tour)
print("Total travel cost:", total_cost)