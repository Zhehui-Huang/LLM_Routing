import numpy as np
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

def create_data_model():
    data = {
        'coordinates': [
            (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
            (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
            (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
            (164, 193), (129, 189), (155, 185), (139, 182)
        ],
        'num_vehicles': 4,
        'depot': 0
    }
    return data

def calculate_distance(coord1, coord2):
    return np.linalg.norm(np.array(coord1) - np.array(coord2))

def create_distance_matrix(coordinates):
    size = len(coordinates)
    distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(size)] for i in range(size)]
    return distance_matrix

def print_solution(data, manager, routing, solution):
    total_distance = 0
    max_route_distance = 0
    routes = []
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        route_distance = 0
        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route.append(data['depot'])
        route_distance += routing.GetArcCostForVehicle(previous_index, routing.End(vehicle_id), vehicle_id)
        routes.append(route)
        print(f'Robot {vehicle_id} Tour: {route}')
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
        if route_distance > max_route_distance:
            max_route_distance = route_distance
    print(f'Maximum Travel Cost: {max_route_distance}')
    return routes, max_route_distance

def main():
    data = create_data_model()
    data['distance_matrix'] = create_distance_matrix(data['coordinates'])
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)
    transit_callback_index = routing.RegisterTransitCallback(lambda from_index, to_index: int(
        data['distance_matrix'][manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]))
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    dimension_name = 'Distance'
    routing.AddDimension(transit_callback_index, 0, 3000, True, dimension_name)
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        print_solution(data, manager, routing, solution)
    else:
        print("No solution found.")

if __name__ == '__main__':
    main()