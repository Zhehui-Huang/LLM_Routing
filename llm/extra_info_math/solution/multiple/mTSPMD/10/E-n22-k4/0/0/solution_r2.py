import numpy as np
from scipy.spatial import distance
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define city coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Function to create distance matrix
def create_distance_matrix(coords):
    return np.round(distance.cdist(coords, coords, 'euclidean')).astype(int)

# Create the data model for the problem
def create_data_model():
    data = {}
    data['distance_matrix'] = create_distance_matrix(coordinates)
    data['num_vehicles'] = 4
    data['start_locations'] = [0, 1, 2, 3]
    data['end_locations'] = [0, 1, 2, 3]
    return data

def solve_vrp():
    data = create_data_model()
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'],
                                           data['start_locations'],
                                           data['end_locations'])
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
        total_distance = 0
        for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)
            plan_output = f'Robot {vehicle_id} Tour: '
            route_distance = 0
            while not routing.IsEnd(index):
                plan_output += str(manager.IndexToNode(index)) + ' -> '
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            plan_output += str(manager.IndexToNode(index))
            print(plan_output)
            print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
            total_distance += route_distance
        print(f'Overall Total Travel Cost: {total, distance}')
    else:
        print('No solution found!')

# Execute the VRP solver
solve_vrp()