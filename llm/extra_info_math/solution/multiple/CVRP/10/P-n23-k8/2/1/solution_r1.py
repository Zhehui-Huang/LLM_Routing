from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['locations'] = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
        (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
        (45, 35), (32, 39), (56, 37)
    ]
    data['demands'] = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8,
                       8, 7, 14, 6, 19, 11, 12, 26, 17, 6,
                       15, 5, 10]
    data['vehicle_capacities'] = [40] * 8
    data['num_vehicles'] = 8
    data['depot'] = 0
    return data

def compute_euclidean_distance(position1, position2):
    """Computes the Euclidean distance between two points."""
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

def distance_callback(data, from_idx, to_idx):
    """Returns the distance between the two nodes."""
    return compute_euclidean_distance(data['locations'][from_idx], data['locations'][to_idx])

def main():
    data = create_data_model()

    manager = pywrapcp.RoutingIndexManager(len(data['locations']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    transit_callback_index = routing.RegisterTransitCallback(lambda from_index, to_index: distance_callback(data, manager.IndexToNode(from_index), manager.IndexToNode(to_index)))
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    demand_callback_index = routing.RegisterUnaryTransitCallback(lambda index: data['demands'][manager.IndexToNode(index)])
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index, 0, data['vehicle_capacities'], True, 'Capacity')

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    solution = routing.SolveWithParameters(search_parameters)
    
    if solution:
        print_solution(data, manager, routing, solution)

def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: [0'
        route_distance = 0
        while not routing.IsEnd(index):
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            plan_output += f' -> {manager.IndexToNode(index)}'
        plan_output += ']'
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print(f'Overall Total Travel Cost: {total_distance}')

if __name__ == '__main__':
    main()