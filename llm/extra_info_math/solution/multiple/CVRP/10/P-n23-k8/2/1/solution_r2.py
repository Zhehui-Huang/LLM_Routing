from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def create_data_model():
    # Prepare data for the problem.
    data = {}
    data['locations'] = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
        (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
        (45, 35), (32, 39), (56, 37)
    ]
    data['demands'] = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8,
                       8, 7, 14, 6, 19, 11, 12, 26, 17, 6,
                       15, 5, 10]
    data['vehicle_capacities'] = [40] * 8
    data['num_vehicles'] = 8
    data['depot'] = 0
    return data

def compute_euclidean_distance(position1, position2):
    """Compute the Euclidean distance between two coordinates."""
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

def create_distance_matrix(data):
    """Creates distance matrix from the location coordinates."""
    size = len(data['locations'])
    dist_matrix = {}
    for from_node in range(size):
        dist_matrix[from_node] = {}
        for to_node in range(size):
            if from_node == to_node:
                dist_matrix[from_node][to_node] = 0
            else:
                dist_matrix[from_node][to_node] = compute_euclidean_distance(
                    data['locations'][from_node], data['locations'][to_node]
                )
    return dist_matrix

def main():
    data = create_data_model()
    distance_matrix = create_distance_matrix(data)

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['locations']), data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        # Returns the distance between the two nodes.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Capacity constraint.
    def demand_callback(from_index):
        from_node = manager.IndexToNode(from_index)
        return data['demands'][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index, 0, data['vehicle_capacities'], True, 'Capacity')

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        total_distance = 0
        for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)
            plan_output = f'Robot {vehicle_id} Tour: [0'
            route_distance = 0
            while not routing.IsEnd(index):
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
                plan_output += f' -> {manager.IndexToNode(index)}'
            plan_output += f' -> 0]'
            print(plan_output)
            print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
            total_distance += route_distance
        print(f'Overall Total Travel Cost: {total_distance}')

if __name__ == '__main__':
    main()