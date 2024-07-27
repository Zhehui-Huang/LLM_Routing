import math
import itertools

# City coordinates data
city_positions = [
    (16, 90),  # Depot
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
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

def euclidean_distance(city1, city2):
    return math.sqrt((city_positions[city1][0] - city_positions[city2][0]) ** 2 + (city_positions[city1][1] - city_positions[city2][1]) ** 2)

# Calculate tour based on given city indices
def calculate_tour_and_cost(city_indices):
    total_cost = 0
    tour = [0]
    last_city = 0

    for city in city_inverse:
        tour.append(city)
        total_cost += euclidean_distance(last_city, city)
        last_city = city

    # Return to the depot
    total_cost += euclidean_distance(last_city, 0)
    tour.append(0)
    
    return tour, total_cost

# Brute force through all combinations, one from each group
min_cost = float('inf')
best_tour = None

for combination in itertools.product(*city_groups):
    city_inverse = list(combination)
    tour, cost = calculate_tour_and_cost(city_inverse)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

print("Tour:", best_tour)
print("Total travel cost:", min_cost)