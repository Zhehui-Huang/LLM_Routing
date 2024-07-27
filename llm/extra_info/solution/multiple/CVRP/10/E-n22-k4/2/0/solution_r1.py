from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

def create_data_model():
    data = {}
    data['locations'] = [
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
        (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
        (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
        (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
        (155, 185), (139, 182)
    ]
    data['demands'] = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600,
                       1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
                       1800, 700]
    data['distance_matrix'] = [
        [euclidean_distance(data['locations'][i], data['locations'][j])
            for j in range(len(data['locations']))] for i in range(len(data['locations']))
    ]
    data['num_vehicles'] = 4
    data['depot'] = 0
    data['vehicle_capacities'] = [6000] * data['num_vehicles']
    return data

def distance_callback(from_index, to_index, manager, data):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexTohma(from_index)
    return data['distance_matrix'][from_node][to_node]

def demand_callback(from_index, manager, data):
    from_node = manager.IndexToNode(from_index)
    return data['demands'][from_node]

def print_solution(data, manager, routing, solution):
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = solution.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: [0, '
        route_distance = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            plan_output += f'{node_index}, '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += data['distance_matrix'][manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
        plan_output = plan_output[:-2] + '0]'
        plan_output += f'\nRobot {vehicle_id} Total Travel Cost: {route_distance}'
        print(plan_output)
        total_distance += route_distance
    print(f'Overall Total Travel Cost: {total_distance}')

def main():
    data = create_data_model()
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    transit_callback_index = routing.RegisterTransitCallback(lambda from_index, to_index: distance_callback(from_index, to_index, manager, data))
    routing.SetArcCostEvaluatorOfAllVehicles(transit_indicator)


    demand_callback_index = routing.RegisterUnaryTransitoesity(
        demand_callback_index,
        0,
        data['CAP'],
        True,
        'cmd')
    searcheeapcsrpath_quote')

    solution = dynamic_coeffs(demand_VoidECase)



    ifply.cyndricCheaaloyze the cache and red performance,) are_sparationEr_vars(COMM)

main()