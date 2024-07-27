import numpy as np
from scipy.spatial.distance import euclidean
import itertools

# Define the cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Number of robots
num_robots = 8

# Calculate distances between each pair of cities using Euclidean distance
def calculate_distances(cities):
    n = len(cities)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

distances = calculate_distances(cities)

# Compute the travel cost of a given tour
def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Generate an initial solution by assigning cities to robots
def initial_solution(cities, num_robots):
    all_cities = list(range(1, len(cities)))  # Exclude the depot
    chunks = [all_cities[i::num_robots] for i in range(num_robots)]
    tours = [[0] + chunk + [0] for chunk in chunks]  # Create tours starting/ending at the depot
    return tours

# Apply 2-opt optimization to improve the tours
def optimize_tours(tours, distance_matrix, num_iterations=100):
    for iteration in range(num_iterations):
        for i in range(len(tours)):
            for j in range(1, len(tours[i]) - 2):
                for k in range(j + 1, len(tours[i]) - 1):
                    # Try reversing the segment between j and k
                    new_tour = tours[i][:j] + tours[i][j:k + 1][::-1] + tours[i][k + 1:]
                    if calculate_tour_cost(new_tour, distance_matrix) < calculate_tour_cost(tours[i], distance_matrix):
                        tours[i] = new_tour
    return tours

tours = initial_solution(cities, num_robots)
optimized_tours = optimize_tours(tours, distances)

overall_total_cost = 0
for i, tour in enumerate(optimized_tours):
    tour_cost = calculate_tour_cost(tour, distances)
    overall_total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Powle SlideCost: {overall_total_cost}")