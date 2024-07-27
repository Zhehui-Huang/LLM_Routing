from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import numpy as np
from math import sqrt

coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69)
}

def euclidean_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Number of cities
num_cities = len(coordinates)
num_robots = 8

# Create the distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for from_idx in range(num_cities):
    for to_idx in range(num_cities):
        if from_idx != to_idx:
            distance_matrix[from_idx, to_idx] = euclidean_distance(coordinates[from_idx], coordinates[to_idx])
        else:
            distance_matrix[from_idx, to_idx] = 0

# Create the routing model
manager = pywrapcp.RoutingIndexManager(num_cities, num_robots, 0)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.time_limit.FromSeconds(10)
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

solution = routing.SolveWithParameters(search_parameters)

def print_solution(manager, routing, solution):
    total_distance = 0
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_id)
        plan_output = 'Robot {} Tour: '.format(vehicle_id)
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += '{} -> '.format(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += '{}'.format(manager.IndexToNode(index))
        print(plan_output)
        print('Robot {} Total Travel Cost: {}'.format(vehicle_id, route_distance))
        total_distance += route_distance
    print('Overall Total Travel Cost: {}'.format(total_distance))

# Display the results
if solution:
    print_solution(manager, routing, solution)
else:
    print("No solution found!")