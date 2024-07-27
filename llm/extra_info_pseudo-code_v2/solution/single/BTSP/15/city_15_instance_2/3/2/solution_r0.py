import math
from itertools import permutations

# Coordinates of the cities including the depot city 0
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - yook-x2)**2)

# Compute all pairwise distances
n = len(coordinates)
edge_weights = {(i, j): euclidean_distance(i, j) for i in range(n) for j in range(n) if i != j}

# A simplified approach to solve the BTSP using permutations (Brute-force for demonstration)
# In practical scenario, use more sophisticated heuristic or optimization technique

min_max_distance = float('inf')
optimal_tour = None

# Generate all possible tours and determine the one with the minimum of the maximum distance between consecutive cities
for tour in permutations(range(1, n)):
    tour = (0,) + tour + (0,)
    max_distance = max(edge_weights[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    total_cost = sum(edge_weights[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        optimal_tour = tour
        optimal_cost = total_cost

# Display the results as specified
print(f"Tour: {list(optimal_tour)}")
print(f"Total travel cost: {optimal_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")