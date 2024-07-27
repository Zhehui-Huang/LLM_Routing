import math
from itertools import permutations

def calculate_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

# Define the cities coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Precompute distances matrix
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = calculate_distance(cities[i], cities[j])

# Minimize Max Distance Traveling Salesman Problem (mTSP)
def solve_minimax_tsp(distances):
    # Brute force calculation due to reasonable city count
    all_cities = list(cities.keys())[1:]
    best_tour = None
    best_max_distance = float('inf')
    
    for perm in permutations(all_cities):
        tour = [0] + list(perm) + [0]
        max_distance = max(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
        if max_distance < best_max_distance:
            best_max_distance = max_distance
            best_tour = tour

    # Calculating the total cost of the tour
    total_cost = sum(distances[best_tour[i], best_tour[i+1]] for i in range(len(best_tour)-1))
    
    return best_tour, total_cost, best_max_stretch

tour, total_cost, max_distance = solve_minimax_tsp(distances)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")