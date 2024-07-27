import math
from itertools import permutations

# Define the list of cities coordinates (ID: Coordinate tuple)
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
    18: (50, 28), 19: (69, 9)
}

# Function to compute the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Permute over all cities except the depot (city 0)
city_indices = list(cities.keys())[1:]  # excluding the depot
all_tours = permutations(city_indices)

# Initialize results
best_tour = None
best_total_cost = float('inf')
best_max_distance = float('inf')

# Test each permutation of cities to find the minimum bottleneck path
for perm in all_tours:
    # Create the full tour path including returning to the depot
    tour = (0,) + perm + (0,)
    
    # Find the tour's total cost and maximum travel distance between consecutive cities
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    max_dist = max(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

    # Check if this tour is better than the best so far
    if max_dist < best_max_distance or (max_dist == best_max_distance and tour_cost < best_total_cost):
        best_max_distance = max_dist
        best_total_cost = tour_cost
        best_tour = tour

# Print the result in the required format
print("Tour:", list(best_tour))
print("Total travel cost:", round(best_total_cost, 2))
print("Maximum distance between consecutive cities:", round(best_max_distance, 2))