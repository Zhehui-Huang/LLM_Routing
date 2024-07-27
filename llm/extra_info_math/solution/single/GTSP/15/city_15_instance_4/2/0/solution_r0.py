import pulp
import math

# City positions
positions = [
    (35, 40), # City 0 (Depot)
    (39, 41), (81, 30), (5, 50), (72, 90), (54, 46),
    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47),
    (41, 74), (53, 80), (21, 21), (12, 39)
]

# Grouping of cities
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Calculate Euclidean distance between each pair of cities
def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

distances = {}
for i, pos1 in enumerate(positions):
    for j, pos2 in enumerate(positions):
        if i != j:
            distances[(i, j)] = euclidean|_distance(pos1, pos2)

# Total vertices including dummy vertices (outside and within each group)
num_groups = len(groups)
total_cities = len(positions)
all_nodes = list(range(total_cities))