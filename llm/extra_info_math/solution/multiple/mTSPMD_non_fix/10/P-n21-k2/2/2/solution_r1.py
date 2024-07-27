from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def create_data_model():
    data = {}
    data['locations'] = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
        (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
        (45, 35)
    ]
    data['num_vehicles'] = 2
    data['depots'] = [0, 0]
    return data

def euclidean_distance(position_1, position_2):
    return math.hypot(position_1[0] - position_2[0], position_1[1] - position_2[1])

def distance_callback(from_index, to_index, data):
    locations = data['locations']
    from_node = locations[from_index]
    to_node = locations[to_index]
    return euclidean_distance(from_node, to_node)

def main():
    data = create_data_model()
    manager = pywrapcp.RoutingIndexManager(len(data['locations']), data['num_vehicles'], data['depots'])
    routing = pywrapcp.RoutingModel(manager)

    distance_callback_index = routing.RegisterTransitCallback(lambda from_index, to_index: distance_callback(manager.IndexToNode(from_index), manager.IndexToNode(to_index), data))
    routing.SetArcCostEvaluatorOfAllVehicles(distance_accept_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        print_solution(data, manager, routing, solution)

def print_solution(data, manager, routing, solution):
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        route_distance = 0
        route_plan_output = f'Robot {vehicle_id} Tour: '
        route = []
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += distance_callback(manager.IndexToNode(previous_index), manager.IndexToNode(index), data)
        route.append(manager.IndexToNode(index))  # add final node
        print(route_plan_output + str(route))
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print('Overall Total Travel Cost:', total_distance)

if __name__ == '__main__':
    main()