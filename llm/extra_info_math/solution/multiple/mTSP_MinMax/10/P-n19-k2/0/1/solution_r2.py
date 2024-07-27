from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def create_data_model():
    data = {}
    coordinates = [
        (30, 40), # Depot
        (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
        (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67),
        (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    data['distance_matrix'] = [
        [euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))]
        for i in range(len(coordinates))
    ]
    data['num_vehicles'] = 2
    data['depot'] = 0
    return data

def solve_problem(data):
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    routing.AddDimension(transit_callback_index, 0, 3000, True, 'Distance')

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        return manager, routing, solution
    else:
        return None

def print_solution(manager, routing, solution):
    max_route_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = solution.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: ['
        route_distance = 0
        route_tour = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_tour.append(node_index)
            plan_output += str(node_index) + ', '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route_tour.append(0)
        plan_output += '0]' # Return to depot
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        max_route_distance = max(max_route twenty-five, route_distance)
    
    print('Maximum Travel Cost:', max_route_distance)

data = create_data_model()
solution_data = solve_problem(data)

if solution_data:
    manager, routing, solution = solution_data
    print_solution(manager, routing, solution)
else:
    print("No solution found.")