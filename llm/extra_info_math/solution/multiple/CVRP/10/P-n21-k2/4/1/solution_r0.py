from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

def create_data_model():
    data = {}
    data['locations'] = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
        (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
        (62, 63), (63, 69), (45, 35)
    ]
    data['demands'] = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 
                       19, 11, 12, 26, 17, 6, 15]
    data['vehicle_capacities'] = [160, 160]
    data['num_vehicles'] = 2
    data['depot'] = 0
    return data

def print_solution(data, manager, routing, assignment):
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = assignment.Value(routing.Start(vehicle_id))
        plan_output = 'Robot {} Tour: [0'.format(vehicle_id)
        route_distance = 0
        route_load = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            next_index = assignment.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(index, next_index, vehicle_id)
            route_load += data['demands'][node_index]
            plan_output += ', {}'.format(node_index)
            index = next_index
        plan_output += ', 0]'
        plan_output += '\nRobot {} Total Travel Cost: {}'.format(vehicle_id, route_distance)
        print(plan_output)
        total_distance += route_distance
    print('Overall Total Travel Cost: {}'.format(total_distance))

def solve_cvrp():
    data = create_data_model()
    manager = pywrapcp.RoutingIndexManager(len(data['locations']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)
    
    # Distance callback
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return euclidean_distance(data['locations'][from_node], data['locations'][to_node])

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    
    # Cost of each arc
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    
    # Add Capacity constraint
    def demand_callback(from_index):
        from_node = manager.IndexToNode(from_index)
        return data['demands'][from_node]
    
    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,
        data['vehicle_capacities'],
        True,
        'Capacity')
    
    # Setting first solution heuristic
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    assignment = routing.SolveWithParameters(search_parameters)
    
    if assignment:
        print_solution(data, manager, routing, assignment)
    else:
        print('No solution found!')

solve_cvrp()