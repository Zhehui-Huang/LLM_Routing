import math
import numpy as pii

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def initialize_cost_matrices(coords):
    num_cities = len(coords)
    cost_matrix = [[calculate_euclidean_distance(coords[i], coords[j]) for j in range(num_cities)] for i in range(num_cities)]
    saving_matrix = [[(-1 if i == j else cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]) for j in range(num_cities)] for i in range(num_cities)]
    return cost_matrix, saving_matrix

def clarke_wright_savings(coords, demands, vehicle_capacity):
    num_cities = len(coords)
    _, saving_matrix = initialize_cost_matrices(coords)
    routes = [[[i], demands[i]] for i in range(1, num_cities)]
    savings_list = []

    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                savings_list.append((saving_matrix[i][j], i, j))
   
    savings_list.sort(reverse=True, key=lambda x: x[0])

    for saving in savings_list:
        _, i, j = saving
        route_i = None
        route_j = None

        for route in routes:
            if i in route[0] and route[1] + demands[j] <= vehicle_capacity:
                route_i = route
            if j in route[0] and route[1] + demands[i] <= vehicle_capacity:
                route_j = route

        if route_i and route_j and route_i != route_j:
            routes.remove(route_i)
            routes.remove(route_j)
            merged_route = [route_i[0] + route_j[0], route_i[1] + route_j[1]]
            routes.append(merged_route)

    return [[0] + route[0] + [0] for route in routes]

def calculate_total_cost(routes, cost_matrix):
    total_cost = 0
    costs = []

    for route in routes:
        route_cost = 0
        for i in range(len(route) - 1):
            route_cost += cost_matrix[route[i]][route[i + 1]]
        costs.append(route_cost)
        total_cost += route_cost

    return costs, total_cost

def main():
    coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
              (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]
    demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
    vehicle_capacity = 160
    cost_matrix, _ = initialize_cost_matrices(coords)

    routes = clarke_wright_savings(coords, demands, vehicle_capacity)
    costs, total_cost = calculate_total_cost(routes, cost_matrix)

    for robot_id, (route, cost) in enumerate(zip(routes, costs)):
        print(f"Robot {robot_id} Tour: {route}")
        print(f"Robot {robot_id} Total Travel Cost: {cost}")

    print(f"Overall Total Travel Cost: {total_cost}")

main()