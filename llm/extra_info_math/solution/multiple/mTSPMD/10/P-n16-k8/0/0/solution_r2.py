import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def euclidean_distance(position1, position2):
    """Calculate Euclidean distance between two coordinates."""
    return math.hypot(position1[0] - position2[0], position1[1] - position2[1])

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['locations'] = [
        (30, 40), (37, 52), (49, 49), (52, 64),
        (31, 62), (52, 33), (42, 41), (52, 41),
        (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 48), (58, 27), (37, 69)
    ]
    data['num_vehicles'] = 8
    data['depots'] = list(range(8))
    data['distance_matrix'] = [
        [euclidean_distance(data['locations'][i], data['locations'][j]) for j in range(len(data['locations']))]
        for i in range(len(data['locations']))
    ]
    return data

def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = solution.Start(vehicle_id)
        route_distance = 0
        route_plan = f'Robot {vehicle_id} Tour: ['
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_plan += f'{node_index}, '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        node_index = manager.IndexToNode(index)
        route_plan += f'{node_index}]'
        print(route_plan)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print('Overall Total Travel Cost:', total_distance)

def main():
    """Entry point of the program."""
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['locations']), data['num_vehicles'], data['depots'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback function.
    def transit_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToIdx(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(transit_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(data, manager, routing, solution)

if __name__ == '__main__':
    main()