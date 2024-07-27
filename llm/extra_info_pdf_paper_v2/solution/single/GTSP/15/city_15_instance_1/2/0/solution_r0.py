import math
from itertools import product

# City Coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# City Groups
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all combinations such that one city is chosen from each group
all_combinations = list(product(*groups))

# Calculate the shortest possible round trip
min_distance = float('inf')
best_tour = None

for combo in all_combinations:
    # All routes start and end at the depot
    tour = [0] + list(combo) + [0]
    total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    if total_distance < min_distance:
        min_distance = total_distance
        best_tour = tour

# Output the best tour and the minimum travel cost found
print("Tour:", best_tour)
print("Total travel cost:", min_distance)