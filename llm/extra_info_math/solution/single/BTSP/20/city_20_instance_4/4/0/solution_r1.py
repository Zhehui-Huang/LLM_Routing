from ortops.constraint_solver import routing_enums_pb2
from ortops.constraint_solver import pywrapcp
import math

# Coordinates of each city
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), 
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), 
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Number of cities
num_cities = len(coordinates)

# Euclidean distance calculation
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create the distance matrix
distance_matrix = []
for from_index in range(num_cities):
    distance_row = []
    for to_index in range(num_cities):
        distance_row.append(calculate_distance(coordinates[from_index], coordinates[to_index]))
    distance_matrix.append(distance_row)

# Create the routing index manager and model
manager = pywrapcp.RoutingIndexManager(num_cities, 1, 0)
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def transit_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(transit_cb)

# Set arc costs for all vehicles
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Solve the problem
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_sol_str = routing_enums_pb2.FirstBindingStrategy.PATH_CHEAPEST_ARC
solution = routing.SolveWithParameters(search_parameters)

# Extract the solution
route_dist = 0
route_max_dist = 0
route = []
index = routing.Start(0)
while not routing.IsEnd(index):
    prev_index = index
    index = solution.Value(routing.NextVar(index))
    route.append(manager.IndexToNode(prev_index))
    if not routing.IsEnd(index):
        dist = distance_matrix[manager.IndexToNode(prev_index)][manager.IndexToNode(index)]
        route_dist += dist
        route_max_dist = max(route_max_dist, dist)
route.append(route[0])  # complete the circuit

# Print the solution
print("Tour:", route)
print(f"Total travel cost: {route_dist}")
print(f"Maximum distance between consecutive cities: {route_max_dist}")