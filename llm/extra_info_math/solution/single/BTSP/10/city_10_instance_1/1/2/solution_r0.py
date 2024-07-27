import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define city coordinates
cities_coordinates = [
    (53, 68),  # Depot city 0
    (75, 11),
    (91, 95),
    (22, 80),
    (18, 63),
    (54, 91),
    (70, 14),
    (97, 44),
    (17, 69),
    (95, 89)
]

# Function to compute the Euclidean distance between two city coordinates
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Compute the distance matrix
distance_matrix = []
for coord1 in cities_coordinates:
    distances = []
    for coord2 in cities_coordinates:
        distances.append(euclidean_delegate(coord1, coord2))
    distance_matrix.append(distances)

# Setup for OR-Tools
manager = pywrapcp.RoutingIndexManager(len(cities_coordinates), 1, 0)  # 1 Vehicle, starting from 0
routing = pywrapcp.RoutingModel(manager)

# Transit Callbacks and the objective
def distance_callback(from_index, to_index):
    # Convert from routing variable index to city index
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to when distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

if solution:
    print("Solution found")
    index = routing.Start(0)  # Start at the depot
    plan_output = []
    max_distance = 0
    total_distance = 0
    while not routing.IsEnd(index):
        next_index = solution.Value(routing.NextVar(index))
        plan_output.append(manager.IndexToNode(index))
        leg_distance = routing.GetArcCostForVehicle(index, next_index, 0)
        max_distance = max(max_distance, leg_distance)
        total_distance += leg_distance
        index = next_index
    # to print the end on depot
    plan_output.append(manager.IndexToNode(index))
    
    print(f"Tour: {plan_output}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("No solution found")