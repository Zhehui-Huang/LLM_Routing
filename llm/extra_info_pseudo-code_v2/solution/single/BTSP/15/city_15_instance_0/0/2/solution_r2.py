import math
from itertools import permutations

# Define the cities' coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Compute all pairwise distances
n = len(cities)
distances = [[calculate_distance(i, j) for j in range(n)] for i in range(n)]

# Function to find a bottleneck traveling salesman tour
def find_bottleneck_tsp(distances):
    # Initialize variables
    min_max_bottleneck = float('inf')
    best_tour = None
    
    # Try permutations of all cities except the depot (city 0)
    for permutation in permutations(range(1, n)):
        # Include the depot city at the start and the end of the tour
        tour = [0] + list(permutation) + [0]
        max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        
        # Update the best tour if a new smaller maximum distance is found
        if max_distance < min_max_bottleneck:
            min_max_bottleneck = max_distance
            best_tour = (tour, total_cost, max_distance)
    
    return best_tour

# Get the bottleneck tour along with total travel cost and max distance between any two consecutive cities
tour, total_cost, max_distance = find_bottleneck_tsp(distances)

# Printing results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))