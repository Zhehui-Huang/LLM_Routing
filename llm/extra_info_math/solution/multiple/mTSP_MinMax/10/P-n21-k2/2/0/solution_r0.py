from ortools.constraint_solver import pywrapcp, routing_enums_pb2

# Data Preparation - Coordinates for the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

def euclidean_distance(position1, position2):
    from math import sqrt
    return sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

# Distance matrix computation
n_cities = len(coordinates)
dist_matrix = {}
for from_counter in range(n_cities):
    dist_matrix[from_counter] = {}
    for to_counter in range(n_cities):
        if from_counter == to_counter:
            dist_matrix[from_counter][to_counter] = 0
        else:
            dist_matrix[from_counter][to_counter] = euclidean_distance(coordinates[from_counter], coordinates[to_counter])

# Using OR-Tools to setup the problem
manager = pywrapcp.RoutingIndexManager(n_cities, 2, 0)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return dist_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Distance constraint to minimize the maximum distance traveled among all vehicles
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

# Solving the problem.
solution = routing.SolveWithParameters(search_parameters)

# Retrieve solution if any and display it
max_route_distance = 0
for vehicle_id in range(2):
    index = routing.Start(vehicle_id)
    route_distance = 0
    route = []
    while not routing.IsEnd(index):
        node_index = manager.IndexToNode(index)
        route.append(node_index)
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
    route.append(manager.IndexToNode(index))  # End index is the depot

    print(f"Robot {vehicle setId} Tour: {route}")
    print(f"Robot {vehicle setId} Total Travel Cost: {route_distance}")
    max_route_distance = max(max_route_distance, route_distance)

print(f"Maximum Travel Cost: {max_route_distance}")