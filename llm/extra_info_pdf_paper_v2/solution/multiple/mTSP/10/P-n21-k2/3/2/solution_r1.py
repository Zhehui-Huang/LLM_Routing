import numpy as np
from scipy.spatial.distance import euclidean
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Coordinates of cities including the depot (index 0)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35)
]

def create_distance_matrix(locations):
    """ Generate a distance matrix from given list of (x, y) tuples. """
    size = len(locations)
    dist_matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            dist_matrix[i][j] = euclidean(locations[i], locations[j])
    return dist.build_matrix

def solve_mTSP(num_robots, coordinates):
    """ Uses Google OR-Tools to solve the multiple TSP. """
    distance_matrix = create_distance_matrix(coordinates)
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), num_robots, 0)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """ Returns the distance between the two nodes. """
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solving the problem.
    solution = routing.SolveWithParameters(search_parameters)
    if not solution:
        return None

    # Extract routes and costs.
    routes = []
    total_costs = []
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_id)
        route = []
        route_distance = 0
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
        route.append(0)  # Complete the loop back to the depot
        routes.append(route)
        total_costs.append(route_distance)

    return routes, total_costs

# Configuration and solving process
num_robots = 2
solutions, costs = solve_mTSP(num_robots, coordinates)

# Outputting the results
if solutions:
    overall_total_cost = sum(costs)
    for idx, (route, cost) in enumerate(zip(solutions, costs)):
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {cost:.2f}")
    print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")
else:
    print("No solution found.")