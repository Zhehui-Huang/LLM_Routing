import math
from itertools import permutations

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

cities = {
    0: (26, 60),
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

# Calculate distances between each pair of cities.
N = len(cities)
distances = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1])

# We need to find the route that minimizes the maximum distance between consecutive cities.
def find_minimax_tour():
    best_tour = None
    lowest_max_distance = float('inf')
    total_cost = 0
    
    for perm in permutations(range(1, N)):
        perm = (0,) + perm + (0,)
        max_distance = 0
        cost = 0
        for i in range(1, len(perm)):
            dist = distances[perm[i-1]][perm[i]]
            cost += dist
            if dist > max_distance:
                max_distance = dist
        if max_distance < lowest_max_distance:
            lowest_max_distance = max_distance
            best_tour = perm
            total_cost = cost

    return best_tour, total_cost, lowest_max_distance

# Use the algorithm (brute-force for demonstration due to convenience)
tour, total_cost, max_distance = find_minimax_tour()

print(f"Tour: {list(tour)}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")