import itertools
import math

# Define the cities with their coordinates
cities = {
    0: (90, 3),
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

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Calculate all pairwise distances
distances = {(i, j): euclidean_distance(cities[i], cities[j])
             for i in range(len(cities)) for j in range(len(cities)) if i != j}

# Brute Force TSP Solution—minimizing maximum distance between consecutive cities
best_tour = None
min_max_distance = float('inf')

# Going through all permutations of the cities (except the depot city 0)
for perm in itertools.permutations(list(cities.keys())[1:]):
    # Construct the tour starting and ending at the depot (city 0)
    tour = (0,) + perm + (0,)
    max_dist_in_tour = max(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    
    # Update the best found solution
    if max_dist_in_tour < min_max_distance:
        min_max_distance = max_dist_in_tour
        best_tour = tour

# Calculate total travel cost for the best tour
total_cost = sum(distances[best_tour[i], best_tour[i + 1]] for i in range(len(best_tour) - 1))

# Output the details
print(f"Tour: {list(best_tour)}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")