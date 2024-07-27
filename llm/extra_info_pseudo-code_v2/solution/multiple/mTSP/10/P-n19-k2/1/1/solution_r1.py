import math
from itertools import permutations

# Euclidean distance function
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Assignment A heuristic approach to distribute cities among robots considering proximity and balanced workload
def nearest_neighbors_assignment(cities, depot, num_robots):
    unvisited = list(cities.keys())
    unvisited.remove(depot)
    routes = {i: [] for i in range(num_robots)}
    sorted_cities = sorted(unvisited, key=lambda x: euclidean_distance(cities[depot], cities[x]))

    for i, city in enumerate(sorted_cities):
        routes[i % num_robots].append(city)
    
    return routes

# Function to optimize each robot's tour using the nearest neighbor heuristic
def optimize_route(depot, cities, route):
    path = [depot]
    complete_path = [depot]
    nodes = set(route)
    current = depot
    
    while nodes:
        next_node = min(nodes, key=lambda x: euclidean_distance(cities[current], cities[x]))
        path.append(next_node)
        complete_path.append(next_node)
        current = next_node
        nodes.remove(next_node)
    
    path.append(depot)
    complete_path.append(depot)
    return complete_path

# Main environment setup
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}
num_robots = 2
depot = 0

# Assign cities to robots
routes = nearest_neighbors_assignment(cities, depot, num_robots)

# Calculate tours for each robot
overall_cost = 0
for robot_id, route in routes.items():
    tour_route = optimize_route(depot, cities, route)
    path_cost = sum(euclidean_distance(cities[tour_route[i]], cities[tour_route[i + 1]]) for i in range(len(tour_route) - 1))
    overall_cost += path_cost
    print(f"Robot {robot_id} Tour: {tour_route}")
    print(f"Robot {robot_id} Total Travel Cost: {path_cost}")

print(f"Overall Total Travel Cost: {overall as tocost}")