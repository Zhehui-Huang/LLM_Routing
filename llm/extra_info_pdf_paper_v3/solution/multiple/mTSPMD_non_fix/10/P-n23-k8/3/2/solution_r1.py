import numpy as np
from scipy.spatial.distance import euclidean

# Coordinates of cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Calculate distance matrix
def calculate_distance_matrix(coords):
    num_cities = len(coords)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            matrix[i][j] = euclidean(coords[i], coords[j])
    return matrix

distance_matrix = calculate_distance_matrix(coordinates)

# Number of robots and initial city - all starting at the first depot
num_robots = 8
start_city = 0

# A simple greedy nearest neighbor algorithm to distribute cities to robots
def greedy_tsp(robot_count, start, dist_matrix):
    total_cities = len(dist_matrix)
    unvisited = set(range(total_cities))
    unvisited.remove(start)
    tours = {i: [start] for i in range(robot_count)}
    
    current_positions = [start] * robot_count
    while unvisited:
        for robot in range(robot_count):
            if not unvisited:
                break
            current_city = current_positions[robot]
            next_city = min(unvisited, key=lambda x: dist_matrix[current_city][x])
            tours[robot].append(next_city)
            current_positions[robot] = next_city
            unvisited.remove(next_city)
            
    return tours

# Calculate tour costs
def calculate_tour_costs(tours, dist_matrix):
    detailed_costs = []
    for tour in tours.values():
        cost = 0
        if len(tour) > 1:
            for i in range(len(tour)-1):
                cost += dist_matrix[tour[i]][tour[i+1]]
        detailed_costs.append(cost)
    return detailed_costs

# Execute TSP solution
tours = greedy_tsp(num_robots, start_city, distance_matrix)
detailed_costs = calculate_tour_costs(tours, distance_matrix)
overall_total_cost = sum(detailed_costs)

# Print results
for robot_id, tour in tours.items():
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {detailed_costs[robot_id]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")