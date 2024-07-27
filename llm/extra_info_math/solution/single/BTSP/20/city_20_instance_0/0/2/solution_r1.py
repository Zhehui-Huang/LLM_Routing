import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates
cities = [
    (8, 11),  # Depot city 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 73), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Calculate Euclidean distances matrix
def compute_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

distance_matrix = [
    [int(compute_euclidean_distance(cities[i], cities[j])) for j in range(len(cities))]
    for i in range(len(cities))
]

# Setup distance matrix and solver
manager = pywrapcp.RoutingIndexManager(len(cities), 1, 0)
routing = pywrapcp.RoutingModel(manager)

def distance_callback(from_index, to_index):
    """Returns the manhattan distance between the two nodes."""
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Distance dimension.
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    10000,  # maximum distance per vehicle
    True,  # start cumul to zero
    dimension_name)

distance_dimension = routing.GetDimensionOrDie(dimension_name)
distance_dimension.SetGlobalSpanCostCoefficient(100)

# Setting first solution heuristic.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
search_parameters.local_search_metaheuristic = (
    routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
search_parameters.time_limit.FromSeconds(1)

# Solve the problem.
solution = routing.SolveWithParameters(search_parameters)
if solution:
    print("Solution found.")
    # Solution distance.
    print('Objective: {}'.format(solution.ObjectiveValue()))
    # Inspect solution.
    index = routing.Start(0)
    plan_output = 'Route:\n'
    route_distance = 0
    distances = []
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
        distances.append(distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)])
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    max_distance = max(distances)
    print("Total travel cost: {}".format(route_distance))
    print("Maximum distance between consecutive cities: {}".format(max_distance))
else:
    print("No solution found.")