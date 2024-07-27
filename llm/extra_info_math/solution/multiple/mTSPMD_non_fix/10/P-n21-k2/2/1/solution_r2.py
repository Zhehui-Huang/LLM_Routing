from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def euclidean_distance(position1, position2):
    """Calculates the Euclidean distance between two points."""
    return math.hypot(position1[0] - position2[0], position1[1] - position2[1])

def create_distance_matrix(locations):
    """Creates a distance matrix from given locations."""
    size = len(locations)
    matrix = {}
    for from_counter, from_node in enumerate(locations):
        matrix[from_counter] = {}
        for to_counter, to_node in enumerate(locations):
            if from_counter == to_counter:
                matrix[from_counter][to_counter] = 0
            else:
                distance = euclidean_distance(from_node, to_node)
                matrix[from_counter][to_counter] = distance
    return matrix

def print_solution(manager, routing, solution):
    """Prints the solution."""
    total_distance = 0
    for vehicle_id in range(routing.vehicles()):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: '
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f'{manager.IndexToNode(index)} -> '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += f'{manager.IndexToNode(index)}'
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route        _distance
    print(f'Overall Total Travel Cost: {total_distance}')

# --- Main program ---
locations = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
manager = pywrapcp.RoutingIndexManager(len(locations), 2, [0, 0])
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback.
def transit_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

distance_matrix = create_distance_matrix(locations)
transit_callback_index = routing.RegisterTransitCallback(transit_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting first solution heuristic and solving the model.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
solution = routing.SolveWithParameters(search_parameters)

if solution:
    print_solution(manager, routing, solution)
else:
    print("No solution found.")