import numpy as np
import math

# Define coordinates for each city
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Assign cities to robots - simple splitting, other algorithms could be more optimal
city_keys = list(cities.keys())[1:]  # Excludes the depot city 0
city_group_1 = city_keys[:len(city_keys)//2]
city_group_2 = city_keys[len(city_keys)//2:]

# Starting with depot in each route
routes = {
    0: [0] + city_group_1 + [0],
    1: [0] + city_group_2 + [0]
}

# Find tours using a simple greedy algorithm for each group.
def find_tour(cities_group):
    tour = [0]
    current_city = 0
    unvisited = cities_group.copy()
    
    while unvisited:
        # Find nearest unvisited city
        next_city = min(unvisited, key=lambda x: distance(current_city, x))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    # Return to depot after visiting all assigned cities
    tour.append(0)
    return tour

# Calculate the cost of each tour
def calculate_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Form tours and calculate their costs
total_travel_cost = 0
for robot_id in routes.keys():
    tour = find_tour(routes[robot_id][1:-1])
    cost = calculate_cost(tour)
    total_travel_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robotid} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")