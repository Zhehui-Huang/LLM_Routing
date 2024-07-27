import math
import itertools

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate distance matrix
def calculate_distance_matrix():
    matrix_size = len(cities)
    distance_matrix = {}
    for i in cities:
        distance_matrix[i] = {}
        for j in cities:
            distance_matrix[i][j] = euclidean_distance(i, j)
    return distance_matrix

# Generate all combinations of cities including city 0
def generate_city_combinations():
    return [tuple(sorted([0] + list(comb))) for comb in itertools.combinations(cities.keys() - {0}, 7)]

# Compute the total travel cost of a given tour
def tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Trying to find the best permutation of cities
def find_best_tour(city_combination, distance_matrix):
    best_tour = None
    best_cost = float('inf')
    for perm in itertools.permutations(city_combination):
        current_tour = list(perm) + [perm[0]]
        current_cost = tour_cost(current_tour, distance_matrix)
        if current_cost < best_cost:
            best_tour = current_tour
            best_cost = current_cost
    return best_tour, best_cost

# Main execution
distance_matrix = calculate_distance_matrix()
combinations = generate_city_combinations()
best_overall_tour = None
best_overall_cost = float('inf')

for combo in combinations:
    best_tour, cost = find_best_tour(combo, distance_matrix)
    if cost < best_overall_cost:
        best_overall_tour = best_tour
        best_overall_cost = cost

# Output
print(f'Tour: {best_overall_tour}')
print(f'Total travel cost: {best_overall_cost}')