import itertools
import math

# Define a function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Cities' coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Choose k cities, starting with depot 0
k = 13

# Generate all combinations of k-1 cities from 1 to 19 (excluding the depot which is always included)
combinations = itertools.combinations(range(1, len(cities)), k-1)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

# Searching for shortest tour
shortest_tour = None
minimum_distance = float('inf')

for subset in combinations:
    # Form the tour starting and ending at the depot
    current_combination = [0] + list(subset) + [0]

    # Generate all possible tours for this combination
    for permutation in itertools.permutations(current_combination[1:-1]):
        current_tour = [0] + list(permutation) + [0]
        current_distance = calculate_total_roundtrip_distance(current_tour)
        if current_distance < minimum_distance:
            minimum_distance = current_distance
            shortest_tour = current_tour

# Outputting the result
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {minimum_distance:.2f}")