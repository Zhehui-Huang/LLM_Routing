import math
from itertools import chain

# Define the coordinates of each city
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Greedy algorithm to find a reasonable tour minimizing maximum edge distance
def find_tour():
    remaining_cities = set(cities.keys())
    tour = [0]
    remaining_cities.remove(0)
    
    while remaining_cities:
        last_city = tour[-1]
        next_city = min(remaining_cities, key=lambda x: distance(last_city, x))
        tour.append(next_city)
        remaining_cities.remove(next_city)
    
    tour.append(0) # return to the starting point
    return tour

# Calculate the total and maximum distances of a tour
def tour_distances(tour):
    total_distance = 0
    max_distance = 0
    
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i+1])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    
    return total_distance, max_distance

# Get the optimized tour using a heuristic
tour = find_tour()
total_distance, max_distance = tour_distances(tour)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_distance, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_distance, 2)}")