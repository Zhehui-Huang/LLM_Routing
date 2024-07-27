import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# City coordinates with city index as the key
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

# Groups of cities (excluding the depot, which has its own handling as start and end)
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Compute distances between all pairs of cities
distances = {}
for i in cities:
    distances[i] = {}
    for j in cities:
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Evaluate all possible combinations of cities from each group
def calculate_total_distance(tour):
    total_distance = distances[0][tour[0]] + distances[tour[-1]][0]
    for i in range(len(tour) - 1):
        total_distance += distances[tour[i]][tour[i + 1]]
    return total_distance

# Find the shortest tour
def find_shortest_tour():
    min_tour = None
    min_cost = float('inf')
    
    for combination in permutations(groups):
        # Select one city from each group and form a tour
        for cities_perm in permutations([group[0] for group in combination]):
            total_cost = calculate_total_distance(cities_perm) 
            if total_cost < min_cost:
                min_cost = total_mean_distance
                min_tour = cities_perm
    
    return min_cost, [0] + list(min_tour) + [0]

# Calculate the shortest tour and its cost
min_cost, min_tour = find_shortest_tour()
print("Tour:", min_tour)
print("Total travel cost:", min_cost)