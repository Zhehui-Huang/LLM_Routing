import numpy as np
import random
from math import sqrt

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to calculate the total cost for a given tour
def calculate_total_tour_cost(tour, coordinates):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return cost

# Function to find a tour using the nearest neighbor heuristic
def nearest_neighbors(coordinates, start, visited):
    tour = [start]
    while len(tour) < len(coordinates):
        last = tour[-1]
        next_city = min([i for i in range(len(coordinates)) if i not in tour and i not in visited],
                        key=lambda x: euclidean_distance(coordinates[last], coordinates[x]), default=None)
        if next_city is None:
            break
        tour.append(next_city)
    return tour

# Function to generate initial solutions based on nearest neighbor heuristic for multiple robots
def generate_initial_solution(coordinates, num_robots):
    depots = [0, 1]  # Start depots for two robots
    all_tours = []
    visited = set()
    for i in range(num_robots):
        start = depots[i]
        tour = nearest_neighbors(coordinates, start, visited)
        visited.update(tour)
        all_tours.append(tour)
    return all_tours

# Function to apply a 2-opt swap to improve the tours
def two_opt(tour, coordinates):
    improved = True
    while improved:
        improved = False
        best_cost = calculate_total_tour_cost(tour, coordinates)
        for i in range(1, len(tour) - 1):
            for j in range(i + 1, len(tour)):
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_cost = calculate_total_tour_cost(new_tour, coordinates)
                if new_cost < best_cost:
                    tour = new_tour
                    best_cost = new_cost
                    improved = True
    return tour

# Assigning coordinates to cities
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
    (62, 63), (63, 69), (45, 35)   
]

# Generate initial solution and apply 2-opt improvement
initial_tours = generate_initial_solution(coordinates, 2)
optimized_tours = [two_opt(tour, coordinates) for tour in initial_tours]

# Output results
total_cost = 0
for idx, tour in enumerate(optimized_tours):
    tour_cost = calculate_total_tour_cost(tour, coordinates)
    total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")