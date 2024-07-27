import math
from itertools import permutations

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def calculate_total_cost(route, distance_matrix):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += distance_matrix[route[i]][route[i + 1]]
    return total_cost

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Create a distance matrix
num_cities = len(cities)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Assign robots and cities
robot_depots = {i: i for i in range(8)}  # depot assignments (robot i starts at city i)
assigned_cities = list(range(8, 16))  # assigned remaining cities

# Find optimal path for each robot (this is a simple heuristic approach)
overall_total_cost = 0
for robot_id, start_city in robot_depots.items():
    potential_cities = [start_city] + assigned_cities
    min_route_cost = float('inf')
    best_route = None
    
    for route in permutations(potential_cities):
        if route[0] == start_city and route[-1] == start_city:
            route_cost = calculate_total_cost(route, distance_matrix)
            if route_cost < min_route_cost:
                min_route_cost = route_cost
                best_route = route

    print(f"Robot {robot_id} Tour: {best_route}")
    print(f"Robot {robot_id} Total Travel Cost: {min_route_cost:.2f}")
    overall_total_cost += min_route_cost
    # Redefine assigned cities for the next robot
    assigned_cities = [city for city in assigned_cities if city not in best_route[1:-1]]

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")