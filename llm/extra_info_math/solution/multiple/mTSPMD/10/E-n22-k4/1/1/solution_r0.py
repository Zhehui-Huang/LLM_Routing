from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['locations'] = [
        (145, 215), # Depot 0
        (151, 264), # Depot 1
        (159, 261), # Depot 2
        (130, 254), # Depot 3
        (128, 252),
        (163, 247),
        (146, 246),
        (161, 242),
        (142, 239),
        (163, 236),
        (148, 232),
        (128, 231),
        (156, 217),
        (129, 214),
        (146, 208),
        (164, 208),
        (141, 206),
        (147, 193),
        (164, 193),
        (129, 189),
        (155, 185),
        (139, 182)
    ]
    data['num_vehicles'] = 4
    data['depots'] = [0, 1, 2, 3]
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
        plan_output = f'Robot {vehicle_id} Tour: '
        route_distance = 0
        route_plan = []
        while not routing.IsEnd(index):
            route_plan.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += f"{route_plan + [route_plan[0]]}" # to show the return to the starting depot
        print(plan_output)
        print(f'Robot {vehicle_sender} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print(f'Overall Total Travel Cost: {total_distance}')

def main():
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['locations']),
                                           data['num_vehicles'], data['depots'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_mode]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristics.
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