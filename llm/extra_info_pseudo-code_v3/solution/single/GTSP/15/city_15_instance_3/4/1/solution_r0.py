import itertools
import math

# Define the city coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Groups of cities
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Distance computation using Euclidean formula
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all combinations of cities such that one city is chosen from each group
all_combinations = list(itertools.product(*groups))

def find_shortest_tour():
    min_distance = float('inf')
    best_tour = None

    # Iterate over every possible tour combination
    for combination in all_combinations:
        # Start and end at the depot (city 0)
        full_tour = [0] + list(combination) + [0]
        current_distance = sum(distance(full_tour[i], full_tour[i + 1]) for i in range(len(full_tour) - 1))

        # If this tour is better, save it
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = full_tour

    return best_tour, min_distance

# Calculate the shortest tour
tour, total_cost = find_shortest_tour()

# Print results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")