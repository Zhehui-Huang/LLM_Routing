import itertools
import math

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

# City groups
city_groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Precompute all pairwise distances
distances = {}
for city1 in cities:
    for city2 in cities:
        if city1 != city2:
            distances[(city1, city2)] = euclidean_distance(city1, city2)

# Generate all possible tours
min_distance = float('inf')
min_tour = None

for permutation in itertools.product(*city_groups):
    # Adding depot to and from the sequence
    full_tour = [0] + list(permutation) + [0]
    # Calculate the distance for this sequence
    total_distance = 0
    for i in range(len(full_tour) - 1):
        total_distance += distances[(full_tour[i], full_tour[i+1])]
    
    # Compare to find the minimum distance
    if total_distance < min_distance:
        min_distance = total_distance
        min_tour = full_tour

# Print the optimal tour and its total travel cost
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_distance}")