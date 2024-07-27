import math
from itertools import permutations

# Coordinates of the cities
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city2][0] - cities[city1][0])**2 + (cities[city2][1] - cities[city1][1])**2)

# Compute all distances between cities
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean_distance(i, j)

# Heuristic TSP approach using permutations (valid for small datasets)
def find_shortest_tour():
    # Consider all permutations of city indices except for the initial city 0
    min_cost = float('inf')
    best_tour = None
    for perm in permutations(range(1, num_cities)):
        # Calculate the total travel cost for this permutation
        cost = distances[0][perm[0]] + sum(distances[perm[i]][perm[i+1]] for i in range(num_cities - 2)) + distances[perm[-1]][0]
        if cost < min_cost:
            min_cost = cost
            best_tour = [0] + list(perm) + [0]
    return best_tour, min_cost

# Compute the shortest tour using the heuristic approach
tour, total_cost = find_shortgether cities excluding the depot city
print("Tour:", tour)
print("Total travel cost:", total_cost)