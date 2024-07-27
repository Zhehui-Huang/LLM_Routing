import math
import itertools

# Input data for cities (city index and coordinates)
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate all distances between cities
distances = {}
for i in cities:
    for j in cities:
        distances[(i, j)] = euclidean_distance(i, j)

# Generate all combinations of 3 cities (excluding the depot), making total 4 cities with the depot
city_indices = list(cities.keys())
city_combinations = itertools.combinations(city_indices[1:], 3)  # (1, 2, 3), ...; excluding depot

# Finding the shortest tour involving exactly 4 cities including depot
min_cost = float('inf')
min_tour = []

for combo in city_combinations:
    # All permutations of the selected cities including depot as starting and ending point
    for perm in itertools.permutations(combo):
        tour = [0] + list(perm) + [0]
        cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
        if cost < min_cost:
            min_cost = cost
            min_tour = tour

# Output
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost:.2f}")