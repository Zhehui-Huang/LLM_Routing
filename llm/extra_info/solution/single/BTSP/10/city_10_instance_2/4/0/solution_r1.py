import math
from itertools import permutations

# City coordinates
cities = [
    (90, 3),  # Depot city
    (11, 17),
    (7, 27),
    (95, 81),
    (41, 54),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29),
    (13, 17)
]

# Function to compute Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Find the tour that minimizes the maximum distance between consecutive cities
def find_best_tour():
    best_max_distance = float('inf')
    best_tour = None
    
    # Generate permutations of the city indices (excluding the depot city, index 0)
    for perm in permutations(range(1, len(cities))):
        # Append the depot city (index 0) to the start and end of the tour
        tour = [0] + list(perm) + [0]
        
        # Calculate the max distance between consecutive cities in this tour permutation
        max_distance = max(
            euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1)
        )
        
        # If the found max distance is better than the current best, update best
        if max_distance < best_max_distance:
            best_max_distance = max_distance
            best_tour = tour
            
    return best_tour, best_max_distance

# Function to compute the total travel cost for a given tour
def calculate_total_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

# Compute the best tour and max distance between consecutive cities
best_tour, best_max_distance = find_best_tour()
total_travel_cost = calculate_total_cost(best_tour)

# Output the results: the tour, the total travel cost, and the maximum distance between consecutive cities
print("Tour:", best_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", best_max_distance)