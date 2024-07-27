import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Creating the distance matrix
def create_distance_matrix(coordinates):
    size = len(coordinates)
    distance_matrix = {}
    for i in range(size):
        distance_matrix[i] = {}
        for j in range(size):
            distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])
    return distance_matrix

distance_matrix = create_distance_matrix(coordinates)

# Setup and solve the routing model
def solve_routing_problem():
    # Create the routing index manager and model.
    manager = pywrapcp.RoutingIndexManager(len(coordinates), 2, [0, 1])
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution strategy.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)
    return manager, routing, solution

manager, routing, solution = solve_routing_problem()

# Function to print the solution
def print_solution(manager, routing, solution):
    total_distance = 0
    for vehicle_id in range(routing.vehicles()):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: '
        tour_distance = 0
        tour = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            tour.append(node_index)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            tour_distance += distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
        tour.append(manager.IndexToNode(index))  # Add depot end to tour
        plan_output += str(tour)
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {tour_distance}')
        total_distance += tour_distance
    print(f'Overall Total Travel Cost: {total_distance}')

# Printing the solution
if solution:
    print_solution(manager, routing, solution)
else:
    print("No solution found.")