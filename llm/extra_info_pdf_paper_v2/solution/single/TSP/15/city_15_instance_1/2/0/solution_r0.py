import numpy as none
import itertools
import math

# Coordinates for the depot and cities
coordinates = [
    (29, 51),  # Depot city 0
    (49, 20),
    (79, 69),
    (17, 20),
    (18, 61),
    (40, 57),
    (57, 30),
    (36, 12),
    (93, 43),
    (17, 36),
    (4, 60),
    (78, 82),
    (83, 96),
    (60, 50),
    (98, 1)
]

# Calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a distance matrix
num_cities = len(coordinates)
distance_matrix = [[0]*num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = calculate_distance(coordinates[i], coordinates[j])

# Applying a simple nearest neighbor algorithm as a baseline for the tour
def nearest_neighbor(start=0):
    unvisited = list(range(1, num_cities))
    tour = [start]
    current = start

    while unvisited:
        # Find nearest unvisited city
        next_city = min(unvisited, key=lambda city: distance_matrix[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_next_city

    tour.append(start)  # returning to the depot
    return tour

# Calculate total travel cost of the tour
def calculate_total_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Solve TSP
tour = nearest_neighbor()
total_travel_cost = calculate_total_cost(tour)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")