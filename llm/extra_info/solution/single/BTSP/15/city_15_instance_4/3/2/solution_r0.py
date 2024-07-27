import math
from itertools import permutations

# Coordinates of cities
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

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate distances matrix
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Function to calculate the total and max distance of a tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distances[tour[i]][tour[i + 1]]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Brute force function to find optimal tour minimizing max distance
def find_optimal_tour():
    best_tour = None
    min_max_distance = float('inf')
    total_cost_min_max = float('inf')

    # Generate all permutations of cities except the depot
    for perm in permutations(range(1, num_cities)):
        # Build the tour starting and ending at the depot
        tour = [0] + list(perm) + [0]
        total_cost, max_distance = evaluate_tour(tour)
        if max_distance < min_max_distance:
            best_tour = tour
            min_max_distance = max_distance
            total_cost_min_max = total_cost
        elif max_distance == min_max_distance:
            if total_cost < total_cost_min_max:
                best_tour = tour
                min_max_distance = max_distance
                total_cost_min_max = total_list

    return best_tour, total_cost_min_max, min_max_distance

# Running the solver
optimal_tour, total_cost, max_distance = find_optimal_tour()
optimal_tour_output = {
    "Tour": optimal_tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

print(optimal_tour_output)