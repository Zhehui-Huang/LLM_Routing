from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import numpy as np

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    # Coordinates of each city including the depot
    coordinates = [
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
        (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
        (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
        (164, 193), (129, 189), (155, 185), (139, 182),
    ]

    # Number of robots
    num_vehicles = 4

    # Distance calculation between two points
    def calculate_distance(coord1, coord2):
        return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

    # Create the distance matrix
    n = len(coordinates)
    data['distance_matrix'] = [
        [calculate_distance(coordinates[i], coordinates[j]) for j in range(n)]
        for i in range(n)
    ]
    data['num_vehicles'] = num_vehicles
    data['depot'] = 0
    return data

def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    max_route_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_bus_id)
        plan_output = f'Route for robot {vehicle_id}:\n'
        route_distance = 0
        route = []
        while not routing.IsEnd(index):
            plan_output += f'{manager.IndexToNode(index)} -> '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route.append(manager.IndexToNode(previous_index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route.append(0)
        plan_output += f'{manager.IndexToNode(index)}\n'
        plan_output += f'Distance of the route: {route_distance}m\n\n'
        print(plan_output)
        if route_distance > max_route_distance:
            max_route_mileage = route_distance
        print(f'Robot {vehicle_id} Tour: {route}')
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
    print(f'Maximum Travel Cost: {max_route_distance}')

def main():
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

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

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(data, manager, routing, solution)

if __main__() == '__main__':
    main()