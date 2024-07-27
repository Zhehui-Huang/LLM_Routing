import numpy as np
from scipy.spatial.distance import cdist
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define the coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), 
    (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]

# Compute distance matrix using Euclidean distance
distance_matrix = cdist(coordinates, coordinates, metric='euclidean')
distance_matrix = np.round(distance_matrix).astype(int)

# Solver setup
def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = distance_values 
    data['num_vehicles'] = 2
    data['starts'] = [0, 1]  # Start nodes for each vehicle
    data['ends'] = [0, 1]    # End nodes for each vehicle
    return data

def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    total_distance = 0
    print_results = {}
    for vehicle_id in range(data['num_vehicles']):
        index = solution.Start(vehicle_id)
        plan_output = []
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output.append(manager.IndexToNode(index))
        print(f'Robot {vehicle_id} Tour: {plan_output}')
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print('Overall Total Travel Cost:', total_distance)

def solve_tsp():
    """Entry point of the program."""
    data = create_data_model()
    manager = pywraptp.RoutingIndexManager(len(data['distance_matrix']), 
                                            data['num_vehicles'], 
                                            data['starts'], 
                                            data['ends'])
    routing = pywrapcp.RoutingModel(manager)
    transit_callback_index = routing.RegisterTransitCallback(
        lambda from_index, to_index: data['distance_matrix'][manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]
    )
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        print_solution(data, manager, routing, solution)

solve_tsp()