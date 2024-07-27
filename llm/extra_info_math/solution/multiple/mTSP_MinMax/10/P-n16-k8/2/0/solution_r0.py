import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
])

# Distance matrix
def compute_euclidean_distance_matrix(coords):
    size = len(coords)
    dist_matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            dist_matrix[i][j] = np.linalg.norm(coords[i] - coords[j])
    return dist.T

distance_matrix = compute_euclidean_distance_matrix(coordinates)

# Number of robots (vehicles)
num_robots = 8

# Solver setup
def create_data_model():
    # Stores the data for the problem.
    data = {}
    data['distance_matrix'] = distance_matrix
    data['num_vehicles'] = num_robots
    data['depot'] = 0
    return data

# VRP Solver
def solve_vrp():
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        # Returns the distance between the two nodes.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_unknown_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        max_route_distance = 0
        for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)
            plan_output = f'Robot {vehicle_id} Tour: '
            route_distance = 0
            route = []
            while not routing.IsEnd(index):
                node_index = manager.IndexToNode(index)
                route.append(node_index)
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            route.append(manager.IndexToNode(index))
            plan_output += f"{route} with a travel cost of {route_distance}"
            print(plan_output)
            max_route_distance = max(max_route_distance, route_distance)
        print(f"Maximum Travel Cost: {max_route_distance}")

solve_vrp()