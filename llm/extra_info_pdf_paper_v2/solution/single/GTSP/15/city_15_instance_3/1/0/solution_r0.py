import math
from itertools import permutations

# City coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Groups of cities
groups = {
    0: [1, 6, 14],
    1: [5, 12, 13],
    2: [7, 10],
    3: [4, 11],
    4: [2, 8],
    5: [3, 9]
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all combinations to choose one city from each group
all_combinations = [(groups[0][i], groups[1][j], groups[2][k], groups[3][l], groups[4][m], groups[5][n]) 
                    for i in range(len(groups[0])) for j in range(len(groups[1]))
                    for k in range(len(groups[2])) for l in range(len(groups[3]))
                    for m in range(len(groups[4])) for n in range(len(groups[5]))]

# Find the shortest tour that visits one city from each group
best_tour = None
min_cost = float('inf')

for comb in all_combinations:
    # Check all permutations of the selected city from each group including return to depot
    for perm in permutations(comb):
        # Construct the tour starting from depot
        tour = [0] + list(perm) + [0]
        # Calculate the tour cost
        cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        # Check if this tour is the shortest found so far
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Print the best tour and the minimal cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)