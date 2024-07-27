import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Coordinates of the cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to calculate Euclidean distance
def euclidean_distance(position1, position2):
    return np.linalg.norm(np.array(position1) - np.array(position2))

# Create distance matrix from coordinates
distance_matrix = [
    [int(euclidean_distance(coordinates[i], coordinates[j])) for j in range(len(coordinates))]
    for i in range(len(coordinates))
]

# Number of vehicles and depot location
num_vehicles = 2
depot = 0

# Create Routing Model
manager = pywrapcp.RoutingIndexManager(len(distance_matrix), num_vehicles, depot)
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    # Returns the distance between the two nodes
    return distance_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting the search parameters
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

if solution:
    # Output tours and costs
    total_cost = 0
    for vehicle_id in range(num_vehicles):
        index = routing.Start(vehicle_id)
        route_distance = 0
        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
        route.append(manager.IndexToNode(index))  # Append the depot
        print(f'Robot {vehicle_id} Tour: {route}')
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_cost += route_distance
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No solution found.")