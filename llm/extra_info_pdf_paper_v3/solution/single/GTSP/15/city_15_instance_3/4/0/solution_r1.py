import math
import itertools

# Define the city coordinates
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
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Function to calculate Euclidean distance
def distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all combinations of choosing one city from each group
group_permutations = list(itertools.product(*groups))

# Function to find the shortest path visiting exactly one city from each group
def find_shortest_path(group_permutations):
    min_cost = float('inf')
    min_path = []

    for group_choice in group_permutations:
        for perm in itertools.permutations(group_choice):
            # Include the depot as the starting and ending point
            path = [0] + list(perm) + [0]
            # Calculate path cost
            cost = sum(distance(path[i], path[i+1]) for i in range(len(path)-1))

            if cost < min_cost:
                min_cost = cost
                min_path = path

    return min_path, min_cost

# Compute the optimal path and cost
optimal_path, optimal_cost = find_shortest_path(group_permutations)

# Output the results
print("Tour:", optimal_path)
print("Total travel cost:", optimal_cost)