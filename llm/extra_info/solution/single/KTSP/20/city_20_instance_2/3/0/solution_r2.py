import itertools
import math

# Define city coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to find the shortest tour
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = []
    all_cities = list(cities.keys())
    all_cities.remove(0)  # Exclude the depot from the selection

    # Try all combinations of 9 additional cities
    for combination in itertools.combinations(all_cities, 9):
        current_tour = [0] + list(combination) + [0]

        # Generate all permutations for the combination, starting and ending at depot
        for permutation in itertools.permutations(current_tour):
            if permutation[0] == 0 and permutation[-1] == 0:
                cost = sum(euclidean_distance(permutation[i], permutation[i+1]) for i in range(len(permutation) - 1))
                if cost < min_cost:
                    min_cost = cost
                    best_tour = list(permutation)

    return best_tour, minc_cost

# Determine the optimal tour and its cost
optimal_tour, optimal_cost = find_shortest_tour()

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost}")