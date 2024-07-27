import math
from itertools import product

# Coordinates of depot and cities
cities = {
    0: (50, 42),  # Depot
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# City groups
groups = [
    [1, 2, 6],  # Group 0
    [3, 7, 8],  # Group 1
    [4, 5, 9]   # Group 2
]

def compute_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible combinations (one city from each group)
combinations = list(product(groups[0], groups[1], groups[2]))

# Initialize variables to find the minimum tour
min_distance = float('inf')
min_tour = []

# Calculate the tour distance for each combination
for combo in combinations:
    # Start at depot, visit selected cities, and return to depot
    tour = [0] + list(combo) + [0]
    # Calculate total distance
    distance = sum(compute_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    # Update minimum if current distance is smaller
    if distance < min_distance:
        min_distance = distance
        min_tour = tour

# Output results
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_distance}")