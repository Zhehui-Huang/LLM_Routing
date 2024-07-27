import math
import numpy as np

# City coordinates excluding the depot
city_coords = [
    (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232),
    (128, 231), (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)
]
depot = (145, 215)
coords = [depot] + city_coords

# Number of robots
num_robots = 4

# Calculate Euclidean distance matrix
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distance_matrix = [[euclidean_distance(coords[i], coords[j]) for j in range(len(coords))] for i in range(len(coords))]

# Define a simple initial solution distribution function
def initial_solution_distribution(num_robots, cities):
    n = len(cities)
    avg = n // num_robots
    leftovers = n % num_robots
    tours = []
    start = 1
    for r in range(num_robots):
        end = start + avg + (1 if r < leftovers else 0)
        tours.append([0] + cities[start:end] + [0])
        start = end
    return tours

initial_cities = list(range(1, len(coords)))  # city indices excluding the depot
initial_tours = initial_solution_distribution(num_robots, initial_cities)

# Function to calculate the cost of a tour
def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# 2-opt optimization
def optimize_tour(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+2, len(tour)):
                if j-i == 1: continue  # Skip adjacent edges
                if calculate_tour_cost(tour[i:j+1]) > calculate_tour_cost(tour[i:j+1][::-1]):
                    tour[i:j+1] = tour[i:j+1][::-1]
                    improved = True
    return tour

optimized_tours = [optimize_tour(tour) for tour in initial_tours]

# Calculate and print the results
total_cost = 0
for idx, tour in enumerate(optimized_tours):
    tour_cost = calculate_tour_cost(tour)
    total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")