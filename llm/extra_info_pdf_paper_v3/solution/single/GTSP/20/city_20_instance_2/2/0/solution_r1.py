import numpy as np
from itertools import product

# Define the positions of cities
positions = [
    (3, 26),   # Depot
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

# Define groups
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

def euclidean_distance(city1, city2):
    return np.sqrt((positions[city1][0] - positions[city2][0])**2 + (positions[city1][1] - positions[city2][1])**2)

# Generate all possible combinations to visit one city from each group
all_possible_tours = []
for combo in product(*groups): 
    all_possible_tours.append((0,) + combo + (0,)) # Add depot at the start and end

# Function to calculate the total travel cost of a tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

# Evaluate all possible tours to find the one with the minimum travel cost
min_cost = float('inf')
best_tour = None
for tour in all_possible_tours:
    cost = calculate_tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output results
print(f"Tour: {list(best_tour)}")
print(f"Total travel cost: {min_cost:.2f}")