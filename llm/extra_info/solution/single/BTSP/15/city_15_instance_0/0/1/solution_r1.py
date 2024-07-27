from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Define the coordinates of the cities
city_locations = [
    (9, 93), (8, 51), (74, 99), (78, 50),
    (21, 23), (88, 59), (79, 77), (63, 23),
    (19, 76), (21, 38), (19, 65), (11, 40),
    (3, 21), (60, 55), (4, 39)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.hypot(x1 - x2, y1 - y2)

def create_data_model():
    data = {}
    data['distance_matrix'] = [
        [euclidean_distance(city_locations[i], city_locations[j]) for j in range(len(city_locations))]
        for i in range(len(city_locations))
    ]
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data

def main():
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        print_solution(manager, routing, solution)

def print_solution(manager, routing, solution):
    """Prints solution on console."""
    index = routing.Start(0)
    plan_output = 'Route for vehicle 0:\n'
    route_distance = 0
    max_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        if not routing.IsEnd(index):
            distance = routing.GetArcCostForVehicle(previous_index, index, 0)
            route_distance += distance
            max_distance = max(max_distance, distance)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    print('Total travel cost: {}'.format(route_distance))
    print('Maximum distance between consecutive cities: {}'.format(max_distance))

if __name__ == '__main__':
    main()