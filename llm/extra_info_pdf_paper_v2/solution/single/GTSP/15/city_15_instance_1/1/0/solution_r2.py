import math
import itertools

# Given cities and their coordinates
positions = {
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

# Groups of cities that the robot needs to visit one city from each group
city_groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Distance calculation using Euclidean distance
def calc_distance(p1, p2):
    return math.sqrt((positions[p1][0] - positions[p2][0])**2 + (positions[p1][1] - positions[p2][1])**2)

# Compute all permutations of selecting one city from each group
all_combinations = list(itertools.product(*city_groups))

# Find the shortest path from depot to one city from each group and back to depot
min_distance = float('inf')
best_tour = None

for cities in all_combinations:
    # Include the depot city at the start and the end of the route for each permutation
    cities = [0] + list(cities) + [0]
    # Calculate the total travel cost for this permutation
    total_distance = sum(calc_distance(cities[i], cities[i + 1]) for i in range(len(cities) - 1))
    # Check if this permutation gives a shorter route
    if total_distance < min_distance:
        min_distance = total_distance
        best_tour = cities

# Output the best tour and the total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")