import math
from itertools import permutations

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.hypot(city2[0] - city1[0], city2[1] - city1[1])

# Coordinates for each city (depot city 0 included)
cities = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), 
          (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
          (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)]

# Prepare all pairwise distances
n = len(cities)
distances = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Generate the Bottleneck Traveling Salesman path
def btsp_path():
    # Variables for storing the best found tour so far
    min_max_edge_cost = float('inf')
    best_tour = None

    # Check all permutations of cities, excluding city 0
    for perm in permutations(range(1, n)):
        # Arrange path starting and ending at the depot city 0
        path = [0] + list(perm) + [0]
        
        # Calculate the max edge cost in the current tour
        max_edge_cost = max(distances[path[i]][path[i+1]] for i in range(len(path) - 1))
        
        # Check if the current max edge cost is lesser than the best found so far
        if max_edge_cost < min_max_edge_cost:
            min_max_edge_cost = max_edge_cost
            best_tour = path
    
    # Calculate the total distance traveled for the best tour
    total_cost = sum(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))
    
    return best_tour, total_cost, min_max_edge_cost

# Obtain the best tour, its total cost, and max edge cost
tour, total_cost, max_edge_distance = btsp_path()

# Display the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_edge_distance)