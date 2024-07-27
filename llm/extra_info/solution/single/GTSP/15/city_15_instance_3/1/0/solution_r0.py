from itertools import product
import math

# Data for cities (index, x-coord, y-coord)
cities = [
    (0, 16, 90),   # Depot [0]
    (1, 43, 99),   # Group 0 [1]
    (2, 80, 21),   # Group 4 [1]
    (3, 86, 92),   # Group 5 [1]
    (4, 54, 93),   # Group 3 [0]
    (5, 34, 73),   # Group 1 [0]
    (6, 6, 61),    # Group 0 [2]
    (7, 86, 69),   # Group 2 [0]
    (8, 30, 50),   # Group 4 [2]
    (9, 35, 73),   # Group 5 [2]
    (10, 42, 64),  # Group 2 [1]
    (11, 64, 30),  # Group 3 [1]
    (12, 70, 95),  # Group 1 [1]
    (13, 29, 64),  # Group 1 [2]
    (14, 32, 79)   # Group 0 [3]
]

# Define city groups
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[1] - city2[1]) ** 2 + (city1[2] - city2[2]) ** 2)

# Calculate all possible tours and their costs
min_cost = float('inf')
best_tour = []

for combination in product(*city_groups):
    # Start at the depot, go through the combination of cities and return to the depot
    tour = [0] + list(combination) + [0]
    
    # Calculate the cost of this tour
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if this tour is better
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")