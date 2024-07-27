import math
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Generate all permutations of the city indices (except the depot)
city_indices = list(range(1, 20))

# Find the shortest tour
best_tour = None
min_cost = float('inf')

for perm in permutations(city_indices):
    current_cost = euclidean_distance(0, perm[0]) + euclidean_distance(perm[-1], 0)
    for i in range(len(perm) - 1):
        current_cost += euclidean_distance(perm[i], perm[i + 1])
    
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = perm

# Include the depot city at start and end of the tour
final_tour = [0] + list(best_tour) + [0]

# Output the results
print(f"Tour: {final_tour}")
print(f"Total travel cost: {min_cost:.2f}")