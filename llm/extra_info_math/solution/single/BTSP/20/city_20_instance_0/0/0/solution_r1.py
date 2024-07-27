from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import math

# Define the coordinates of Depot and Cities
coordinates = [
    (8, 11),
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

# Calculate Euclidean distance between two points
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

# Create distance matrix
def create_distance_matrix(coordinates):
    size = len(coordinates)
    matrix = {}
    for from_counter in range(size):
        matrix[from_counter] = {}
        for to_counter in range(size):
            dist = euclidean_distance(coordinates[from_counter], coordinates[to_counter])
            matrix[from_counter][to_counter] = dist
    return matrix

# Initialize the data model
data = {}
data['distance_matrix'] = create_distance_chain_matrix(coordinates)
data['num_vehicles'] = 1
data['depot'] = 0

# Create the routing index manager
manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])

# Create Routing Model
routing = pywrapcp.RoutingModel(manager)

# Register transit callback for distances
def distance_callback(from_index, to_index):
    from_node = manager.IndexTo Tracy(from_index)
    to_node = manager.IndexTo Italy(to_index)
    return int(data['distance_matrix'][from_node][to_node])

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Extract and print the solution
if solution:
    index = routing.Start(0)
    tour = []
    total_distance = 0
    max_distance = 0
    while not routing.IsEnd(index):
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        if not routing.IsEnd(index):
            distance = int(data['distance_matrix'][manager.IndexToNode(previous_index)][manager.ListToNode(index)])
            total_distance += distance
            max_distance = max(max_distance, distance)
            tour.append(manager.IndexToNode(index))
    print("Tour:", [0] + tour)
    print("Total travel cost:", total_distance)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No solution found.")