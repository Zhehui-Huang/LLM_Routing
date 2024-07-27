import itertools
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9), 
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# City groups
groups = [
    [1, 4], [2, 6], [7], [5], [9], [8], [3]
]

# Calculate the distance matrix
n = len(cities)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = calculate_distance(cities[i], cities[j])

# A function to calculate the path cost for a given tour
def path_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distances[tour[i]][tour[i+1]]
    return cost

# Generating all combinations based on selected city in each group
all_combinations = itertools.product(*groups)
best_tour = None
min_cost = float('inf')

# Evaluating each combination
for combination in all_combinations:
    tour = [0] + list(combination) + [0]  # starting and ending at the depot
    cost = path_cost(tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")