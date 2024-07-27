import itertools
import math

# Cities coordinates
cities = [
    (50, 42),  # Depot city 0
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

# City groups
groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all permutations of one city from each group
possible_tours = itertools.product(*groups)
best_tour = None
min_cost = float('inf')

# Evaluate each possible tour
for tour in possible_tours:
    # Include the depot city at start and end
    full_tour = [0] + list(tour) + [0]
    total_distance = 0
    
    # Calculate the cost for the current tour
    for i in range(len(full_tour) - 1):
        total_distance += distance(full_tour[i], full_tour[i + 1])
    
    # Check if the current tour is the shortest one
    if total_distance < min_cost:
        min_cost = total_distance
        best_tour = full_tour

# Output the best tour and the total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")