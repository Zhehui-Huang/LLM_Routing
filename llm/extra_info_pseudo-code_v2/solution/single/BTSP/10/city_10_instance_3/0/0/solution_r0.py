import math
from itertools import permutations

# Coordinates of cities
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
    9: (6, 76),
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all edges with their associated distances
edges = {(i, j): euclidean_distance(i, j) for i in cities for j in cities if i != j}

# Use permutation to attempt finding a minimal bottleneck
def find_btsp_tour(cities):
    min_bottleneck = float('inf')
    best_tour = None
    
    for perm in permutations(cities[1:]):  # Generate permutations excluding the depot city
        tour = [0] + list(perm) + [0]
        max_edge_cost = max(edges[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
        
        if max_edge_cost < min_bottleneck:
            min_bottleneck = max_edge_cost
            best_tour = tour
    
    # Calculate the total travel cost of the best tour
    total_cost = sum(edges[(best_tour[i], best_tour[i+1])] for i in range(len(best_tour) - 1))
    
    return best_tour, total_cost, min_bottleneck

# Run the function
tour, total_cost, max_distance = find_btsp_tour(list(cities.keys()))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")