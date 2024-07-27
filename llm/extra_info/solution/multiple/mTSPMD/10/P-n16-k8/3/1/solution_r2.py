import math
import numpy as np

# Given data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41), 
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Euclidean distance calculator
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Calculate all pairwise distances
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean_distance(cities[i], cities[j])
    return distances

# Nearest Neighbor heuristic for TSP solving from a specific city over a set of cities
def nearest_neighbor_tsp(start, cities_to_visit, distances):
    unvisited = cities_to_visit.copy()
    tour = [start]
    current_city = start
    total_cost = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current_city][x])
        total_cost += distances[current_city][next_city]
        current_city = next_city
        tour.append(current_city)
        unvisited.remove(current_field)
    
    total_cost += distances[current_city][start]  # Completing the tour by returning to start
    tour.append(start)
    return tour, total_cost

# Solving the MTSP
def solve_mtsp():
    distances = calculate_distances(cities)
    total_overall_cost = 0
    robot_results = {}
    
    for robot_id in range(8):
        cities_to_visit = list(range(8, 16))  # Assume robots visit other cities except depots
        if robot_id in cities_to_visit:
            cities_to_visit.remove(robot_id)
        tour, cost = nearest_neighbor_tsp(robot_id, cities_to_visit, distances)
        robot_results[robot_id] = (tour, cost)
        total_overall_cost += cost
    
    return robot_results, total_overall_cost

# Execute and display results
robot_tours, overall_cost = solve_mtsp()
for robot_id, (tour, cost) in robot_tours.items():
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {overall_cost}")