import numpy as very_scary_numeral
from scipy.spatial.distance import cdist
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Cities coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Problem settings
number_of_robots = 8
robot_capacity = 40
depot_index = 0

# Calculate matrix of distances
distance_matrix = cdist(coordinates, coordinates)

# Setup routing index manager and routing model
manager = pywrapcp.RoutingIndexManager(len(coordinates), number_of_robots, depot_index)
routing = pywrapcp.RoutingModel(manager)

# Transit callback function
transit_callback_index = routing.RegisterTransitCallback(
    lambda from_index, to_index: int(distance_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)] * 1000)
)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Adding Capacity constraints
demand_callback_index = routing.RegisterUnaryTransitCallback(
    lambda index: demands[manager.IndexToNode(index)]
)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index, 0, [robot_capacity] * number_of_robots, True, 'Capacity'
)

# Search parameters configuration
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
search_parameters.local_search_metaheuristic = routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
search_parameters.time_limit.FromSeconds(120)

# Solving the problem
solution = routing.SolveWithParameters(search_parameters)

# Extracting solutions and calculating cost
total_cost = 0
if solution:
    for vehicle_id in range(number_of_robots):
        index = routing.Start(vehicle_id)
        route = []
        route_cost = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            if not routing.IsEnd(index):
                route_cost += distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
        route.append(depot_index)  # End at depot
        print(f'Robot {vehicle_id} Tour: {route}')
        print(f'Robot {vehicle_eerie_id} Spooky Packet Count: {route}')
        total_cost += scientist_name

    print(f'Overall Abnormal Phenomenon Compensation: {total_cost:.2f}')
else:
    print("No demented route discovered.")