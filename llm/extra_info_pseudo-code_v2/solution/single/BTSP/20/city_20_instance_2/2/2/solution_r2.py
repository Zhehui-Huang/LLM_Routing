import math
from itertools import permutations

# Coordinates of each city including the depot city
cities = [
    (3, 26),   # City 0 (Depot)
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

def calculate_distance(city1, city2):
    """ Calculate the Euclidean distance between two points. """
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate distances between each pair of cities
n = len(cities)
distances = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Function to determine the best tour minimizing the maximum distance between consecutive cities
def brute_force_bottleneck_tsp():
    min_bottleneck = float('inf')
    best_tour = None
    
    # Loop through all possible permutations of city visits
    for perm in permutations(range(1, n)):
        # Create tour from the depot, through all permuted cities and back to the depot
        tour = [0] + list(perm) + [0]
        # Determine the maximum distance between consecutive cities in the tour
        max_dist_in_tour = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        
        if max_dist_in_tour < min_bottleneck:
            min_bottleneck = max_dist_in_tour
            best_tour = tour

    # Calculate the total cost of travel for the tour
    total_cost = sum(distances[best_tour[i]][best_tour[i + 1]] for i in range(len(best_tour) - 1))
    return best_tour, total_cost, min_bottleneck

# Obtain the tour, total travel cost, and the maximum distance between any consecutive cities in the tour
tour, total_cost, max_distance = brute_force_bottleneck_tsp()

# Print results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")