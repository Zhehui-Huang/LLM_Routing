import math
from itertools import permutations, product

# Coords of each city, including the depot
coords = [
    (29, 51), # Depot
    (49, 20),
    (79, 69),
    (17, 20),
    (18, 61),
    (40, 57),
    (57, 30),
    (36, 12),
    (93, 43),
    (17, 36),
    (4, 60),
    (78, 82),
    (83, 96),
    (60, 50),
    (98, 1)
]

# City groups
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Calculate Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2)

# Compute all distances
distances = [[distance(i, j) for j in range(len(coords))] for i in range(len(coords))]

# Heuristic function to solve the problem
def find_shortest_GTSP_tour():
    min_cost = float('inf')
    shortest_tour = None
    
    # Iterate over all permutations of one city from each group
    all_combinations = list(product(*groups))
    for combination in all_combinations:
        current_permutations = permutations(combination)
        for perm in current_permutations:
            # Calculate tour cost for the chosen cities
            tour = [0] + list(perm) + [0]
            cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
            
            # Update the shortest tour and minimum cost
            if cost < min_cost:
                min_cost = cost
                shortest_tour = tour
    
    return shortest_tour, min_cost

# Find the shortest tour and its cost
shortest_tour, min_cost = find_shortest_GTSP_tour()

# Output the results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {min_cost}")