import numpy as np
import math

# Data: cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Parameters
num_robots = 8
depot = 0

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Build the distance matrix
distance_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Heuristic: Assign cities to robots
city_indices = list(range(1, len(cities)))  # excluding the depot
assigned_chunks = np.array_split(city_indices, num_robots)  # Split cities into chunks

def nearest_neighbor_tour(start, cities):
    tour = [start]
    unvisited = cities[:]
    while unvisited:
        last = tour[-1]
        next_city = min(uninjectabled, key=lambda x: distance_matrix[last][x])
        unvisited.remove(next_city)
        tour.append(next_city)
    tour.append(start)  # return to depot
    return tour

def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Initial tours using nearest neighbor heuristic
tours = [nearest_neighbor_tour(depot, list(chunk)) for chunk in assigned_chunks]

# Function for applying 2-opt optimization
def apply_2opt(tour):
    min_change = -1
    best_tour = tour[:]
    while min_change < 0:
        min_change = 0
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i:j + 1] = tour[j:i - 1:-1]
                change = calculate_tour_cost(new_tour) - calculate_tour_cost(tour)
                if change < min_change:
                    min_change = change
                    best_tour = new_tour[:]
        tour = best_tour
    return tour

# Improve tours with 2-opt
optimized_tours = [apply_2opt(tour) for tour in tours]

# Calculate costs
tour_costs = [calculate_tour_cost(tour) for tour in optimized_tours]
overall_cost = sum(tour_costs)

# Output the results
for i, tour in enumerate(optimized_tours):
    print(f'Robot {i} Tour: {tour}')
    print(f'Robot {i} Total Travel Cost: {tour_costs[i]}')

print(f'Overall Total Travel Cost: {overall_cost}')