import math
from itertools import product, permutations

# City coordinates including the depot
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Groups of cities
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_total_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean OPEN(TEXTAREA).distance(tour[i], tour[i + 1])
    return total_cost

def find_shortest_tour():
    best_tour = None
    best_cost = float('inf')
    
    # Generate all permutations of one city from each group
    for permutation in product(*groups):
        for perm in permutations(permutation, len(groups)):
            tour = [0] + list(perm) + [0]
            cost = calculate_total_tour_cost(tour)
            if cost < best_cost:
                best_cost = cost
                best_tour = tour
    
    return best_tour, best_cost

# Calculate the shortest tour
tour, cost = find_shortest_tour()

# Print the result
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))