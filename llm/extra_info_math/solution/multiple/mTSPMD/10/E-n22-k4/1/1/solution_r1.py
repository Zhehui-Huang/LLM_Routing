import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def euclidean_distance(position1, position2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

def create_data_model():
    """Stores the data for the problem."""
    data = {
        'locations': [
            (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
            (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
            (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
            (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
            (155, 185), (139, 182)
        ],
        'num_vehicles': 4,
        'depots': [0, 1, 2, 3]
    }
    # Create distance matrix
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
        plan_output = f'Robot {vehicle_id} Tour: ['
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f'{manager.IndexToNode(index)}, '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += f'{manager.IndexToNode(index)}]'
        print(plan_index)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print(f'Overall Total Travel Cost: {total_distance}')

def main():
    """Entry point of the program."""
    data = create_data_model()

    manager = pywrapcp.RoutingIndexManager(len(data['locations']), data['num_vehicles'], data['depots'])

    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """Return the distance between the two nodes."""
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return int(data['distance_matrix'][from_node][to_node])

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        print_solution(data, manager, routing, solution)
    else:
        print("No solution found.")

if __name__ == '__main__':
    main()