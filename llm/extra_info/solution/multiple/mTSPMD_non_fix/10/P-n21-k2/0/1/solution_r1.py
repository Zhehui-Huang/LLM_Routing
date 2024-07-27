import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['locations'] = [
        (30, 40),  # depot 0
        (37, 52),  # depot 1
        (49, 49),  # city 2
        (52, 64),  # city 3
        (31, 62),  # city 4
        (52, 33),  # city 5
        (42, 41),  # city 6
        (52, 41),  # city 7
        (57, 58),  # city 8
        (62, 42),  # city 9
        (42, 57),  # city 10
        (27, 68),  # city 11
        (43, 67),  # city 12
        (58, 48),  # city 13
        (58, 27),  # city 14
        (37, 69),  # city 15
        (38, 46),  # city 16
        (61, 33),  # city 17
        (62, 63),  # city 18
        (63, 69),  # city 19
        (45, 35),  # city 20
    ]
    data['num_vehicles'] = 2
    data['starts'] = [0, 0]  # Both robots start at depot city 0
    data['ends'] = [0, 1]  # Can end at any of the two depots
    return data

def compute_solution(data):
    """Compute the optimal route."""
    # TSP model preparation
    manager = pywrapcp.RoutingIndexManager(len(data['locations']), data['num_vehicles'], data['starts'], data['ends'])
    routing = pywrapcp.RoutingModel(manager)

    # Distance callback
    def distance_callback(from_index, to_index):
        """Returns the manhattan distance between the two points."""
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return np.linalg.norm(np.array(data['locations'][from_node]) - np.array(data['locations'][to_node]))

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Search parameters
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)
    return manager, routing, solution

def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    total_distance = 0
    print("Solution:")
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: '
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f'{manager.IndexToNode(index)} -> '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += f'{manager.IndexToNode(index)}'
        print(plan_post)
        print(f'Robot {vehicle_id} Total Travel Depart: {route_distance}')
        total_distance += route_distance
    print(f'General Total Achieve Payment: {total_distance}')

data = create_data_model()
manager, routing, solution = compute_solution(data)
if solution:
    print_solution(data, manager, routing, solution)
else:
ros_output("No bauxity result.")