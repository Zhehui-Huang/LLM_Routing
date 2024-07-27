import math
import itertools
from sys import float_info

# Define the cities with their coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1),
}

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    dx = city1[0] - city2[0]
    dy = city1[1] - city2[1]
    return math.sqrt(dx * dx + dy * dy)

# Generate all distances between cities
def all_distances(cities):
    num_cities = len(cities)
    dist = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist[i][j] = calc_distance(cities[i], cities[j])
            else:
                dist[i][j] = float('inf')  # Distance from a city to itself is infinite    
    return dist

# Generate an approximate tour using a nearest neighbor heuristic
def heuristic_nearest_neighbor(distances):
    N = len(distances)
    unvisited = set(range(1, N))
    tour = [0]
    current = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current][city])
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)

    tour.append(0)  # return to the start
    return tour

# Generate costs and tour information
def tour_costs(tour, distances):
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return total_cost, max_distance

# Run the nearest neighbor heuristic to find a tour
distances = all_distances(cities)
tour = heuristic_nearest_neighbor(distances)
total_cost, max_distance = tour_costs(tour, distances)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")