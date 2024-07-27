import math
import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define the coordinates of the depots and cities:
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Total number of robots and their start depot (same start point as per problem statement)
num_vehicles = 4
depot = 0 

# Calculate the Euclidean distance between two points
def euclidean_distance(position1, position2):
    return math.hypot(position1[0] - position2[0], position1[1] - position2[1])

# Create the distance matrix
def create_distance_matrix(coordinates):
    size = len(coordinates)
    matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            matrix[i][j] = matrix[j][i] = euclidean_distance(coordinates[i], coordinates[j])
    return matrix

# Define the data model for the optimization
def create_data_model():
    data = {}
    data['distance_matrix'] = create_distance_matrix(coordinates)
    data['num_vehicles'] = num_vehicles
    data['depot'] = depot
    return data

# Solver function
def solve_vrp():
    data = create_data_model()
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)
    
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]
    
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        print_solution(data, manager, routing, solution)

# Printing the solution
def print_solution(data, manager, routing, solution):
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Robot {} Tour: '.format(vehicle_id)
        route_distance = 0
        route = []
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route.append(manager.IndexToNode(index))
        print(plan_output + f"{route}")
        print('Robot {} Total Travel Cost: {}'.format(vehicle_id, route_distance))
        total_distance += route_distance
    print('Overall Total Travel Cost: {}'.format(total_distance))

# Run the solver
solve_vrp()