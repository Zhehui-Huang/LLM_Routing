from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Define the coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), 
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), 
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Number of cities
num_cities = len(coordinates)

# Calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Calculate the distance matrix
distance_matrix = []
for from_index in range(num_cities):
    distance_row = []
    for to_index in range(num_cities):
        distance_row.append(calculate_distance(coordinates[from_index], coordinates[to_index]))
    distance_matrix.append(distance_row)

# Create the routing model
manager = pywrapcp.RoutingIndexManager(num_cities, 1, 0)
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def transit_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(transit_callback)

# Set the arc costs for all vehicles
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Solve the problem
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

solution = routing.SolveWithParameters(search_parameters)

# Gather the results if a solution was found
if solution:
    route = []
    index = routing.Start(0)
    route_distance = 0
    max_distance = 0
    while not routing.IsEnd(index):
        route.append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        if not routing.IsEnd(index):
            segment_distance = distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
            route_distance += segment_loop_distance
            if segment_distance > max_distance:
                max_distance = segment_distance
    route.append(manager.IndexToNode(index)) # Add the depot to end the route

    print("Tour:", route)
    print("Total travel cost:", round(route_distance, 2))
    print("Maximum distance between consecutive cities:", round(max_distance, 2))
else:
    print("No solution found.")