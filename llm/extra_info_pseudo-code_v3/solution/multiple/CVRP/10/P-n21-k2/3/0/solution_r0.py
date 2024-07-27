import math
from typing import List, Tuple

def euclidean_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def compute_distance_matrix(locations: List[Tuple[int, int]]) -> List[List[float]]:
    n = len(locations)
    distance_matrix = [[euclidean_distance(locations[i], locations[j]) for j in range(n)] for i in range(n)]
    return distance_matrix

locations = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15
]

distance_matrix = compute_distance_matrix(locations)
num_robots = 2
robot_capacity = 160

def solve_cvrp(locations, demands, distance_matrix, num_robots, capacity):
    num_cities = len(locations)
    routes = [[] for _ in range(num_robots)]
    load = [0] * num_robots
    visited = [False] * num_cities
    visited[0] = True  # Depot city is always considered visited
    
    # Greedy Assignment to robots
    for robot in range(num_robots):
        current_city = 0
        while True:
            next_city = None
            min_distance = float('inf')
            for i in range(1, num_cities):
                if not visited[i] and (load[robot] + demands[i] <= capacity) and distance_matrix[current_city][i] < min_distance:
                    min_distance = distance_matrix[current_city][i]
                    next_city = i
            if not next_city:
                break
            routes[robot].append(next_city)
            load[robot] += demands[next_city]
            visited[next_city] = True
            current_city = next_city
        routes[robot].insert(0, 0)  # Start from depot
        routes[robot].append(0)  # Return to depot
    
    return routes

routes = solve_cvrp(locations, demands, distance_matrix, num_robots, robot_capacity)

def calculate_route_cost(route, distance_matrix):
    cost = 0
    for i in range(len(route) - 1):
        cost += distance_matrix[route[i]][route[i + 1]]
    return cost

# Output
overall_total_cost = 0
for index, route in enumerate(routes):
    cost = calculate_route_cost(route, distance_matrix)
    overall_total_cost += cost
    print(f"Robot {index} Tour:", route)
    print(f"Robot {index} Total Travel Cost:", cost)

print("Overall Total Travel Cost:", overall_total_cost)