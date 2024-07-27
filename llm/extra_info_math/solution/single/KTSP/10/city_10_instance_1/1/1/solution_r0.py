import math
from itertools import combinations, permutations

# Coordinates of the cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate the Euclidean distance between any two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Find the shortest tour that starts and ends at depot (0)
def find_shortest_tour(cities):
    min_distance = float('inf')
    best_tour = None
    for selection in combinations(cities.keys() - {0}, 4):  # Choose 4 cities, excluding the depot
        current_cities = [0] + list(selection)
        for perm in permutations(current_cities[1:]):
            tour = [0] + list(perm) + [0]
            cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            if cost < min_distance:
                min_distance = cost
                best_tour = tour
    return best_tour, min_distance

# Solve the problem
tour, total_cost = find_shortest_tour(cities)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)