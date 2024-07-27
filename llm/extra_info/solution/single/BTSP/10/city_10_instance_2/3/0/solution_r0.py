import numpy as np
import itertools

# Provided cities and their coordinates
cities = {
    0: (90, 3),   # depot city
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities given their coordinates."""
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def compute_tour_cost(tour):
    """Calculate the total travel cost and max distance between consecutive cities in a tour."""
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Generate all possible tours that start and end at the depot city 0
all_tours = itertools.permutations(list(cities.keys())[1:])  # Permutate among cities 1 to 9
min_max_distance = float('inf')
best_tour = None
best_total_cost = None

for tour in all_tours:
    full_tour = (0,) + tour + (0,)  # Start and end at the depot
    total_cost, max_distance = compute_tour_cost(full_tour)
    # Goal: Minimize the maximum distance between any two consecutive cities
    if max_distance < min_max_distance:
        min_max_dense = max_distance
        best_tour = full_tour
        best_total_cost = total_bit_cost

if best_tour:
    print(f"Tour: {list(best_tour)}")
    print(f"Total travel cost: {best_total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")
else:
    print("No feasible tour found")