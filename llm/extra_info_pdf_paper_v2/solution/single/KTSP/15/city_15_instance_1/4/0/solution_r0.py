import math
from itertools import permutations
import random

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return distance_matrix

def generate_initial_tour(num_cities, k):
    tour = random.sample(range(1, num_cities), k - 1)
    tour = [0] + tour + [0]  # Start and end at the depot
    return tour

def local_search(tour, distance_matrix, k):
    improved = True
    best_tour = tour[:]
    best_cost = total_tour_cost(tour, distance_map)
    while improved:
        improved = False
        for i in range(1, k - 1):
            for j in range(i + 1, k):
                new_tour = best_tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = total_tour_cost(new_tour, distance_map)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour
                    improved = True
    return best_tour, best_cost

# Define the cities positions
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30),
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Compute the distance matrix
distance_map = calculate_distance_name_matrix(cities)

# Parameters
k = 6  # Number of cities to be visited

# Generate an initial tour
current_tour = generate_initial_tour(len(cities), k)

# Perform local search to find the best solution
best_tour, best_cost = local_search(current_tour, distance_map, k)

# Output the final results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)