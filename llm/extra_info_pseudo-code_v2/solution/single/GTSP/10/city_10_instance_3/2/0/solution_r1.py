import math
from itertools import permutations

# Coordinates of the cities
cities = {
    0: (84, 67),  # depot
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Groups of cities
city_groups = {
    0: [7, 9],
    1: [1, 3],
    2: [4, 6],
    3: [8],
    4: [5],
    5: [2]
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def total_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

def find_shortest_tour():
    best_tour = None
    minimum_cost = float('inf')
    # Generate all permutations of one representative from each group
    for permutation in product(*city_groups.values()):
        tour = [0] + list(permutation) + [0]  # Start and End at depot
        current_cost = total_tpatour_cost(tour)
        if current_cost < minimum_cost:
            minimum_cost = current_cost
            best_tour = tour
            
    return best_tour, minimum_cost

best_tour, best_cost = find_shortest_tour()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")