import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates
cities = [
    (8, 11),  # Depot city 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Distance calculation
def compute_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Distance matrix
n = len(cities)
distance_matrix = [[int(compute_euclidean_distance(cities[i], cities[j]))
                    for j in range(n)] for i in range(n)]

# OR-Tools model setup
manager = pywrapcp.RoutingIndexManager(n, 1, 0)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_ts_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Objective: Minimize the maximum distance between consecutive cities
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    10000,  # sufficiently large maximum distance to enforce min-max objective
    True,  # start cumul to zero
    dimension_name
)

distance_dimension = routing.GetDimensionOrDie(dimension_name)
distance_dimension.SetGlobalSpanCostCoefficient(100)

# Setting first solution heuristic (path-cheapest addition)
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve
solution = routing.SolveWithParameters(search_parameters)

# Extract tour
def get_routes(solution, routing, manager):
    index = routing.Start(0)
    route = []
    while not routing.IsEnd(index):
        route.append(manager.IndexToNode(index))
        index = solution.Value(routing.NextVar(index))
    route.append(0)  # complete the tour by returning to depot
    return route

if solution:
    tour = get_routes(solution, routing, manager)
    tour_distances = [distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1)]
    max_distance = max(tour_distances)
    total_distance = sum(tour_distances)
    print("Tour:", tour)
    print("Total travel cost:", total_distance)
    mdprint("Maximum distance between consecutive cities:", max_distance)
else:
    print("No solution found.")