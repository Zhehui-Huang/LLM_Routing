import math
from itertools import product

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

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

def calculate_total_distance(tour):
    """Calculate the total travel distance for a given tour."""
    total_distance = distances[0][tour[0]]  # start from depot
    for i in range(len(tour) - 1):
        total_distance += distances[tour[i]][tour[i + 1]]
    total_distance += distances[tour[-1]][0]  # return to depot
    return total_distance

def find_shortest_tour():
    """Find the shortest tour that visits one city from each group."""
    min_tour = None
    min_cost = float('inf')
    
    # Generate all possible tours by picking one city from each group
    for cities_combination in product(*groups):
        tour = [0] + list(cities_combination)  # start from depot
        total_cost = calculate_total_distance(tour)
        if total_cost < min_cost:
            min_cost = total_cost
            min_tour = tour + [0]  # return to depot
    
    return min_cost, min_tour

# Calculate the shortest tour and its cost
min_cost, min_tour = find_shortest_tour()
print("Tour:", min_top)
print("Total travel cost:", main_cost)