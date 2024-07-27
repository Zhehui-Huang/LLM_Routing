import numpy as np
import random

# Distance function
def calculate_distance(city1, city2, cities):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Initiate all distances
def create_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i, num_cities):
            if i != j:
                dist = calculate_distance(i, j, cities)
                dist_matrix[i, j] = dist
                dist_matrix[j, i] = dist
            else:
                dist_matrix[i, j] = float('inf')
    return dist_matrix

# Initial solution generator using the Nearest Neighbor strategy
def initialize_tours(num_robots, start_city, cities):
    num_cities = len(cities)
    all_cities = set(range(num_cities))
    tours = [[] for _ in range(num_robots)]
    unvisited = set(range(1, num_cities))  # assuming all start from city 0 and each must visit city 0 at the start
    current_cities = [start_city] * num_robots

    # Initialize the first step out from the depot
    for i in range(num_robots):
        nearest = min(unvisited, key=lambda x: distance_matrix[start_city][x])
        tours[i].extend([start_city, nearest])
        current_cities[i] = nearest
        unvisited.remove(nearest)

    # Greedily build up the rest of the tours
    while unvisited:
        for i in range(num_robots):
            if not unvisited:
                break
            nearest = min(unvisited, key=lambda x: distance_matrix[current_cities[i]][x])
            tours[i].append(nearest)
            current_cities[i] = nearest
            unvisited.remove(nearest)

    return tours

# Calculate tour cost
def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Settings and initialization
cities = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
          10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63),
          19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)}

num_robots = 8
start_city = 0  # Depot city 0 as the starting location

distance_matrix = create_distance_matrix(cities)
tours = initialize_tours(num_robots, start_city, cities)

# Tabu Search specifics skipped

# Output results
total_cost = 0
for i, tour in enumerate(tours):
    tour_cost = calculate_tour_cost(tour + [tour[0]], distance_matrix)  # coming back to start point
    total_cost += tour_cost
    print(f"Robot {i} Tour: {tour + [tour[0]]}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print("Overall Total Travel Cost: {:.2f}".format(total_cost))