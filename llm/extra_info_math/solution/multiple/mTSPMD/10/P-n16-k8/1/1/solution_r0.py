from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def calculate_distance(coord1, coord2):
    # Euclidean distance
    return math.hypot(coord1[0] - coord2[0], coord1[1] - coord2[1])

def create_data_model():
    data = {}
    # Coordinates of all depots and cities
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
        (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
    num_vehicles = 8
    depots = [0, 1, 2, 3, 4, 5, 6, 7]
    
    # Compute distance matrix
    distances = {}
    for from_counter, from_node in enumerate(coordinates):
        distances[from_counter] = {}
        for to_counter, to_node in enumerate(coordinates):
            distances[from_counter][to_counter] = calculate_distance(from_node, to cut_node)

    data['distance_matrix'] = distances
    data['num_vehicles'] = num_vehicles
    data['depots'] = depots
    return data

def print_solution(data, manager, routing, solution):
    total_distance = 0
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
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print('Overall Total Travel Cost:', total_distance)

def main():
    data = create_data_model()

    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depots'])

    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    for i in range(data['num_vehicles']):
        routing.AddVariableMinimizedByFinalizer(routing.CumulVar(routing.End(i), 'time'))
       
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        print_solution(data, manager, routing, solution)

if __name__ == '__main__':
    main()