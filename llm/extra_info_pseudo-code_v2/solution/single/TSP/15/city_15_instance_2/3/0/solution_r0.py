import math
from itertools import permutations

# Define the cities with coordinates
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

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Compute distances matrix
n = len(cities)
distances = [[calculate_distance(i, j) for j in range(n)] for i in range(n)]

# Find a simple initial tour using nearest neighbor heuristic starting and ending at the depot 0
def nearest_neighbor_tour(start):
    unvisited = set(cities.keys())
    tour = [start]
    unvisited.remove(start)
    current_city = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start)  # Returning to depot
    return tour

# Calculate the total cost of a tour
def calculate_tour_cost(tour):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Get an initial simple tour
initial_tour = nearest_neighbor_tour(0)
initial_cost = calculate_tour_cost(initial_tour)

# Output the initial solution
print("Initial Tour:", initial_tour)
print("Initial Total Travel Cost:", round(initial_cost, 2))