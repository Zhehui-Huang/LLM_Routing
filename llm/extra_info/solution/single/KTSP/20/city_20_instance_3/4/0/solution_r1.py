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

# Generate all combinations of 12 other cities from the 19 non-depot cities (since one is the depot, city 0)
combinations_of_cities = combinations(list(cities.keys())[1:], 12)

shortest_tour = None
shortest_distance = float('inf')

for combo in combinations_of_cities:
    # Include the depot city (0) to the list for forming complete circuits
    trial_cities = [0] + list(combo)

    # Generate all permutations of the trial_cities
    for perm in permutations(trial_cities):
        # Ensure the tour starts and ends at the depot city 0
        if perm[0] == 0:
            # Form a tour by looping back to the depot
            tour_path = list(perm) + [0]
            
            # Calculate the complete trip distance for this tour path
            trip_distance = sum(euclidean_holder_distance(tour_path[i], tour_path[i + 1]) for i in range(len(tour_path) - 1))
            
            # Check if this tour has a shorter total distance than the current shortest
            if trip_distance < shortest_distance:
                shortest_distance = trip_distance
                shortest_tour = tour_path

print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {shortest_distance}")