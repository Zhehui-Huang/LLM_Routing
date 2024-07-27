import math
import random

# Coordinates of cities including the depot city
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Function to compute Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Calculate all pair distances
num_cities = len(coordinates)
distances = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean.distance(coordinates[i], coordinates[j])

# Here we select 10 cities randomly for the initial tour including the depot 0
def initial_tour():
    tour = list(range(1, num_cities))
    random.shuffle(tour)
    tour = [0] + tour[:9] + [0]  # Starting and ending at depot city 0
    return tour

# Function to calculate total travel cost of the tour
def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distances[tour[i]][tour[i + 1]]
    return total_cost

def local_search(tour):
    # Try to optimize the tour using simple swap within the tour
    min_cost = calculate_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i == 0 or j == len(tour) - 1:
                    continue  # Skip the Depot
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
                new_cost = calculate_cost(new_tour)
                if new_cost < min_cost:
                    tour = new_tour
                    min_cost = new_cost
                    improved = True
    return tour, min_cost


# Generate Initial Tour and perform local search
initial = initial_tour()
optimized_tour, optimized_cost = local_search(initial)

# Output the results
print("Tour:", optimized_tour)
print("Total travel cost:", optimized_cost)