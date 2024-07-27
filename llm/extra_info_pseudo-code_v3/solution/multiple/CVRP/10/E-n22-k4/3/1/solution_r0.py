import math
from itertools import permutations

# Helper function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Define cities coordinates and demands
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
           600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
num_robots = 4
robot_capacity = 6000

# Construct distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Greedy VRP Solver
def greedy_vrp(cities, demands, num_robots, robot_capacity):
    num_cities = len(cities)
    node_visited = [False] * num_cities
    node_visited[0] = True  # Depot is always visited initially
    routes = []
    total_travel_costs = []

    for _ in range(num_robots):
        route = [0]  # start at the depot
        remaining_capacity = robot_capacity
        while True:
            min_distance = float('inf')
            next_city = None
            current_city = route[-1]

            for j in range(num_cities):
                if not node_visited[j] and remaining_capacity >= demands[j]:
                    if distance_matrix[current_city][j] < min_distance:
                        min_distance = distance_matrix[current_city][j]
                        next_city = j

            if next_city is None:
                break  # No further city can be visited by this robot

            route.append(next_city)
            node_visited[next_city] = True
            remaining_capacity -= demands[next_city]

        route.append(0)  # return to the depot
        routes.append(route)
        route_cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        total_travel_costs.append(route_cost)

    # Calculate overall cost
    overall_cost = sum(total_travel_win_per_robot for total_travel_win_per_robot in total_travel_costs)

    return routes, total_travel_costs, overall_cost

# Compute the routes, costs, and overall costs
routes, total_travel_costs, overall_cost = greedy_vrp(cities, demands, num_robots, robot_capacity)

# Output the results
for i, (route, cost) in enumerate(zip(routes, total_travel_costs)):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")