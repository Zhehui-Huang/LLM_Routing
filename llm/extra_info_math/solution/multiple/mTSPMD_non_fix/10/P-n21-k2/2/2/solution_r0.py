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
    data['depots'] = [0, 1]
    return data

def euclidean_distance(position_1, position_2):
    return math.hypot(position_1[0] - position_2[0], position_1[1] - position_2[1])

def create_distance_callback(data):
    distances = {}
    for from_counter, from_node in enumerate(data['locations']):
        distances[from_counter] = {}
        for to_counter, to_node in enumerate(data['locations']):
            distances[from_counter][to_counter] = euclidean_distance(from_node, to_node)
    return distances

def add_distance_dimension(routing, distance_callback):
    routing.SetArcCostEvaluatorOfAllVehicles(distance_callback)

def main():
    data = create_data_model()
    distance_matrix = create_distance_callback(data)
    routing = pywrapcp.RoutingModel(len(data['locations']), data['num_vehicles'], data['depots'])
    transit_callback_index = routing.RegisterTransitCallback(lambda from_index, to_index: distance_matrix[routing.IndexToNode(from_index)][routing.IndexToNode(to_index)])
    add_distance_dimension(routing, transit_callback_index)
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    solution = routing.SolveWithParameters(search_parameters)
    total_distance = 0
    routes = []
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        route_distance = 0
        route = []
        while not routing.IsEnd(index):
            route.append(routing.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += distance_matrix[routing.IndexToNode(previous_index)][routing.IndexToNode(index)]
        route.append(routing.IndexToNode(index))
        print(f'Robot {vehicle_id} Tour: {route}')
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        routes.append(route)
        total_distance += route_distance
    print('Overall Total Travel Cost:', total_distance)

if __name__ == '__main__':
    main()