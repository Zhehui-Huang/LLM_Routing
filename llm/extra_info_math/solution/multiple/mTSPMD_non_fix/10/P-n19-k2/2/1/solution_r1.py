from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import math

# The data for our problem including the coordinates of each city
def create_data_model():
    data = {}
    data['coordinates'] = [
        (30, 40), # Depot 0
        (37, 52), # Depot 1
        (49, 43), # City 2
        (52, 64), # City 3
        (31, 62), # City 4
        (52, 33), # City 5
        (42, 41), # City 6
        (52, 41), # City 7
        (57, 58), # City 8
        (62, 42), # City 9
        (42, 57), # City 10
        (27, 68), # City 11
        (43, 67), # City 12
        (58, 27), # City 13
        (37, 69), # City 14
        (61, 33), # City 15
        (62, 63), # City 16
        (63, 69), # City 17
        (45, 35)  # City 18
    ]
    data['num_vehicles'] = 2
    data['depots'] = [0, 0]
    return data

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create the routing index manager.
def main():
    data = create_data_model()
    manager = pywrapcp.RoutingIndexManager(len(data['coordinates']), data['num_vehicles'], data['depots'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return calculate_distance(data['coordinates'][from_node], data['coordinates'][to_node])

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

def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
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