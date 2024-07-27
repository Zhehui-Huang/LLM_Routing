import math
from itertools import combinations

# Given data
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
               (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
               (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
num_robots = 2
robot_capacity = 160

# Calculate Euclidean distance for travel cost estimation
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Assign cities to robots based on a simple heuristic
def assign_cities_to_robots():
    remaining_capacity = [robot_capacity] * num_robots
    robot_routes = [[] for _ in range(num_robots)]
    city_robot_assignment = [-1] * len(coordinates)

    for city in range(1, len(coordinates)):
        assigned = False
        for robot in range(num_robots):
            if remaining_capacity[robot] >= demands[city]:
                robot_routes[robot].append(city)
                city_robot_assignment[city] = robot
                remaining_capacity[robot] -= demands[city]
                assigned = True
                break

        if not assigned:
            # If no robot could take the city due to capacity, assign forcefully to least loaded robot
            least_loaded_robot = remaining_capacity.index(max(remaining_capacity))
            robot_routes[least_loaded_robot].append(city)
            remaining_capacity[least_loaded_robot] -= demands[city]

    return robot_routes

# Function to find the shortest route for a given set of cities
def find_shortest_route(cities):
    best_order = None
    best_cost = float('inf')
    for order in combinations(cities, len(cities)):
        order = [0] + list(order) + [0]  # start and end at the depot
        cost = sum(distance(order[i], order[i+1]) for i in range(len(order) - 1))
        if cost < best_cost:
            best_cost = cost
            best_order = order

    return best_order, best_cost

def solve_vrp():
    robot_routes = assign_cities_to_robots()
    total_cost = 0
    solution_details = []

    for i, route in enumerate(robot_routes):
        tour, cost = find_shortest_route(route)
        solution_details.append(f"Robot {i} Tour: {tour}")
        solution_details.append(f"Robot {i} Total Travel Cost: {cost:.2f}")
        total_cost += cost

    solution_details.append(f"Overall Total Travel Cost: {total_cost:.2f}")
    return solution_details

# Generate the solution
solution = solve_vrp()
for line in solution:
    print(line)