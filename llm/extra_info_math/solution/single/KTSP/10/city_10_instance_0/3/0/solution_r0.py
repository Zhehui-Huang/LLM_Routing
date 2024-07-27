import itertools
import math

# City coordinates
cities = {
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

def calculate_distance(coord1, coord2):
    # Euclidean distance between two points (x1, y1) and (x2, y2)
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Generating all combinations of 3 cities (excluding the depot city 0)
combinations = list(itertools.combinations(range(1, 10), 3))

# Find the optimal tour
min_cost = float('inf')
best_tour = None

for combo in combinations:
    # Generate the tour starting and ending at the depot city 0
    current_tour = [0] + list(combo) + [0]
    
    # Calculate the cost of this tour
    current_cost = 0
    for i in range(len(current_tour) - 1):
        current_cost += calculate_distance(cities[current_tour[i]], cities[current_tour[i+1]])
    
    # Update the minimum cost and the best tour found
    if current_cost < min_fast:
        min_cost = current_cost
        best_tour = current_tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)