import numpy as np
from scipy.spatial.distance import euclidean

# City coordinates and demands configuration
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
    (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robot details
number_of_robots = 2
robot_capacity = 160

def calculate_cost_matrix(coords):
    n = len(coords)
    cost_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                cost_matrix[i][j] = euclidean(coords[i], coords[j])
            else:
                cost_matrix[i][j] = float('inf')
    return cost_matrix

def initial_solution(cost_matrix, demands, capacity):
    n = len(cost_matrix)
    routes = [[] for _ in range(number_of_robots)]
    loads = [0] * number_of_robots  # load for each robot

    city_assigned = [False] * n
    city_assigned[0] = True  # Depot is not a city to be assigned

    for city in range(1, n):
        if demands[city] > capacity:
            raise ValueError("Demand exceeds robot capacity")

        for robot in range(number_of_robots):
            if loads[robot] + demands[city] <= capacity:
                if not routes[robot]:  # Start a new route if empty
                    routes[robot].append(0)  # start from depot
                routes[robot].append(city)
                loads[robot] += demands[city]
                city_assigned[city] = True
                break
    
    # close each route with the depot
    for robot in range(number_of_robots):
        if routes[robot]:
            routes[robot].append(0)

    unassigned_cities = [i for i, assigned in enumerate(city_assigned) if not assigned]
    if unassigned_cities:
        raise ValueError("Not all cities are assigned. Unassigned cities: " + str(unassigned_cities))
    
    return routes

def calculate_route_cost(routes, cost_matrix):
    total_cost = 0
    individual_costs = []
    for route in routes:
        route_cost = 0
        for i in range(len(route) - 1):
            route_cost += cost_matrix[route[i]][route[i + 1]]
        individual_costs.append(route_cost)
        total_cost += route_cost
    return individual_costs, total_cost

# Main execution section
cost_matrix = calculate_cost_matrix(coordinates)
routes = initial_solution(cost_matrix, demands, robot_capacity)
individual_costs, total_cost = calculate_route_cost(routes, cost_matrix)

# Outputting the results
for idx, (route, cost) in enumerate(zip(routes, individual_costs)):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")