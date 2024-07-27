from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import math

# Define the coordinates of Depot and Cities
coordinates = [
    (8, 11),   # Depot City 0
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
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
            if from_counter == to_counter:
                matrix[from_counter][to_counter] = 0
            else:
                dist = int(euclidean_distance(coordinates[from_counter], coordinates[to_counter]))
                matrix[from_counter][to_counter] = dist
    return matrix

# Initialize the data model
data = {}
data['distance_matrix'] = create_distance_matrix(coordinates)
data['num_vehicles'] = 1
data['depot'] = 0

# Create the routing index manager
manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])

# Create Routing Model
routing = pywrapcp.RoutingModel(manager)

# Register transit callback for distances
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return data['distance_matrix'][from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Use Minimax Objective
objective = routing.RegisterMinMaxDistanceFromDepotObjective(transit_callback_index)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Extract the solution
def extract_solution(manager, routing, solution):
    index = routing.Start(0)
    tour = []
    total_distance = 0
    while not routing.IsEnd(index):
        tour.append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        if not routing.IsEnd(index):
            total_distance += data['distance_matrix'][tour[-1]][manager.IndexToNode(index)]
    tour.append(manager.IndexToNode(index))
    return tour, total_distance, max(data['distance_matrix'][tour[i]][tour[i+1]] for i in range(len(tour)-1))

if solution:
    tour, total_cost, max_distance = extract_solution(manager, routing, solution)
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("No solution found.")