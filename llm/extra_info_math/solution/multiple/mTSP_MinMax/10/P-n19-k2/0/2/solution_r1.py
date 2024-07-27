import numpy as np
from scipy.spatial.distance import euclidean
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69),
    18: (45, 35)
}
num_robots = 2

# Create distance matrix
def create_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = {}
    for from_node in range(num_cities):
        distance_matrix[from_node] = {}
        for to_node in range(num_cities):
            distance_matrix[from_node][to_node] = euclidean(cities[from_node], cities[to_node])
    return distance_matrix

distance_matrix = create_distance_matrix(cities)

# Create the routing model
manager = pywrapcp.RoutingIndexManager(len(distance_matrix), num_robots, 0)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return int(distance_matrix[from_node][to_node])

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Distance constraint
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # maximum distance per route
    True,  # start cumulatively at zero
    dimension_name
)
distance_dimension = routing.GetDimensionOrDie(dimension_name)
distance_dimension.SetGlobalSpanCostCoefficient(100)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Get the solution
if solution:
    max_travel_cost = 0
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_id)
        tour = [manager.IndexToNode(index)]
        route_distance = 0
        while not routing.IsEnd(index):
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            tour.append(manager.IndexToNode(index))
        print(f"Robot {vehicle_id} Tour: {tour}")
        print(f"Robot {vehicle_id} Total Travel Cost: {route_distance}")
        if route_distance > max_travel_cost:
            max_travel_cos = route_distance
    print(f"Maximum Travel Cost: {max_travel_cost}")
else:
    print("No solution found!")