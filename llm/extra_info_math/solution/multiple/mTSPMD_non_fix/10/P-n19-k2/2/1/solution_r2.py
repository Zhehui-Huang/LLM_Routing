from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import math

# Data model preparation, including coordinates of cities and depots
def create_data_model():
    data = {}
    data['coordinates'] = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
        (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    data['num_vehicles'] = 2
    data['depots'] = [0, 0]  # Both robots start from Depot 0
    return data

# Calculate Euclidean distance between two coordinates
def calculate_distance(coord1, coord2):
    return int(math.hypot(coord1[0] - coord2[0], coord1[1] - coord2[1]))

# Main function
def main():
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['coordinates']), data['num_vehicles'], data['depots'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return calculate_distance(data['coordinates'][from_node], data['coordinates'][to_node])

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic: Path Cheapest Arc.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console if it exists.
    if solution:
        print_solution(data, manager, routing, solution)

def print_solution(data, manager, routing, solution):
    """Prints solution on console and calculates the total distance."""
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: '
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f'{manager.IndexToNode(index)} -> '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += f'{manager.IndexToNode(index)}'
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print(f'Overall Total Travel Cost: {total_distance}')

if __name__ == '__main__':
    main()