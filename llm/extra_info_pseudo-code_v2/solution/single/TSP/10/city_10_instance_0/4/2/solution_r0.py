import math
from itertools import permutations

# City coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate a stateful nearest neighbor tour
def nearest_neighbor_tour(start=0):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current, city))
        tour.append(next_city)
        current = next_city
        unvisited.remove(current)
    tour.append(start)  # Return to the depot
    return tour

# Calculate the tour's total length
def calculate_tour_length(tour):
    total_length = 0
    for i in range(len(tour) - 1):
        total_length += distance(tour[i], tour[i + 1])
    return total_length

# Solving the TSP
initial_tour = nearest_neighbor_tour()
tour_length = calculate_tour_length(initial_tour)

# Output result
print(f"Tour: {initial_tour}")
print(f"Total travel cost: {tour_length}")