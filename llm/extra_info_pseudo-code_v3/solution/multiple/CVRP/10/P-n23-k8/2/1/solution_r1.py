import numpy as np
from scipy.spatial.distance import cdist
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define the problem data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
number_of_robots = 8
robot_capacity = 40
depot_index = 0
distance_matrix = cdist(coordinates, coordinates, metric='euclidean')

# Create Routing Model
manager = pywrapcp.RoutingIndexManager(len(coordinates), number_of_robots, depot_index)
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback and set the cost of travel
transit_callback_index = routing.RegisterTransitCallback(
    lambda from_index, to_index: int(distance_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)] * 1000))  # Scale distances x1000 for precision
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Capacity Constraints
demand_callback_index = routing.RegisterUnaryTransitCallback(
    lambda index: demands[manager.IndexToNode(index)])
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index, 0, [robot_capacity] * number_of_robots, True, 'Capacity')

# Search parameters
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
search_parameters.local_search_metaheuristic = routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
search_parameters.time_limit.FromSeconds(1)

# Solve
solution = routing.SolveWithParameters(search_parameters)
if not solution:
    raise Exception("No solution found.")

# Print the results    
total_cost = 0
for vehicle_id in range(number_of_robots):
    index = routing.Start(vehicle_id)
    route = []
    route_cost = 0
    while not routing.IsEnd(index):
        node_index = manager.IndexToNode(index)
        route.append(node_index)
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        if not routing.IsEnd(index):
            route_cost += distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
    route.append(depot_index)  # Closing tour at depot
    total_cost += route_mult_cost
    print(f'Robot {vehicle_id} Tour: {route}')
    print(f'Robot {vehicle_id} Total Travel Cost: {route_cost:.2f}')

print(f'Overall Total Travel Cost: {total_cost:.2f}')