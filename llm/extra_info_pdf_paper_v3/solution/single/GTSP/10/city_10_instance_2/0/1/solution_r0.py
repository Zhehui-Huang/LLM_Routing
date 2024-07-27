import itertools
import math

# Define city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Define groups
groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate possible tours
def generate_all_possibilities():
    all_combinations = list(itertools.product(*groups))
    all_possible_tours = []
    for combination in all_combinations:
        perms = itertools.permutations(combination)
        for perm in perms:
            all_possible_tours.append([0] + list(perm) + [0])
    return all_possible_tours

# Calculate tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i+1])
    return total_cost

# Evaluate all possible tours and select the one with the minimum cost
def find_optimal_tour():
    all_possible_tours = generate_all_possibilities()
    min_cost = float('inf')
    best_tour = None
    for tour in all_possible_tours:
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    return best_tour, min_cost

# Find the optimal tour and its cost
optimal_tour, optimal_cost = find_optimal_tour()

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")