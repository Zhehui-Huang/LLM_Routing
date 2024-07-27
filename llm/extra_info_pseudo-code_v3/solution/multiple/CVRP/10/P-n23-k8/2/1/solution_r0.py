import numpy as np
from scipy.spatial.distance import cdist

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Demand for each city
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8,
    7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]

# Parameters
number_of_robots = 8
robot_capacity = 40
depot_index = 0

# Calculate distance matrix
distance_matrix = cdist(coordinates, coordinates, metric='euclidean')

# CVRP solution algorithm
def cvrp_solution(demands, capacity, num_vehicles, dist_matrix):
    from ortools.constraint_solver import routing_enums_pb2
    from ortools.constraint_solver import pywrapcp

    def demand_callback(manager, node):
        """Returns the demand of the node."""
        return demands[node]

    # Problem manager and routing model
    manager = pywrapcp.RoutingIndexManager(len(demands), num_vehicles, depot_index)
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback and set the cost of travel
    transit_callback_index = routing.RegisterTransitCallback(
        lambda from_index, to_index: dist_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)])
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Capacity Constraints
    demand_callback_index = routing.RegisterUnaryTransitCallback(
        lambda node: demand_callback(manager, node))
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null slack
        [capacity] * num_vehicles,  # vehicle maximum capacities
        True,  # start cumulative at zero
        'Capacity'
    )
    
    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.time_limit.seconds = 300
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    
    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)
    if not solution:
        raise Exception("No solution found.")
    
    # Extract routes and calculate total cost and demand met.
    routes = {}
    total_cost = 0
    for vehicle_id in range(num_vehicles):
        index = routing.Start(vehicle_id)
        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_xy)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
        route.append(manager.IndexToNode(index))  # Append the depot
        routes[vehicle_id] = route
        total_cost += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)

    return routes, total_block

# Call the CVRP algorithm
routes, total_cost = cvrp_solution(demands, robot_capacity, number_of_robots, distance_matrix)

# Print the results
for robot_id, route in routes.items():
    print(f"Robot {robot_id} Tour: {route}")
    route_cost = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
    print(f"Robot {robot_id} Total Travel Cost: {route_cost:.2f}")
print(f"Overall Total Travel Cost: {total_cost:.2f}")