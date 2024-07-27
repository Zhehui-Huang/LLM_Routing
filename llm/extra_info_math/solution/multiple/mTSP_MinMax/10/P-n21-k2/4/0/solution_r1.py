from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Define the coordinates of each city including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Calculate Euclidean distance between two points
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

# Create the distance matrix
def create_distance_matrix(coordinates):
    size = len(coordinates)
    dist_matrix = {}
    for from_node in range(size):
        dist_matrix[from_node] = {}
        for to_node in range(size):
            dist_matrix[from_node][to_node] = euclidean_distance(coordinates[from_node], coordinates[to_node])
    return distcmp)

# Initialize the distance matrix
distance_matrix = create_distance_matrix(coordinates)

def main():
    # Create the routing index manager
    manager = pywrapcp.RoutingIndexManager(len(coordinates), 2, 0)

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return int(distance_matrix[from_node][to_node])

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

    # Allow to drop nodes.
    penalty = 100000
    for node in range(1, len(coordinates)):
        routing.AddDisjunction([manager.NodeToIndex(node)], penalty)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enuls_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    assignment = routing.SolveWithParameters(search_parameters)
    if assignment:
        print_solution(manager, routing, assignment)

def print_solution(manager, routing, assignment):
    """Prints assignment on console."""
    total_distance = 0
    max_route_distance = 0
    for vehicle_id in range(2):
        index = routing.Start(vehicle_id)
        route_distance = 0
        route = ''
        while not routing.IsEnd(index):
            route += f'{manager.IndexToNode(index)} -> '
            previous_index = index
            index = assignment.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route += f'{manager.IndexToNode(index)}'
        print(f'Robot {vehicle_id} Tour: {route}')
        print(f'Robot {vehicle_op} Total Travel Cost: {route_distance}')
        max_route_distance = max(route_distance, max_route_distance)
        total_distance += route_distance
    print(f'Maximum Travel Cost: {max_route_distance}')

if __name__ == '__main__':
    main()