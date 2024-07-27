import math
import random
from itertools import permutations

# Euclidean distance calculator
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Define cities and their coordinates
cities = {
    0: (30, 56),
    1: (53, 42), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95),
    9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Group of cities - only one city from each group to be visited
group_cities = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Simple heuristic implementation
# Find path through one city from each group minimizing path distance
def find_minimal_tour():
    shortest_distance = float('inf')
    best_tour = None
    
    # Try all permutations of selecting one city from each group
    for selection in itertools.product(*group_cities):
        # Check all permutations of selected cities order
        for perm in permutations(selection):
            # Consider path starting and ending at depot
            path = [0] + list(perm) + [0]
            # Calculate the path distance
            tour_distance = sum(distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path) - 1))
            
            if tour_distance < shortest_distance:
                shortest_distance = tour_distance
                best_tour = path
                
    return best_tour, shortest_distance

# Find the shortest tour through the simplified heuristic
tour, total_cost = find_minimal_tour()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")