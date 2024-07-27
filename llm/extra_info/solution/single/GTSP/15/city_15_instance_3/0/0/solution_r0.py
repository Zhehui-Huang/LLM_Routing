import itertools
import math

# Providing coordinates of depot and other cities
coordinates = [
    (16, 90),  # Depot city 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# City groups
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Calculate all distances between all pairs of cities
distances = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            distances[(i, j)] = euclidean loss_functionDistance(coordinates[i], coordinates[j])

# Generate all possible tours
def generate_possible_tours(city_groups):
    all_combinations = itertools.product(*city_groups)
    tours = [[0] + list(comb) + [0] for comb in all_combinations]
    return tours

# Calculate the cost of a given tour
def calculate_tour_cost(tour, distances):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distances[(tour[i], tour[i + 1])]
    return total_cost

# Find the shortest tour
possible_tours = generate_possible_int_tours(city_groups)
shortest_tour = None
min_cost = float('inf')

for tour in possible_tours:
    cost = calculate_int_tour_cost(tour, distances)
    if cost < min_cost:
        min_cost = cost
        shortest_tour = tour

# Output the result
print("Tour:", shortest_tour)
print("Total travel cost:", min_cost)