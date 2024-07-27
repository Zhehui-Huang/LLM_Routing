import math
from itertools import permutations

# City coordinates (city index starting from 0 which is Depot; indexes correspond to positions in the list)
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Heuristic function to generate a feasible tour
def find_bottleneck_tour():
    num_cities = len(cities)
    # Try all city permutations (skipping depot which is always the start/end)
    best_tour = None
    best_max_distance = float('inf')
    best_total_cost = float('inf')

    for perm in permutations(range(1, num_cities)): # Try different permutations
        current_tour = [0] + list(perm) + [0]
        max_distance = 0
        total_distance = 0
        for i in range(len(current_tour) - 1):
            dist = calculate_distance(current_tour[i], current_tour[i+1])
            total_distance += dist
            if dist > max_distance:
                max_distance = dist
        
        if max_distance < best_max_distance:
            best_max_distance = max_distance
            best_total_cost = total_distance
            best_tour = current_tour
        elif max_distance == best_max_distance and total_distance < best_total_cost:
            best_total_cost = total_distance
            best_tour = current_tour

    return best_tour, best_total_cost, best_max_distance

# Execute the heuristic algorithm
tour, total_cost, max_distance = find_bottleneck_tour()

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)