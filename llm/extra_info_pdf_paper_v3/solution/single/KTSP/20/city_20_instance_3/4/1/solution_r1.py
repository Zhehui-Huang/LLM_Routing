import math
import random

# Define the cities coordinates
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

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Apply a simple heuristic to construct an initial good enough tour
def initial_tour(start_city, num_cities):
    available_cities = list(cities.keys())
    available_cities.remove(start_city)
    random.shuffle(available_cities)
    tour = [start_city]
    current_city = start_city
    
    while len(tour) < num_cities:
        # we try to find the nearest city to the current city which has not been visited yet
        next_city = min(available_cities, key=lambda x: euclidean_distance(current_city, x))
        available_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    
    tour.append(start_city)  # return to the starting city
    return tour

# Calculate the travel cost of the tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(tour[i-1], tour[i])
    return total_cost

# Construct an initial tour visiting exactly 13 cities
selected_tour = initial_tour(0, 13)

# Calculate the cost of the tour
tour_cost = calculate_tour_cost(selected_tour)

# Output the results
print("Tour:", selected_tour)
print("Total travel cost:", tour_cost)