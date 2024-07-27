import math
from itertools import permutations

# Define coordinates of cities
coordinates = [
    (30, 56),  # Depot city 0
    (53, 42),
    (1, 95),
    (25, 61),
    (69, 57),
    (6, 58),
    (12, 84),
    (72, 77),
    (98, 95),
    (11, 0),
    (61, 25),
    (52, 0),
    (60, 95),
    (10, 94),
    (96, 73),
    (14, 47),
    (18, 16),
    (4, 43),
    (53, 76),
    (19, 72)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate distance matrix
num_cities = len(coordinates)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

def calculate_total_distance(tour):
    total_distance = 0
    for k in range(len(tour) - 1):
        total_distance += distance_matrix[tour[k]][tour[k + 1]]
    return total_distance

def find_shortest_tour():
    best_tour = None
    best_cost = float('inf')
    for tour_permutation in permutations(range(1, num_cities)):
        tour = [0] + list(tour_permutation) + [0]  # starting and ending at the depot
        current_cost = calculate_total_distance(tour)
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = tour
    return best_tour, best_cost

# Compute the shortest tour and the total travel cost
shortest_tour, total_travel_cost = find_shortest_tour()

# Output the tour and the total cost
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {total_travel dist}:.2f}")