import math
import heapq

# Constants
NUMBER_OF_ROBOTS = 4
ROBOT_CAPACITY = 6000

# City coordinates and demands
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [
    0, 1100, 700, 800, 1400, 2100, 
    400, 800, 100, 500, 600, 1200, 
    1300, 1300, 300, 900, 2100, 1000, 
    900, 2500, 1800, 700
]

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def construct_cost_matrix(coords):
    n = len(coords)
    cost_matrix = [[calculate_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]
    return cost_matrix

def solve_cvrp_with_saving_method(cost_matrix, demands, vehicle_capacity, num_vehicles):
    n = len(demands)
    savings = []

    for i in range(1, n):
        for j in range(i + 1, n):
            if i != j:
                savings.append(((cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]), i, j))
    
    # Sorting savings in descending order
    savings.sort(reverse=True, key=lambda x: x[0])

    routes = [[0] for _ in range(num_vehicles)]
    load = [0] * num_vehicles
    used = [False] * n

    while savings:
        _, i, j = savings.pop(0)
        if not used[i] and not used[j]:
            for k in range(num_vehicles):
                if load[k] + demands[i] + demands[j] <= vehicle_capacity:
                    routes[k].extend([i, j])
                    load[k] += (demands[i] + demands[j])
                    used[i] = used[j] = True
                    break

    # Ensure all demands are met, assign remaining demands
    for i in range(1, n):
        if not used[i]:
            for k in range(num_vehicles):
                if load[k] + demands[i] <= vehicle_capacity:
                    routes[k].append(i)
                    load[k] += demands[i]
                    used[i] = True
                    break

    # Close the routes returning to the depot
    for k in range(num_vehicles):
        if routes[k][-1] != 0:
            routes[k].append(0)

    return routes

def calculate_route_cost(route, cost_matrix):
    return sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

def print_solution(routes, cost_matrix):
    total_cost = 0
    for idx, route in enumerate(routes):
        route_cost = calculate_route_cost(route, cost_matrix)
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Compensation: {route_cost}")
        total_cost += route_cost
    print(f"Overall Total Travel Cost: {total_cost}")

# Main execution
cost_matrix = construct_cost_matrix(coordinates)
routes = solve_cvrp_with_saving_method(cost_matrix, demands, ROBOT_CAPACITY, NUMBER_OF_ROBOTS)
print_solution(routes, cost_matrix)