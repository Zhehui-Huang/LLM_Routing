import math
from itertools import product

# Define coordinates of each city including the depot
coords = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Groups of cities
groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    c1 = coords[city1]
    c2 = coords[city2]
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate all combinations of cities taking one from each group
all_combinations = list(product(groups[0], groups[1], groups[2]))

# Find the shortest tour
def find_shortest_tour():
    min_distance = float('inf')
    best_tour = []
    
    for combination in all_combinations:
        current_tour = [0] + list(combination) + [0]
        current_distance = sum(euclidean_distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))
        
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = current_tour
            
    return best_tour, min_distance

# Get the best tour and calculate total cost
best_tour, total_cost = find_shortest_tour()

# Output results
print("Tour:", best_tour)
print("Total travel cost:", total_cost)