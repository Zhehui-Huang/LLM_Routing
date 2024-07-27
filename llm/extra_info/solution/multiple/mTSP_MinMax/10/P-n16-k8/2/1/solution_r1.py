import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Coordinate data for the cities including the depot city
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), 
    (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Calculate Euclidean distance matrix
def euclidean_distance(coord1, coord2):
    return int(np.hypot(coord1[0] - coord2[0], coord1[1] - coord2[1]) + 0.5)

distance_matrix = [
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))]
    for i in range(len(coordinates))
]

# Number of Robots
num_robots = 8

# Create the routing model.
manager = pywrapcp.RoutingIndexManager(len(coordinates), num_robots, 0)
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback.
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Set the cost of travel
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Distance constraint
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # maximum distance per vehicle
    True,  # start cumul to zero
    dimension_name)

# Set the search parameters.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem.
solution = routing.SolveWithParameters(search_parameters)

# Extract and print the tours for each robot and the corresponding travel costs.
if solution:
    max_route_distance = 0
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_id)
        tour = []
        route_distance = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            tour.append(node_index)
            next_index = solution.Value(routing.NextVar(index))
            route_distance += distance_matrix[node_index][manager.IndexToNode(next_index)]
            index = next_index
        tour.append(manager.IndexToNode(index))  # Append the depot city
        print(f"Robot {vehicle_id} Tour: {tour}")
        print(f"Robot {vehicle_id} Total Travel Cost: {route_distance}")
        max_route_distance = max(max_route_distance, route_distance)
    print(f"Maximum Travel Cost: {max_route_distance}")
else:
    print("No solution found.")