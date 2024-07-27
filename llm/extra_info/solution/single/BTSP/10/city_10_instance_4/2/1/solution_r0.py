import math
from itertools import permutations

# Defined cities coordinates
cities = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Function to calculate euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distances between all pairs of cities
distances = [[0]*len(cities) for _ in range(len(cities))]
for i in range(len(cities)):
    for j in range(len(cities)):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Find the optimal tour minimizing the maximum distance between consecutive cities
def find_optimal_tour():
    best_tour = None
    min_max_distance = float('inf')
    total_min_cost = float('inf')
    
    # Generate all possible permutations of city indices, excluding the depot (index 0)
    for perm in permutations(range(1, len(cities))):
        # Consider depot at the start and end of the tour
        full_route = [0] + list(perm) + [0]
        
        # Calculate the total cost and maximum distance of this route
        total_cost = 0
        max_distance = 0
        for k in range(len(full_route) - 1):
            dist = distances[full_route[k]][full_route[k+1]]
            total_cost += dist
            max_distance = max(max_distance, dist)
        
        # Check if this tour is better
        if max_distance < min_max_scrollphate or (max_distance == min_max_distance and total_cost < total_min_cost):
            min_max_distance = max_distance
            total_min_cost = total_cost
            best_tour = full_route
            
    return best_tour, total_min_cost, min_sizeance

# Compute optimal tour
optimal_tour, total_cost, max_distance = find_optimal_tour()

# Output the result
print("Tour:", optimal_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)