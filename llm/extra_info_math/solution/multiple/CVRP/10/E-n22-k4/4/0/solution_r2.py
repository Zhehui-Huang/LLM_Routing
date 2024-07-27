from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def compute_euclidean_distance(coord1, coord2):
    return int(math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2))

def create_data_model():
    data = {}
    data['coordinates'] = [
        (145, 215),  # Depot
        (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
        (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217),
        (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), (164, 193),
        (129, 189), (155, 185), (139, 182)
    ]
    data['demands'] = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600,
                       1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
    data['vehicle_capacities'] = [6000] * 4
    data['num_vehicles'] = 4
    data['depot'] = 0
    number_of_locations = len(data['coordinates'])
    data['distance_matrix'] = [
        [compute_euclidean_distance(data['coordinates'][i], data['coordinates'][j]) for j in range(number_of_locations)] for i in range(number_of_locations)
    ]
    return data

def print_solution(data, manager, routing, solution):
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: '
        route_distance = 0
        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route.append(0)  # returning to depot
        plan_output += str(route)
        plan_output += f'\nRobot {vehicle_id} Total Travel Cost: {route_distance}'
        print(plan_output)
        total_distance += route_distance
    print(f'Overall Total Travel Cost: {total_distance}')

def main():
    data = create_data_model()

    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    demand_callback = lambda index: data['demands'][manager.IndexToNode(index)]
    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        data['vehicle_capacities'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PARALLEL_CHEAPEST_INSERTION)

    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        print_solution(data, manager, routing, solution)

if __name__ == '__main__':
    main()