import random
import math
from itertools import permutations

# Coordinates of the depot and the cities
cities = {
    0: (26, 60),  # Depot
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

# Groups of cities
groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

# Calculate Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Brute force approach to solve the problem
def find_shortest_tour(groups, cities):
    best_cost = float('inf')
    best_tour = None
    
    # Generate all permutations of one city from each group
    for group_permutation in permutations([random.choice(group) for group in groups]):
        perm_with_depot = [0] + list(group_permutation) + [0]
        
        # Calculate tour cost
        current_cost = 0
        for i in range(len(perm_with_depot) - 1):
            current_cost += distance(cities[perm_with_depot[i]], cities[perm_with_depot[i + 1]])
        
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = perm_with_depot
    
    return best_tour, best_cost

# Find the shortest tour
tour, total_cost = find_shortest_tour(groups, cities)

# Output result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")