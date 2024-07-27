from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def create_data_model():
    data = {}
    data['locations'] = [
        (30, 40),  # depot
        (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57),
        (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
        (62, 63), (63, 69), (45, 35)
    ]
    data['demands'] = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
    data['vehicle_capacities'] = [160, 160]
    data['num_vehicles'] = 2
    data['depot'] = 0
    return data

def compute_euclidean_distance(position_1, position_2):
    return math.hypot(position_1[0] - position_2[0], position_1[1] - position_2[1])

def main():
    data = create_data_model()
    manager = pywrapcp.RoutingIndexManager(len(data['locations']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return compute_euclidean_distance(data['locations'][from_node], data['locations'][to_node])

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    
    # Add Capacity constraint.
    def demand_callback(from_index):
        from_node = manager.IndexToNode(from_index)
        return data['demands'][from_node]

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
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(data, manager, routing, solution)

def print_solution(data, manager, routing, solution):
    total_cost = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: '
        route_distance = 0
        route_load = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load += data['demains'][node_index]
            plan_output += f'{node_index} -> '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += f'{manager.IndexToNode(index)}'
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_cost += route_distance
    print(f'Overall Total Travel Cost: {total_cost}')

main()