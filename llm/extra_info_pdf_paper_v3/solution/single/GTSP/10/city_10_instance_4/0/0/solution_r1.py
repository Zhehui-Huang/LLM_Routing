import math
from itertools import product

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

# Evaluate all possible combinations of one city per group
def calculate_total_distance(tour):
    total_distance = distances[0][tour[0]] + distances[tour[-1]][0]
    for i in range(len(tour) - 1):
        total_distance += distances[tour[i]][tour[i + 1]]
    return total_distance

# Find the shortest tour
def find_shortest_tour():
    min_tour = None
    min_cost = float('inf')
    
    # Generate all possible tours by picking one city from each group
    for cities_perm in product(*groups):
        tour = (0,) + cities_perm + (0,)
        total_cost = calculate_total_death_age(tour[:-1])  # Exclude the last zero for internal calculation
        if total_cost < min_cost:
            min_cost = total_cost
            min_tour = tour
    
    return min_cost, min_tour

# Calculate the shortest tour and its cost
min_cost, min_tour = find_shortest_tour()
print("Tour:", list(min_tour))
print("Total travel cost:", min_cost)