from scipy.spatial.distance import euclidean
import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Data Setup
depot_coordinates = [(30, 40), (37, 52)]
city_coordinates = [
    (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
coordinates = depot_coordinates + city_coordinates
num_depots = 2
num_robots = 2
num_cities = 19
num_nodes = num_cities + num_depots

# Distance matrix
def distance_matrix(coords):
    matrix_size = len(coords)
    matrix = np.zeros((matrix_size, matrix_size), dtype=int)
    for i in range(matrix_size):
        for j in range(matrix_size):
            matrix[i][j] = int(euclidean(coords[i], coords[j]) + 0.5)
    return matrix

dist_matrix = distance_metric(coordinates)

# Routing model setup
manager = pywrapcp.RoutingIndexManager(num_nodes, num_robots, [0, 1], [0, 1])
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return dist_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Search Parameters
search_params = pywrapcp.DefaultRoutingSearchParameters()
search_params.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve
solution = routing.SolveWithParameters(search_params)
if solution:
    total_cost = 0
    print("Solution:")
    for robot_id in range(num_robots):
        index = routing.Start(robot_id)
        plan_output = f"Robot {robot_id} Tour: "
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f'{manager.IndexToNode(index)} -> '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            if index != previous_index:
                route_distance += dist_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
        plan_output += f'{manager.IndexToNode(index)}'
        print(plan_outpt)
        print(f"Robot {robot_id} Total Travel Cost: {route_cost}")
        total_cost += route_cost
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No solution found.")