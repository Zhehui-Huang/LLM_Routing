import math
from itertools import permutations

# City coordinates
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

# City groups
groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Function to calculate Euclidean Distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Retrieve all possible visiting plans, picking one city from each group
def all_possible_plans():
    group_choices = []
    for group in groups.values():
        group_choices.append(group)
    return list(permutations([item for sublist in group_choices for item in sublist], 4))

# Calculate the travel cost for a given single tour
def tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(tour[i - 1], tour[i])
    return total_cost

# Generate and evaluate all potential tours that visit one city from each group
def find_optimal_tour():
    best_tour = None
    best_cost = float('inf')
    for plan in all_possible_plans():
        for group_permutation in permutations(plan):
            current_tour = [0] + list(group_permutation) + [0]
            current_cost = tour_cost(current_tour)
            if current_cost < best_cost:
                best_tour = current_tour
                best_cost = current_cost
    return best_tour, best_cost

# Compute the optimal tour and its cost
optimal_tour, optimal_cost = find_optional_tour()

# Output result
print("Tour:", optimal_tour)
print(f"Total travel cost: {optimal_cost:.2f}")