import math
from itertools import permutations

# City coordinates
cities = {
    0: (53, 68),  # depot
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

# Groups of cities
groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.hypot(cities[city1][0] - cities[city2][0], cities[city1][1] - cities[city2][1])

# Generate all combinations of cities taking one city from each group
def generate_city_combinations():
    from itertools import product
    return list(product(groups[0], groups[1], groups[2], groups[3]))

# Calculate the total tour cost given a sequence of cities, starting and ending at the depot
def calculate_tour_cost(tour):
    total_cost = euclidean_distance(0, tour[0])  # From depot to first city
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(tour[i - 1], tour[i])
    total_cost += euclidean_distance(tour[-1], 0)  # From last city back to depot
    return total_cost

# Find the shortest tour using a naive permutation approach over all combinations
def find_shortest_tour():
    best_tour = None
    min_cost = float('inf')
    for combo in generate_city_combinations():
        for permutation in permutations(combo):
            cost = calculate_tour_cost(permutation)
            if cost < min_cost:
                min_cost = cost
                best_tour = permutation
    return best_tour, min_cost

# Solve the problem
best_tour, min_cost = find_shortest_tour()

# Format the output: Tour starting and ending at depot (city 0)
formatted_tour = [0] + list(best_tour) + [0]

print("Tour:", formatted_tour)
print("Total travel cost:", round(min_cost, 2))