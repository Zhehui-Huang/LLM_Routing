import math
from itertools import permutations

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all possible tours starting and ending at the depot (0)
all_tours = permutations([i for i in cities if i != 0])
min_longest_distance = float('inf')
optimal_tour = None
total_min_cost = float('inf')

for tour in all_tours:
    full_tour = [0] + list(tour) + [0]
    max_distance = 0
    total_cost = 0
    for i in range(len(full_tour) - 1):
        dist = euclidean_distance(full_tour[i], full_tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    if max_distance < min_longest_distance:
        min_longest_distance = max_distance
        optimal_tour = full_tour
        total_min_cost = total_cost

# Outputting the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_min_cost}")
print(f"Maximum distance between consecutive cities: {min_longest_distance}")