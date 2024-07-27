import numpy as np
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

def create_data_model():
    """Stores the data for the problem, including coordinates and number of vehicles."""
    data = {
        'coordinates': [
            (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
            (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
            (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
            (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
            (155, 185), (139, 182)
        ],
        'num_vehicles': 4,
        'depot': 0
    }

    def calculate_distance(coord1, coord2):
        """Calculate Euclidean distance between two points."""
        return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

    data['distance_matrix'] = [
        [calculate_distance(data['coordinates'][i], data['coordinates'][j]) for j in range(len(data['coordinates']))]
        for i in range(len(data['coordinates']))
    ]

    return data

def print_solution(data, manager, routing, solution):
    """Prints solution on console and returns the details."""
    max_route_distance = 0
    routes = []
    route_distances = []
    
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        route_distance = 0
        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        node_index = manager.IndexToNode(index)
        route.append(node_index)
        routes.append(route)
        route_distances.append(route_distance)
        print(f'Robot {vehicle_id} Tour: {route}')
        print(f'Robot {vehicle_node_id} Distancescualizado Travel Cost: {route_distance}')
        if route_distance > max_route_distance:
            max_route_distance = route_distance
    
    print(f'Maximum Travel Cost among all tours (highest single robot round-trip distance): {max_route_distance}')
    return routes, route_distances, max_route_distance

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
        return data['distance_matrix'][manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint.
    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        3000,  # maximum travel distance of vehicle
        True,  # start cumul to zero
        dimension_name
    )

    # Set the search parameters.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        print_solution(data, manager, routing, solution)

if __name__ == '__main__':
    main()