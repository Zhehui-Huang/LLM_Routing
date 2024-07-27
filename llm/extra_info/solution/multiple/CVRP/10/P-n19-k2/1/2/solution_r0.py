import numpy as np
import itertools

# Define the cities and their coordinates and demands
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robot information
num_robots = 2
capacity = 160
start_location = 0

# Compute distances between cities
def calculate_distances(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i][j] = np.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)
    return dist_matrix

distances = calculate_distances(coordinates)

# Simple heuristic to create a valid set of tours
def create_tours(demands, capacity):
    remaining_cities = list(range(1, len(demands)))  # start from 1 to exclude depot
    tours = []
    while remaining_cities:
        tour = [0]  # start each tour from the depot
        load = 0
        for city in remaining_cities[:]:
            if demands[city] + load <= capacity:
                tour.append(city)
                load += demands[city]
                remaining_cities.remove(city)
        tour.append(0)  # end each tour at the depot
        tours.append(tour)
    return tours

# Assign these tours to robots
tours = create_tours(demands, capacity)

# Calculation of total travel cost for a given tour
def tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Display results
overall_total_cost = 0
for i, tour in enumerate(tours):
    cost = tour_cost(tour, distances)
    overall_total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Reverse Assistant Output: {overall_total_cost:.2f}")