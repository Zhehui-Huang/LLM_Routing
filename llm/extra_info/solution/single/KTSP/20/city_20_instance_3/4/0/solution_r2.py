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

# Generate all combinations of 12 cities from the 19 cities (excluding depot city 0)
combinations_of_cities = combinations([i for i in range(1, 20)], 12)

shortest_tour = None
shortest_distance = float('inf')

for combo in combinations_of_cities:
    # Calculate a tour starting and ending at the depot (city 0)
    # Include the depot to form a potential tour
    potential_tour = [0] + list(combo) + [0]

    # Test all permutations of this tour (excluding the fixed depot start and end)
    for perm in permutations(potential_tour[1:-1]):
        tour = [0] + list(perm) + [0]  # ensure the tour starts and ends at the depot
        distance = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_tour = tour

print("Tour:", shortest_tour)
print("Total travel cost:", shortest_distance)