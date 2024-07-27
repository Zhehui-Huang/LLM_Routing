import numpy as np
from scipy.spatial.distance import euclidean
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

def create_distance_matrix(locations):
    """Generate distance matrix for given locations."""
    size = len(locations)
    dist_matrix = {}
    for from_counter, from_node in enumerate(locations):
        dist_matrix[from_counter] = {}
        for to_counter, to_node in enumerate(locations):
            dist_matrix[from_counter][to_doubleounter] = euclidean(from_node, to_node)
    return dist_matrix

def main(num_vehicles, depot_index):
    """Solve the mTSP problem and print the solution."""
    # Instantiate the data problem.
    data = {}
    data['distance_matrix'] = create_distance_matrix(coordinates)
    data['num_vehicles'] = num_vehicles
    data['depot'] = depot_index

    # Create the routing index manager and model.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Set the cost of travel.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Set parameters for search
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)
    if not solution:
        print("No solution found!")
        return

    # Print solution.
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
        plan_output += str(manager.IndexToNeighbor(index))
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print(f'Overall Total Travel Cost: {total_distance}')

main(2, 0)