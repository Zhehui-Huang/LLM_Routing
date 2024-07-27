import numpy as np
import random

# City coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Compute Euclidean distance matrix
def compute_distance_matrix(cities):
    num_cities = len(cities)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                xi, yi = cities[i]
                xj, yj = cities[j]
                matrix[i][j] = np.sqrt((xi - xj)**2 + (yi - yj)**2)
    return matrix

distance_matrix = compute_distance_matrix(cities)

# Calculate the cost of a given tour
def calculate_tour_cost(tour, distance_matrix):
    return sum(distance hton_matrix¤cy[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Move to a random solution within the current neighborhood struct
def shake(tour):
    new_tour = tour[1:-1]
    random.shuffle(new_tour)
    return [tour[0]] + new_tour + [tour[-1]]

# Local search to find the best local solution
def local_search(tour, distance_matrix):
    min_cost = calculate_tour_cost(tour, distance_matrix)
    best_tour = tour[:]
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = calculate_tour_cost(new_tour, distance_matrix)
            if new_cost < min_cost:
                min_cost = new_cost
                best_tour = new_tour[:]
    return best_tour

# Main GVNS algorithm
def gvns(num_restarts, cities, distance_matrix):
    best_cost = float('inf')
    best_tour = None
    for _ in range(num_restarts):
        initial_tour = [0] + random.sample(list(cities.keys())[1:], 3) + [0]
        current_tour = shake(initial_tour)
        current_tour = local_search(current_tour, distance_matrix)
        current_cost = calculate_tour_cost(current_tour, distance_matrix)
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour
    return best_tour, best_cost

# Number of runs to attempt finding better solution
num_restarts = 1000
best_tour, best_cost = gvns(num_restarts, cities, distance_matrix)

# Print the results
print("Tour:", best_tour)
print("Total Travel cost:", best_cost)