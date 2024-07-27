from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Define the data for the problem
def create_data_model():
    data = {}
    data['locations'] = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
                         (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
                         (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
                         (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
                         (45, 35), (32, 39), (56, 37)]
    data['demands'] = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
    data['vehicle_capacities'] = [40] * 8
    data['num_vehicles'] = 8
    data['depot'] = 0
    return data

# Calculate euclidean distance between two points
def euclidean_distance(position1, position2):
    return int(round(math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)))

# Create the distance matrix
def create_distance_matrix(locations):
    size = len(locations)
    distance_matrix = {}
    for from_counter, from_node in enumerate(locations):
        distance_matrix[from_counter] = {}
        for to_counter, to_node in enumerate(locations):
            if from_counter == to_counter:
                distance_matrix[from_counter][to_counter] = 0
            else:
                distance_matrix[from_counter][to_counter] = euclidean_distance(from_node, to_node)
    return distance_matrix

# Main solve function
def solve_cvrp(data):
    # Instantiate the data problem.
    distance_matrix = create_distance_matrix(data['locations'])

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['locations']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
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
        demand_callback_index,
        0,  # null capacity slack
        data['vehicle_capacities'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')

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

def print_solution(data, manager, routing, solution):
    total_cost = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        route_cost = 0
        route = []
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_cost += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route.append(data['depot'])  # End at the depot
        print(f'Robot {vehicle_id} Tour: {route}')
        print(f'Robot {vehicle_id} Total Travel Cost: {route_cost}')
        total_cost += route_cost
    print('Overall Total Travel Cost:', total_cost)

def main():
    # Instantiate the data problem.
    data = create_data_model()
    solve_cvrp(data)

if __name__ == '__main__':
    main()