from itertools import product
from math import sqrt

# City coordinates including the depot
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

# City groups
groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def calculate_total_distance(tour):
    total_distance = euclidean_distance(0, tour[0])  # Depot to first city
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])
    total_distance += euclidean_distance(tour[-1], 0)  # Last city back to depot
    return total_distance

# Generate all combinations of picking one city from each group
all_combinations = product(*groups)

# Find the tour with the minimum travel distance
min_distance = float('inf')
optimal_tour = None

for combination in all_combinations:
    tour = list(combination)
    total_distance = calculate_total_distance(tour)
    if total_distance < min_distance:
        min_distance = total_distance
        optimal_tour = tour

# Format the output
optimal_tour.insert(0, 0)  # Start at the depot
optimal_tour.append(0)  # End at the depot
result = {
    "Tour": optimal_tour,
    "Total travel cost": min_distance
}

print(f"Tour: {result['Tour']}")
print(f"Total travel cost: {result['Total travel cost']:.2f}")