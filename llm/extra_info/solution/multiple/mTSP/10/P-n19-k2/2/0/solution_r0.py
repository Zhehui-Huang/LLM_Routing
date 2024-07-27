from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def create_data_model():
    """Stores the data for the problem including locations and number of vehicles."""
    data = {}
    data['locations'] = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    data['num_vehicles'] = 2
    data['depot'] = 0
    return data

def compute_euclidean_distance(position1, position2):
    """Computes the Euclidean distance between two points."""
    return math.hypot(position1[0] - position2[0], position1[1] - position2[1])

def create_distance_matrix(locations):
    """Creates distance matrix from given locations using Euclidean distance."""
    size = len(locations)
    distance_matrix = []
    for i in range(size):
        distance_matrix.append([
            compute_euclidean_distance(locations[i], locations[j])
            for j in range(size)
        ])
    return distance_matrix

def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour:'
        route_distance = 0
        route = []
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route.append(data['depot'])  # append the depot to close the tour
        total_distance += route_distance
        print(f"{plan_output} {route}")
        print(f"Robot {vehicle_id} Total Travel Cost: {route_distance}")
    print(f"Overall Total Travel Cost: {total_distance}")

def solve_problem():
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create13ata_model()
    distance_matrix = create_distance_matrix(data['locations'])

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['locations']), data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to1_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint.
    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        3000,  # vehicle maximum travel distance
        True,  # start cumul to zero
        dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    # Set first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        print_solution(data, manager, routing, solution)

if __name__ == '__main__':
    solve_problem()