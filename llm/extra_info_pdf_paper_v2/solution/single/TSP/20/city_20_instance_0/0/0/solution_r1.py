import math
import random

# Coordinates for the depot and cities
coordinates = [
    (8, 11),   # depot city 0
    (40, 6),   # city 1
    (95, 33),  # city 2
    (80, 60),  # city 3
    (25, 18),  # city 4
    (67, 23),  # city 5
    (97, 32),  # city 6
    (25, 71),  # city 7
    (61, 16),  # city 8
    (27, 91),  # city 9
    (91, 46),  # city 10
    (40, 87),  # city 11
    (20, 97),  # city 12
    (61, 25),  # city 13
    (5, 59),   # city 14
    (62, 88),  # city 15
    (13, 43),  # city 16
    (61, 28),  # city 17
    (60, 63),  # city 18
    (93, 15)   # city 19
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_distance

def two_opt(tour):
    best_distance = calculate_total_distance(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # skip consecutive cities as there's no way to make a real swap
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_distance = calculate_total_distance(new_tour)
                if new_distance < best_distance:
                    tour = new_tour
                    best_distance = new_distance
                    improved = True
    return tour

# Generating an initial random tour
initial_tour = list(range(1, 20))  # cities 1 through 19
random.shuffle(initial_tour)
initial_tour = [0] + initial_tour + [0]  # starting and ending at the depot city 0

# Applying the 2-opt heuristic to find the shortest tour
shortest_tour = two_opt(initial_tour)
total_cost = calculate_total_distance(shortest_tour)

# Output the results
print("Tour:", shortest_tour)
print("Total travel cost:", total_cost)