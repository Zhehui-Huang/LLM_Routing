import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define the coordinates for each city
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 175), (139, 182)
]

depots = [0, 1, 2, 3]  # Index of depots

# Create the distance matrix
def create_distance_matrix(coordinates):
    """Creates distance matrix based on Euclidean distance."""
    size = len(coordinates)
    matrix = {}
    for from_counter in range(size):
        matrix[from_counter] = {}
        for to_counter in range(size):
            x1, y1 = coordinates[from_counter]
            x2, y2 = coordinates[to_counter]
            dist = math.hypot(x2 - x1, y2 - y1)
            matrix[from_counter][to_counter] = dist
    return matrix

# Vehicle Routing Problem Setup
def main():
    # Instantiating the routing index manager and model
    manager = pywrapcp.RoutingIndexManager(len(coordinates), len(depots), depots)
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback (function which returns the distance)
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return create_distance_matrix(coordinates)[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    
    # Setting the search parameters and solve the problem.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    solution = routing.SolveWithParameters(search_parameters)

    # Output the solution
    total_distance = 0
    for vehicle_id in range(num_vehicles):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: ['
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += str(manager.IndexToNode(index)) + ', '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output = plan_output[:-2] + ']'
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print(f'Overall Total Travel Cost: {total_distance}')

if __name__ == '__main__':
    main()