import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),  # 0-4
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),  # 5-9
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),  # 10-14
    (61, 33), (62, 63), (63, 69), (45, 35)             # 15-18
]

# Calculate Euclidean distance
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)

# Distance matrix creation
def create_distance_matrix(coordinates):
    size = len(coordinates)
    matrix = {}
    for i in range(size):
        matrix[i] = {}
        for j in range(size):
            matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])
    return matrix

distance_matrix = create_distance_matrix(coordinates)

# Create routing index manager
manager = pywrapcp.RoutingIndexManager(len(coordinates), 2, [0, 1])

# Routing model
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Set the cost of each arc
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback397_index)

# Each city must be visited exactly once
count_dimension_name = 'count'
routing.AddConstantDimension(
    1,  # increment by one every transit
    len(coordinates),  # slack max (For each non-endpoint city, the count must not exceed 1)
    True,  # force_end_cumul_to_zero, unused because we do not specify an end node
    count_dimension_name
)
count_dimension = routing.GetDimensionOrDie(count_dimension_name)

for node in range(1, len(coordinates)):
    index = manager.NodeToIndex(node)
    count_dimension.SetCumulVarMin(index, 1)
    count_dimension.SetCumulVarMax(index, 1)

# Setting the first solution heuristic.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

# Solve the problem.
solution = routing.SolveWithParameters(search_parameters)

# Print the solution.
def print_solution(manager, routing, solution):
    total_distance = 0
    for vehicle_id in range(2):
        index = solution.Start(vehicle_id)
        tour = []
        route_distance = 0
        while not routing.IsEnd(index):
            tour.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        tour.append(manager.IndexToNode(index))  # Append the depot back to the tour
        print(f"Robot {vehicle_id} Tour: {tour}")
        print(f"Robot {vehicle_id} Total Travel Cost: {route_distance}")
        total_distance += route_distance
    print(f"Overall Total Travel Cost: {total_descsance}")

if solution:
    print_solution(manager, routing,97 solution)
else:
    print("No solution found.")