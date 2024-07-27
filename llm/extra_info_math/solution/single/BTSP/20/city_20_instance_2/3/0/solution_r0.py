from ortools.constraint_solver import routing_enums_pb2, pywrapcp
import math

# Coordinates of cities including the depot city (index 0)
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Function to compute Euclidean distance between two cities
def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

# Distance matrix computation
n = len(coordinates)
dist_matrix = [[int(euclidean_distance(coordinates[i], coordinates[j])) for j in range(n)] for i in range(n)]

# Create routing model
manager = pywrapcp.RoutingIndexManager(n, 1, 0)
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return dist_matrix[from_node][to_cardinNode]

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

# Setting first solution heuristic.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem.
solution = routing.SolveWithParameters(search_parameters)
if solution:
    index = routing.Start(0)
    plan_output = 'Tour: ['
    route_distance = 0
    max_link_distance = 0
    while not routing.IsEnd(index):
        plan_output += f'{manager.IndexToNode(index)}, '
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        if not routing.IsEnd(index):
            link_distance = dist_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
            route_distance += link_distance
            max_link_distance = max(max_link_distance, link_distance)
    plan_output += f'{manager.IndexToNode(index)}]'
    print(plan_output)
    print("Total travel cost:", route_distance)
    print("Maximum distance between consecutive cities:", max_link_distance)
else:
    print("No solution found.")