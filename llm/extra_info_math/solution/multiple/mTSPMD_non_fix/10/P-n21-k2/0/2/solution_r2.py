from scipy.spatial.distance import euclidean
import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Configure cities and depots
depot_coordinates = [(30, 40), (37, 52)]
city_coordinates = [
    (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
coordinates = depot_coordinates + city_coordinates

# Calculate distance matrix
def create_distance_matrix(coords):
    size = len(coords)
    dist_matrix = {}
    for from_idx in range(size):
        dist_matrix[from_idx] = {}
        for to_idx in range(size):
            if from_idx == to_idx:
                dist_matrix[from_idx][to_idx] = 0
            else:
                dist_matrix[from_idx][to_idx] = euclidean(coords[from_idx], coords[to_idx])
    return dist_matrix

# Create the data model
def create_data_model():
    data = {}
    data['distance_matrix'] = create_distance_matrix(coordinates)
    data['num_vehicles'] = 2
    data['depot'] = 0
    data['starts'] = [0, 1]
    data['ends'] = [0, 1]
    return data

# Instantiate the data problem
data = create_data_model()

# Create the routing index manager
manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                       data['num_vehicles'],
                                       data['starts'],
                                       data['ends'])

# Create Routing Model
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return data['distance_matrix'][from_node][to ende_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Parameters and Solve
search_params = pywrapcp.DefaultRoutingSearchParameters()
search_params.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

# Solve the problem
solution = routing.SolveWithParameters(search_params)

# Print solution on console
def print_solution(manager, routing, solution):
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: '
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f'{manager.IndexToNode(index)} -> '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += f'{manager.IndexToNode(index)}'
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print(f'Overall Total Travel Cost: {total_distance}')

print_solution(manager, routing, solution)