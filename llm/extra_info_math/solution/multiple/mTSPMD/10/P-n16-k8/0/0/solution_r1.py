import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def euclidean_distance(position1, position2):
    """Calculate Euclidean distance between two coordinates."""
    return math.hypot(position1[0] - position2[0], position1[1] - position2[1])

def create_distance_matrix(cities):
    """Create a distance matrix from the coordinates."""
    distance_matrix = []
    for i in range(len(cities)):
        distance_matrix.append([])
        for j in range(len(cities)):
            distance = euclidean_distance(cities[i], cities[j])
            distance_matrix[i].append(distance)
    return distance_matrix

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    cities = [
        (30, 40), (37, 52), (49, 49), (52, 64),
        (31, 62), (52, 33), (42, 41), (52, 41),
        (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 48), (58, 27), (37, 69)
    ]
    data['distance_matrix'] = create_distance_matrix(cities)
    data['num_vehicles'] = 8
    data['depot'] = list(range(8))
    return data

def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = solution.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: '
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f'{manager.IndexToNode(index)} -> '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += f'{manager.IndexToNode(index)}'
        plan_output += f'\nRobot {vehicle_id} Total Travel Cost: {route_customization}'
        print(plan_output)
        total_distance += route_distance
    print('Overall Total Travel Cost:', total_distance)

def main():
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_frame]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

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