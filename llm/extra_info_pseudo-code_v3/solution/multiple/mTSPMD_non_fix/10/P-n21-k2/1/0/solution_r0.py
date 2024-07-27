import numpy as. np
from math import sqrt
from random import choice
import itertools

# City coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

# Calculate distances between cities
def euclidean_distance(city1, city2):
    return sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Number of robots
num_robots = 2

# Starting depots assuming two robots start from the same depot city 0 (Depot 0)
start_depots = [0, 0]

# NUMPY Array to hold distances
distance_matrix = np.zeros((len(coordinates), len(coordinates)))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        distance_matrix[i, j] = euclidean

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i + 1])
    return cost

# Nearest Neighbor tour initialization
def nearest_neighbor_tour(start_city):
    tour = [start_city]
    unvisited_cities = set(range(len(coordinates))) - {start_city}

    current_city = start_city
    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        current_city = next_city
        unvisited_cities.remove(next_city)
    return tour

# Get initial tours for each robot
tours = [nearest_neighbor_tour(start_depots[i]) for i in range(num_robots)]

# Improve tours using Tabu Search
def tabu_search(tours):
    max_iterations = 100
    tabu_list = []
    best_solution = tours
    best_cost = sum(calculate_tour_cost(tour) for tour in tours)

    for iteration in range(max_iterations):
        # Generate neighbors by swap within a tour
        all_possible_swaps = []
        for robot_index, tour in enumerate(tours):
            for i, j in itertools.combinations(range(1, len(tour) - 1), 2):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                all_possible_swaps.append((robot_index, new_tour))

        # Evaluate all neighbors and select the best non-taboo move
        for robot_index, new_tour in all_possible_swaps:
            new_tours = tours[:]
            new_tours[robot_index] = new_tour
            new_cost = sum(calculate_tour_cost(tour) for tour in new_tours)
            if new_cost < best_cost and new_tour not in tabu_list:
                best_solution = new_tours
                best_cost = new_cost
                tabu_list.append(new_tour)
                if len(tabu_list) > 10:  # Limit tabu list size
                    tabu_list.pop(0)

    return best_solution

optimized_tours = tabu_search(tours)

# Print output according to the required format
overall_cost = 0
for idx, tour in enumerate(optimized_tours):
    tour_cost = calculate_tour_cost(tour)
    overall_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_icon():.2f}")