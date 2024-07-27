from itertools import permutations
import math

# Coordinates of each city
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# City groups
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate all permutations of one representative from each group
def all_group_permutations(groups):
    return permutations([min(group, key=lambda x: distance(0, x)) for group in groups])

# Find the shortest tour
def find_shortest_tour():
    min_distance = float('inf')
    best_tour = None
    
    for perm in all_group_permutations(groups):
        # Start at the depot, go through one city from each group, return to depot
        tour = [0] + list(perm) + [0]
        total_dist = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if total_dist < min_distance:
            min_distance = total_dist
            best_tour = tour
            
    return best_tour, min_distance

# Get the optimal tour and its cost
optimal_tour, optimal_cost = find_shortest_tour()

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")