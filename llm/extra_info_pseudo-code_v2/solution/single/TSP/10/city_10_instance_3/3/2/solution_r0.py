import math
from itertools import permutations

# Cities' coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate the distance matrix
n = len(cities)
dist_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = distance(cities[i], cities[j])

# Find the shortest path using permutations (brute-force)
min_cost = float('inf')
best_tour = None

for perm in permutations(range(1, n)):  # permutations of city indices except the depot
    cost = dist_matrix[0][perm[0]]  # start from the depot
    for i in range(len(perm)-1):
        cost += dist_matrix[perm[i]][perm[i+1]]
    cost += dist_matrix[perm[-1]][0]  # return to the depot

    if cost < min_cost:
        min_cost = cost
        best_tour = [0] + list(perm) + [0]

# Output result
print("Tour:", best_tour)
print("Total travel cost:", min_cost)