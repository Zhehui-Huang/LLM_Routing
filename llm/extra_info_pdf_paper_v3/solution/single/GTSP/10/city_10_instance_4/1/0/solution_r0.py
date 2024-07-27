import math
from itertools import permutations

# City coordinates with depot as the first entry
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Groupings of cities
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Calculate Euclidean distance between two cities
def distance(a, b):
    x1, y1 = cities[a]
    x2, y2 = cities[b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Finding all permutations of one city from each group, representing all possible group visiting orders
all_group_permutations = list(permutations([group[0] for group in groups]))

# Initializing minimum distance large to find the minimum route
min_distance = float('inf')
best_route = []

# Brute force all permutations to find the optimal route involving one city from each group
for perm in all_group_permutations:
    for ordering in permutations(perm):
        # Formulating the route starting and ending at the depot
        route = [0] + list(ordering) + [0]
        # Calculate the total distance of the current order
        total_distance = sum(distance(route[i], route[i+1]) for i in range(len(route)-1))
        # Update minimum distance and best route found
        if total_distance < min_distance:
            min_distance = total_distance
            best_route = route

# Output the required results
print("Tour:", best_route)
print("Total travel cost:", round(min_distance, 2))