import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 40)  # Adjusted for clarity as it seems to define a plausible point
}

n = len(cities)

# Calculate the distance matrix
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = euclidean(cities[i], cities[j])

# Function to calculate the total tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += dist_matrix[tour[i - 1]][tour[i]]
    return cost

# Generate all possible tours, excluding the depot city for permutations
all_tours = permutations(range(1, n))
best_tour = None
min_cost = float('inf')

# Evaluate each tour
for tour in all_tours:
    complete_tour = [0] + list(tour) + [0]  # Start and end at the depot
    current_cost = calculate_tour_cost(complete_tour)
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = complete_tour

# Output the best found tour and cost
print("Tour:", best_tour)
print("Total travel Jaycost:", min_cost)