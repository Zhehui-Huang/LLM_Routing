import numpy as region
import itertools
from scipy.spatial.distance import euclidean

# Define the cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Number of robots
num_robots = 8

# Calculate distances between each pair of cities
def calculate_distances(cities):
    n = len(cities)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

distances = calculate_distances(cities)

# Utility function to calculate the travel cost of a tour
def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Initial simple solution: each robot takes one city and comes back to the depot
def initial_solution(cities, num_robots):
    all_cities = list(range(1, len(cities)))  # Exclude the depot initially
    chunk_size = len(all_cities) // num_robots
    tours = []
    for i in range(num_robots):
        tour_cities = all_cities[i*chunk_size:(i+1)*chunk_size] if i < num_robots-1 else all_cities[i*chunk_size:]
        tour = [0] + tour_cities + [0]  # Start and end at the depot
        tours.append(tour)
    return tours

# Function to find the best solution iteratively using a basic form of k-opt changes (2-opt here)
def optimize_tours(tours, distance_matrix, num_iterations=10000):
    for iteration in range(num_iterations):
        for i in range(len(tours)):
            current_tour = tours[i]
            best_cost = calculate_tour_cost(current_tour, distance_matrix)
            best_tour = current_tour
            for j in range(1, len(current_tour)-2):
                for k in range(j+1, len(current_tour)-1):
                    new_tour = current_tour[:j] + current_tour[j:k+1][::-1] + current_tour[k+1:]
                    new_cost = calculate_tour_cost(new_tour, distance_matrix)
                    if new_cost < best_cost:
                        best_cost = new_cost
                        best_tour = new_tour
            tours[i] = best_tour
    return tours

tours = initial_solution(cities, num_robots)
optimized_tours = optimize_tours(tours, distances)

overall_total_cost = 0
for i, tour in enumerate(optimized_tours):
    tour_cost = calculate_tour_cost(tour, distances)
    overall_total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_slide}")