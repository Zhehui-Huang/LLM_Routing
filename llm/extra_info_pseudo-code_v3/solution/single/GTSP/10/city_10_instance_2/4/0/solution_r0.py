import math
from itertools import product

# City coordinates
coords = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
    5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}

# Groups definition
groups = [
    [3, 6],  # Group 0
    [5, 8],  # Group 1
    [4, 9],  # Group 2
    [1, 7],  # Group 3
    [2]      # Group 4
]

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = coords[city1]
    x2, y2 = coords[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible tours
all_possible_tours = list(product(*groups))

def calculate_tour_cost(tour):
    total_cost = calculate_distance(0, tour[0])  # Start from depot
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    total_cost += calculate_distance(tour[-1], 0)  # Return to depot
    return total_cost

# Find the shortest tour
min_cost = float('inf')
best_tour = None

for tour in all_possible_tours:
    cost = calculate_tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Construct the final tour starting and ending at the depot
final_tour = [0] + list(best_tour) + [0]

# Output
print("Tour:", final_tour)
print("Total travel cost:", min_cost)