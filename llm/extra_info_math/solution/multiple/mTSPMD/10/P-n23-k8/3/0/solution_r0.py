import numpy as np
from scipy.spatial import distance_matrix
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define the cities' coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Calculate the distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Number of robots and respective depots
num_robots = 8
depot_locations = list(range(num_robots))  # Depots are the first 8 locations in the coordinates list

# Create the routing model
manager = pywrapcp.RoutingIndexManager(len(coordinates), num_robots, depot_locations)
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return dist_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Distance constraint
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # maximum distance per vehicle
    True,  # start cumul to zero
    dimension_name)
distance_dimension = routing.GetDimensionOrDie(dimension_name)
distance_dimension.SetGlobalSpanCostCoefficient(100)

# Solving the problem
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
solution = routing.SolveWithParameters(search_parameters)

# Print solution on console.
total_cost = 0
for vehicle_id in range(num_robots):
    index = routing.Start(vehicle_id)
    plan_output = 'Robot {} Tour: '.format(vehicle_id)
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
    plan_output += ' {}'.format(manager.IndexToNode(index))
    print(plan_output)
    print('Robot {} Total Travel Cost: {}'.format(vehicle_id, route_distance))
    total_cost += route_distance
print('Overall Total Travel Cost: {}'.format(total_cost))