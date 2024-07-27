import itertools
import math

# Coordinates of the cities
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
    14: (12, 39)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate all pairwise distances
distances = {}
for i in cities:
    for j in cities:
        distances[(i, j)] = euclidean_distance(cities[i], cities[j])

def calculate_tour_cost(tour):
    return sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

# Generate all possible tours that visit exactly 12 cities
min_tour = None
min_cost = float('inf')
for subset in itertools.combinations(range(1, len(cities)), 11):  # Visit 11 other cities
    current_tour = [0] + list(subset) + [0]
    for permuted_tour in itertools.permutations(current_tour[1:-1]):
        full_tour = [0] + list(permuted_tour) + [0]
        tour_cost = calculate_tour_cost(full_tour)
        if tour_cost < min_cost:
            min_tour = full_tour
            min_cost = tour_cost

# Print the output commands to ensure execution
if min_tour is not None and min_cost is not float('inf'):
    print(f"Tour: {min_tour}")
    print(f"Total travel cost: {min_cost}")
else:
    print("No solution found or something went wrong with the calculation.")