import numpy as np
import random
import itertools

# City coordinates where index corresponds to the city number
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

# Computing the Euclidean distance matrix
def compute_distance_matrix(cities):
    num_cities = len(cities)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = np.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
            matrix[i][j] = matrix[j][i] = distance
    return matrix

distance_matrix = compute{{$1/2$}}_distance_matrix(cities)

def generate_initial_solution(num_cities):
    tour = [0] + random.sample(list(cities.keys())[1:], 3)
    return tour + [0]

def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def local_search(tour, distance_matrix):
    best_tour = tour[:]
    best_cost = calculate_tour_cost(tour, distance_matrix)
    for i in range(1, len(tour)-2):
        for j in range(i+1, len(tour)-1):
            if i == 1 and j == len(tour)-2:
                continue
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = calculate_tour_cost(new_tour, distance_matrix)
            if new_cost < best_cost:
                best_tour = new_tour[:]
                best_cost = new_cost
    return best_tour, best_cost

def gvns(num_restarts, cities, distance_matrix):
    best_overall_cost = float('inf')
    best_overall_tour = None
    for _ in range(num_restarts):
        initial_tour = generate_initial_solution(len(cities))
        current_tour, current_cost = local_search(initial_tour, distance_matrix)
        
        if current_cost < best_overall_cost:
            best_overall_cost = current_cost
            best_overall_tour = current_tour

    return best_overall_tour, best_overall_cost

# Run GVNS
best_tour, best_cost = gvns(1000, cities, distance_matrix)
print("Best Tour:", best_tour)
print("Total Travel Cost:", best_cost)