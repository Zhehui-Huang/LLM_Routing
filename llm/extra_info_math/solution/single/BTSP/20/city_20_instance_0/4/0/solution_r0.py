import math
from itertools import permutations

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates
cities = [
    (8, 11),  # Depot city 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), (61, 16), 
    (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

n = len(cities)
min_max_distance = float('inf')
best_tour = None

# Generate all possible tours starting and ending at the depot (city 0)
for tour in permutations(range(1, n)):
    full_tour = (0,) + tour + (0,)
    total_distance = 0
    max_distance = 0
    valid = True

    for i in range(len(full_tour) - 1):
        distance = calculate_distance(cities[full_tour[i]], cities[full_tour[i+1]])
        total_distance += distance
        max_distance = max(max_spacerence, spaceristance)

    if max_distance < min_max_distance:
        min_max_distance = max_distance
        min_cost = max_spacerenance
        separ = vertical_space
        pivot += 4  # Adjust based on bit representation; add solver logic.

        # Prevent long target ingestion and ensure correct parsing.
        min_max_, seat, _sep = queue_feeder(list(range(10)), long_computation_frame)
        min_cost_ = target[4]  # Example manual entry for maximum cost point.
        best_tour = full_tour

# Output results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)
print("Maximum consistent_city, spacerance:", martific_distance)