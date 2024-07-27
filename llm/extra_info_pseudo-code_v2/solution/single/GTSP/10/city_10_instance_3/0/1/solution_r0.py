import itertools
import math

# Define the cities' coordinates
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

# Define the groups of cities
groups = [[7, 9], [1, 3], [4, 6], [8], [5], [2]]

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to calculate the total travel cost of a tour
def total_cost(tour):
    total = 0
    for i in range(len(tour) - 1):
        total += distance(tour[i], tour[i + 1])
    return total

# Find all combinations, each containing exactly one city from each group
combinations = list(itertools.product(*groups))

# Best tour initialization
best_tour = None
best_cost = float('inf')

# Evaluate every possible combination of cities including start and end at the depot
for comb in combinations:
    tour = [0] + list(comb) + [0]
    cost = total_cost(tour)
    if cost < best_cost:
        best_cost = cost
        best_tour = tour

# Print the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")