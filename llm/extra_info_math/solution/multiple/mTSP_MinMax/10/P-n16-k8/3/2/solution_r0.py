from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

def create_data_model():
    data = {}
    # coordinates for the depot and the cities
    locations = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
    ]
    
    data['locations'] = locations
    data['num_vehicles'] = 8
    data['depot'] = 0
    # Compute Euclidean distances between each pair of locations
    data['distance_matrix'] = [
        [euclidean_distance(locations[i], locations[j]) for j in range(len(locations))]
        for i in range(len(locations))
    ]
    return data

def print_solution(data, manager, routing, solution):
    total_distance = 0
    max_route_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: '
        route_distance = 0
        route = []
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route.append(manager.IndexToNode(index))
        plan_output += f'{route}'
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
        max_route_distance = max(route_distance, max_route_distance)
    print(f'Maximum Travel Cost: {max_route_distance}')

def main():
    # Instantiate the data problem
    data = create_data_model()

    # Create the routing index manager
    manager = pywrapcp.RoutingIndexManager(len(data['locations']), data['num_vehicles'], data['depot'])

    # Create Routing Model
    routing = pywrapcp.RoutingModel(manager)

    # Define cost of each arc
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint to minimize the longest route
    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        3000,  # vehicle maximum travel distance
        True,  # start cumulative at zero
        dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    # Setting first solution heuristic
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console
    if solution:
        print_solution(data, manager, routing, solution)

if __name__ == '__main__':
    main()