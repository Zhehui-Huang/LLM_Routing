import math
from itertools import combinations

# City coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Calculate distance matrix
n = len(cities)
dist = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            dist[i][j] = distance(i, j)

# Search for the shortest tour visiting exactly 4 cities (including the depot)
min_distance = float('inf')
best_tour = []

# Consider all combinations of 3 cities other than the depot
for combo in combinations(range(1, n), 3):
    current_route = [0] + list(combo) + [0]
    # Calculate total distance for the route 0 -> city1 -> city2 -> city3 -> 0
    current_distance = sum(dist[current_route[i]][current_route[i+1]] for i in range(len(current_route)-1))
    if current_distance < min_distance:
        min_distance = current_distance
        best_tour = current_route

# Output the best tour and its distance
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")