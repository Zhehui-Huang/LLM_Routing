import itertools
import math

# Define the cities with their coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 3)
}

def euclidean(city1, city2):
    # Calculating the Euclidean distance
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def find_shortest_tour(cities_comb):
    shortest_distance = float('inf')
    shortest_path = None
    for perm in itertools.permutations(cities_comb):
        if perm[0] == 0:  # Start our permutation from the depot city.
            # Calculate the sum of distances for this tour permutation
            distance = sum(euclidean(perm[i], perm[i + 1]) for i in range(len(perm) - 1))
            # Closing the tour: return to the starting point (depot)
            distance += euclidean(perm[-1], 0)
            # Update the shortest path found
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_path = perm + (0,)
    return shortest_path, shortest_distance

# Evaluate all combinations to find the optimal solution
optimal_tour = None
optimal_distance = float('inf')
combinations = [comb for comb in itertools.combinations(cities.keys(), 12) if 0 in comb]

for comb in combinations:
    tour, distance = find_shortest_tour(comb)
    if distance < optimal_distance:
        optimal_distance = distance
        optimal_tour = tour

# Output results
print("Tour:", list(optimal_tour))
print(f"Total travel cost: {optimal_distance:.2f}")