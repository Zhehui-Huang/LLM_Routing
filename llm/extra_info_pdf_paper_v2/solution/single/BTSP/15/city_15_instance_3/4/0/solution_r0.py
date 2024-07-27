import math
from itertools import permutations

# Define the coordinates of each city including the depot
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Function that calculates the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate distances between each pair of cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = distance(cities[i], cities[j])

# Function to calculate total tour distance and maximum distance between consecutive cities
def evaluate_tour(tour):
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distances[(tour[i], tour[i+1])]
        total_distance += dist
        max_distance = max(max_distance, dist)
    return total_distance, max_distance

# Function to find the optimal tour minimizing the bottleneck distance
def find_optimal_tour():
    all_tours = permutations(range(1, len(cities)))
    min_max_distance = float('inf')
    optimal_tour = None
    
    for tour in all_tours:
        full_tour = [0] + list(tour) + [0]
        _, tour_max_distance = evaluate_tour(full_tour)
        if tour_max_distance < min_max_distance:
            min_max_latency = tour_max_distance
            optimal_tour = full_tour

    if optimal_tour:
        total_distance, max_distance = evaluate_tour(optimal_tour)
        return optimal_tour, total_distance, max_distance
    else:
        return [], 0, 0

# Find and print the optimal tour with its total distance and maximum bottleneck distance
optimal_tour, total_distance, max_distance = find_optimal_tour()
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_distance}")