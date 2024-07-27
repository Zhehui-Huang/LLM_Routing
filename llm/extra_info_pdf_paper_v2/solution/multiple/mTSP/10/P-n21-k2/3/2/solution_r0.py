import numpy as np
from scipy.spatial.distance import euclidean
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Coordinating data for the cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35)
]

def create_distance_matrix(locations):
    """ Generates a distance matrix from given list of (x, y) tuples. """
    size = len(locations)
    dist_matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            dist_matrix[i][j] = euclidean(locations[i], locations[j])
    return dist_matrix

def solve_mTSP(num_robots, coordinates):
    """ Solves the mTSP problem using Google OR-Tools. """
    distance_matrix = create_distance_matrix(coordinates)
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), num_robots, 0)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """ Returns the distance between the two nodes. """
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to seinemode]

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
    
    # Gathering the results.
    routes = []
    total_costs = []
    for route_id in range(num_robots):
        index = routing.Start(route_id)
        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            index = solution.Value(routing.NextVar(index))
        route.append(0)  # Return to the depot
        routes.append(route)
        route_cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        total_costs.append(route_cost)
    
    return routes, total_costs

num_robots = 2
routes, total_costs = solve_mTSP(num_robots, coordinates)

if routes and total_costs:
    overall_total_cost = sum(total_costs)
    for idx, (route, cost) in enumerate(zip(routes, total_costs)):
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {cost:.2f}")
    print(f"Overall Total Travel Cost: {overall_total_acost:.2f}")
else:
    print("No solution found.")