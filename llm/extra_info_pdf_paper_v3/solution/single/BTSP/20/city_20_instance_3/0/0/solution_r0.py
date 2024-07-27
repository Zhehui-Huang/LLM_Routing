import math
from itertools import permutations

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61),
    4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77),
    8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate Euclidean distance between two cities
def dist(u, v):
    return math.sqrt((cities[u][0] - cities[v][0]) ** 2 + (cities[u][1] - cities[v][1]) ** 2)

# Generating a simple heuristic tour using nearest neighbor algorithm
def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys())
    tour = [start_city]
    current_city = start_city
    unvisited.remove(start_city)

    while unvisited:
        next_city = min(unvisited, key=lambda city: dist(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # Return to the starting point
    return tour

# Calculate total cost and the maximum distance between any two consecutive cities in the tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0

    for i in range(len(tour) - 1):
        d = dist(tour[i], tour[i + 1])
        total_cost += d
        if d > max_distance:
            max_distance = d

    return total_cost, max_distance

# Generate tour using the nearest neighbor heuristic and evaluate it
start_city = 0
tour = nearest_neighbor_tour(start_city)
total_cost, max_distance = evaluate_tour(tour)

# Display results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")