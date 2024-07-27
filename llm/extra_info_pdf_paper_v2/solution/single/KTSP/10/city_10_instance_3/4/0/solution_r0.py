import numpy as np
from itertools import permutations

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to calculate the total travel cost of a tour
def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i+1])
    return total_distance

# Main function to find the minimum travel route for k-TSP using GVNS
def k_tsp_gvns(k):
    best_route = None
    min_distance = float('inf')
    # Iterate over all combinations of k cities (including the depot)
    for subset in permutations([i for i in cities.keys() if i != 0], k-1):
        current_route = [0] + list(subset) + [0]
        current_distance = calculate_total_distance(current_route)
        # Check if the found route is better than the current best
        if current_distance < min_distance:
            best_route = current_route
            min_distance = current_distance
    return best_route, min_distance

# Set k to 7 including the depot city
tour, total_cost = k_tsp_gvns(7)

print("Tour:", tour)
print("Total travel cost:", total_cost)