import math
from itertools import permutations

# Coordinates of cities including the depot city (index 0)
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Groups of city indices
groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16],
    [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 
                     + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def find_shortest_tour():
    """Find the shortest possible tour visiting one city from each group."""
    min_distance = float('inf')
    best_tour = []

    # Generate all possible permutations of selecting exactly one city from each group
    for selection in permutations([min(g) for g in groups]):
        # Prepending and appending the depot city (0)
        tour = [0] + list(selection) + [0]  # example: [0, 4, 6, 9, 2, 1, 8, 0]
        cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if cost < min_distance:
            min_distance = cost
            best_tour = tour
    
    return best_tour, min_distance

# Execute the function and compute results
tour, total_cost = find_shortest_tour()

# Print outputs expected in the specified format
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))