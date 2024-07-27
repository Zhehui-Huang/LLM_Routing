from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Distance calculation using Euclidean distance
def compute_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create the distance matrix
def create_distance_matrix(coordinates):
    size = len(coordinates)
    dist_matrix = {}
    for from_counter in range(size):
        dist_matrix[from_counter] = {}
        for to_counter in range(size):
            dist_matrix[from_counter][to_counter] = compute_euclidean_distance(
                coordinates[from_counter], coordinates[to_counter]
            )
    return dist_matrix

# Main solve function using Google OR-Tools
def solve_vrp(coordinates, num_robots, depot):
    # Create the routing index manager
    manager = pywrapcp.RoutingIndexManager(len(coordinates), num_robots, depot)

    # Create Routing Model
    routing = pywrapcp.RoutingModel(manager)

    # Distance callback
    distance_matrix = create_distance_matrix(coordinates)
    transit_callback_index = routing.RegisterTransitCallback(
        lambda from_index, to_index: distance_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]
    )

    # Cost of each arc
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic (cheapest addition).
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)
    return manager, routing, solution

# Output the solution.
def print_solution(manager, routing, solution):
    total_cost = 0
    for vehicle_id in range(manager.GetNumberOfVehicles()):
        index = routing.Start(vehicle_id)
        plan_output = 'Robot {} Tour: '.format(vehicle_id)
        route_distance = 0
        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            if not routing.IsEnd(index):
                route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route.append(manager.IndexToNode(index))  # Add the depot end
        plan_output += str(route)
        plan_output += ' Total Travel Cost: {}'.format(route_boundary)
        print(plan_output)
        total_cost += route_distance
    print('Overall Total Travel Cost: {}'.format(total_cost))

# Number of robots and the depot initialization (all start at city 0)
num_robots = 8
depot = 0

# Solve the problem
manager, routing, solution = solve_vrp(coordinates, num_robots, depot)

# Output the solution
if solution:
    print_solution(manager, routing, solution)
else:
    print("No solution found!")