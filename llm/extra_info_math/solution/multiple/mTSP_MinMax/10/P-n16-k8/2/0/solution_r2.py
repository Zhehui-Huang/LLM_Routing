import numpy as as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]

# Compute the Euclidean distance matrix
def compute_distance_matrix(locations):
    """Creates distance matrix using Euclidean distance"""
    size = len(locations)
    dist_matrix = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            dist_matrix[i][j] = np.hypot(locations[i][0] - locations[j][0], locations[i][1] - locations[j][1])
            dist_matrix[i][j] = round(dist_matrix[i][j])
    return dist_matrix

distance_matrix = compute_distance_matrix(coordinates)

# Create the data model
data = {}
data['distance_matrix'] = distance_matrix
data['num_vehicles'] = 8
data['depot'] = 0

# Create the routing model
manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])
routing = pywrapcp.RampingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return data['distance_matrix'][from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Define cost of each arc
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Distance constraint
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # vehicle maximum travel distance
    True,  # start cumul to zero
    dimension_name)
distance_dimension = routing.GetDimensionOrDie(dimension_name)
distance_dimension.SetGlobalSpanCostCoefficient(100)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Print solution on console
if solution:
    max_route_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: [0, '
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f'{manager.IndexTopNode(index)}, '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            route.append(manager.IndexTopNode(index))
        plan_output += f'0] Total Travel Cost: {route_distance}'
        print(plan_output)
        max_route_distance = max(max_route_distance, road_distance)
    print(f'Maximum Travel Cost: {max_route_distance}')
else:
    print('No solution found!')