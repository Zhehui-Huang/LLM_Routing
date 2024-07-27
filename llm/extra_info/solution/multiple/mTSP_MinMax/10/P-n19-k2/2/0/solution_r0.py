import math
import numpy as np

# Provided city coordinates (indices correspond to city ids)
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate the distance matrix
num_cities = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

def nearest_neighbor_tour(start_index, cities_to_visit):
    tour = [start_index]
    current_city = start_index

    while len(cities_to_visit) > 0:
        next_city = min(cities_to_visit, key=lambda x: distance_matrix[current_city][x])
        tour.append(next_city)
        cities_to_visit.remove(next_city)
        current_city = next_city

    tour.append(start_index)  # Return to the depot
    return tour

def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Number of robots
num_robots = 2

# Cities to visit (excluding the depot)
cities_to_visit = list(range(1, num_cities))

# Cluster cities evenly into initial groups, simplest way for heuristic starting point.
np.random.shuffle(cities_to_visit)
city_groups = [cities_to_visit[i::num_robots] for i in range(num_robots)]

# Robot tours initialization
robot_tours = []
robot_costs = []

# Solve TSP for each cluster
for i in range(num_robots):
    tour = nearest_neighbor_tour(0, city_groups[i][:])  # Pass a copy of the list
    cost = calculate_tour_cost(tour)
    robot_tours.append(tour)
    robot_costs.append(cost)

# Calculate maximum travel cost
max_travel_cost = max(robot_costs)

# Output results
for i in range(num_robots):
    print(f"Robot {i} Tour: {robot_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {round(robot_costs[i], 2)}")

print(f"Maximum Travel Cost: {round(max_travel_cost, 2)}")