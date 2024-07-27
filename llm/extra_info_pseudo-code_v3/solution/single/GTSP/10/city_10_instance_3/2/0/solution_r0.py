import itertools
import math

# City coordinates
coordinates = [
    (84, 67), # Depot city 0
    (74, 40), # City 1
    (71, 13), # City 2
    (74, 82), # City 3
    (97, 28), # City 4
    (0, 31),  # City 5
    (8, 62),  # City 6
    (74, 56), # City 7
    (85, 71), # City 8
    (6, 76)   # City 9
]

# Groups of city indices
city_groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Precompute all possible city groups selection
all_possible_tours = itertools.product(*city_groups)

# Find shortest tour among all possibilities
min_cost = float('inf')
best_tour = []

for tour in all_possible_tours:
    # Add the depot as starting and ending point
    full_tour = [0] + list(tour) + [0]
    cost = sum(distance(full_tour[i], full_tour[i+1]) for i in range(len(full_tour) - 1))
    
    if cost < min_cost:
        min_cost = cost
        best_tour = full_tour

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", min_cost)