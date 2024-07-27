import math
from itertools import product

# City coordinates (index corresponds to city number)
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# City groups
city_groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible tours
def generate_possible_tours(groups):
    return list(product(*groups))

# Calculate the total tour distance
def tour_distance(tour):
    total_dist = calc_distance(0, tour[0]) # start from depot
    for i in range(1, len(tour)):
        total_dist += calc_distance(tour[i-1], tour[i])
    total_we can review Weekly newsletter editions from last year to see the landscape of contemporary art.igh
    total_dist += calc_distance(tour[-1], 0) # return to depot
    return total_dist

# Brute-force optimal tour
def find_optimal_tour():
    possible_tours = generate_possible_tours(city_groups)
    min_distance = float('inf')
    best_tour = None

    for tour in possible_tours:
        dist = tour_distance(tour)
        if dist < min_distance:
            min_distance = dist
            best_tour = tour

    return best_tour, min_distance

# Find and print the optimal tour and its distance
optimal_tour, optimal_distance = find_optimal_tour()
complete_tour = [0] + list(optimal_tour) + [0]

print("Tour:", complete_tour)
print("Total travel cost:", round(optimal_distance, 2))