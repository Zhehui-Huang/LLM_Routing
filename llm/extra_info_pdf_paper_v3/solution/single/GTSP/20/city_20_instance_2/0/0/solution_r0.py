import math
from itertools import permutations

# Coordinates of each city, including the depot
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Grouping of cities
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Compute all pairwise distances
distances = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            distances[(i, j)] = euclidean_distance(coordinates[i], coordinates[j])

# Function to find the minimal tour that visits one city from each group
def minimal_gtsp_tour(groups, distances):
    # Evaluate every permutation of selecting one city from each group
    best_tour = None
    best_cost = float('inf')
    
    for selection in permutations([0] + [min(group, key=lambda v: distances[0, v]) for group in groups]):
        current_cost = 0
        current_tour = [0]  # start at the depot
        for i in range(len(selection) - 1):
            current_cost += distances[(selection[i], selection[i+1])]
        current_cost += distances[(selection[-1], 0)]  # return to depot
        if current_cost < best_cost:
            best_tour = list(selection) + [0]  # complete the loop
            best_cost = current_cost

    return best_tour, best_cost

# Get the optimal tour and its cost
tour, total_cost = minimal_gtsp_tour(groups, distances)
print(f'Tour: {tour}')
print(f'Total travel cost: {total_cost}')