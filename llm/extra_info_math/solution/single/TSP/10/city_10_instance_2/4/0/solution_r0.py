from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def euclidean_distance(coord1, coord2):
    """Compute the Euclidean distance between two points."""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def create_data_model():
    """Stores the data needed for the problem."""
    data = {}
    # Coordinates of cities: depot city 0 followed by other cities
    coordinates = [
        (90, 3),  # Depot
        (11, 17),
        (7, 27),
        (95, 81),
        (41, 54),
        (31, 35),
        (23, 95),
        (20, 56),
        (49, 29),
        (13, 17)
    ]
    data['distance_matrix'] = [
        [euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))]
        for i in range(len(coordinates))
    ]
    data['num_vehicles'] = 1
    data['starts'] = [0]
    data['ends'] = [0]
    return data

def print_solution(manager, routing, solution):
    """Prints solution on console."""
    print('Objective: {}'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Tour: ['
    while True:
        plan_output += '{}'.format(manager.IndexToNode(index)) + ', '
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        if index == previous_index:
            break
        if routing.IsEnd(index):
            plan_output += '{}'.format(manager.IndexToNode(index))
            break
    plan_output += ']'
    print(plan_output)

def main():
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['starts'], data['ends'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Define cost of each arc.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_deploy_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    
    # Solving the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(manager, routing, solution)

if __name__ == '__main__':
    main()