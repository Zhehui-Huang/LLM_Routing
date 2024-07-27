import math
from itertools import permutations

# Coordinates of the cities
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def distance(city1, city2):
    (x1, y1), (x2, y2) = cities[city1], cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calculate_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def find_best_tour():
    best_tour, best_cost = None, float('inf')
    for subset in combinations(cities.keys(), 6):
        if 0 in subset:
            for perm in permutations(subset):
                if perm[0] == 0:
                    tour = list(perm) + [0]  # ensure the tour starts and ends at the depot
                    cost = calculate_cost(tour)
                    if cost < best_cost:
                        best_tour, best_cost = tour, cost
    return best_tour, best_cost

# Execute the TSP solution search
best_tour, best_cost = find_best_tour()

# Output
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")