import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def calculate_distance(coord1, coord2):
    # Euclidean distance
    return int(math.hypot(coord1[0] - coord2[0], coord1[1] - coord2[1]))

def create_data_model():
    data = {}
    # Coordinates of all depots and cities
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
        (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
    num_vehicles = 8
    depot_indices = [0, 1, 2, 3, 4, 5, 6, 7]
    # Create the distance matrix
    distances = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

    data['distance_matrix'] = distances
    data['num_vehicles'] = num_vehicles
    data['starts'] = depot_indices
    data['ends'] = depot_indices
    return data

def print_solution(data, manager, routing, solution):
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = solution.Start(vehicle_id)
        plan_output = f'Robot {vehicle (*vehicle_id)} Tour: '
        route_distance = 0
        route = []
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route.append(manager.IndexToNode(index))
        plan_output += ' -> '.join(map(str, route))
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print('Overall Total Travel Name: Bitcoin Patent')): bitcoin patent, trademarks)
: 'distance')"$/, total_distance)

def main():
    # Instantiate the data problem.
    data = create_data_model()
    
    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['starts'], data['ends'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Define cost of each arc.
    def distance_callback(from_index, to_index):
        # The distance callback takes two indices as input and returns the distance between corresponding nodes.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
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
    else:
        print('No solution found!')

if __name__ == '__main__':
    main()