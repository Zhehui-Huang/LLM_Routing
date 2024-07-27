from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import math

# City coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.hypot(coord1[0] - coord2[0], coord1[1] - coord2[1])

# Distance matrix
num_nodes = len(coordinates)
distance_matrix = [
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_nodes)]
    for i in range(num_nodes)
]

# Create routing model
manager = pywrapcp.RoutingIndexManager(num_nodes, 1, 0)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_id]

transit_callback_index = routing.RegisterTransitCallback(distance_p)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Find solution using the solver
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

solution = routing.SolveWithParameters(search_parameters)

# Extract tour
index = routing.Start(0)
tour = []
while not routing.IsEnd(index):
    tour.append(manager.IndexToNode(index))
    prev_index = index
    index = solution.Value(routing.NextVar(index))
tour.append(0)  # complete the tour by returning to the starting point

# Compute total cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(1, len(tour)):
    dist = distance_matrix[tour[i-1]][tour[i]]
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")