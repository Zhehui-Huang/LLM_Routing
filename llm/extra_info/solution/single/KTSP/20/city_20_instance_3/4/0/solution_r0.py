from itertools import combinations, permutations
import math

cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Generate all combinations of 12 additional cities from the 19 cities (excluding depot city 0)
combinations_of_cities = combinations([i for i in range(1, 20)], 12)

shortest_tour = None
shortest_distance = float('inf')

for combo in combinations_of_towns:
    # Always include the depot
    current_combination = [0] + list(combo)

    # Generate all permutations of the combination to find the shortest path
    for perm in permutations(current_combination):
        if perm[0] == 0:  # Ensure tour starts at the depot
            trip_distance = sum(euclidean_distance(perm[i], perm[i + 1]) for i in range(len(perm) - 1))
            trip_distance += euclidean_distance(perm[-1], perm[0])  # Return to the depot
            
            if trip_distance < shortest_distance:
                shortest_distance = trip_distance
                shortest_tour = list(perm) + [0]  # ensure the tour ends at the depot

print("Tour:", shortest_tour)
print("Total travel cost:", shortest_distance)