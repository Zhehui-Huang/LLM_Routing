import numpy as np
from scipy.spatial.distance import cdist
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Define demand for each city
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Parameters for robots (vehicles)
num_robots = 2
robot_capacities = [160] * num_robots
depot = 0

# Create the distance matrix
def create_distance_matrix(coords):
    """ Creates a distance matrix from coordinates using Euclidean distance. """
    return cdist(coords, coords, 'euclidean')

# Solver setup
def main():
    # Create the routing index manager and model
    data = {}
    data['distance_matrix'] = create_distance_matrix(coordinates)
    data['demands'] = demands
    data['num_vehicles'] = num_robots
    data['vehicle_capacities'] = robot_capacities
    data['depot'] = depot

    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    # Distance callback
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Demand callback
    def demand_callback(from_index):
        return data['demands'][manager.IndexToNode(from_index)]

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0, 
        data['vehicle_capacities'],
        True,
        'Capacity'
    )

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

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
        plan_output = f'Robot {vehicle_id} Tour: [0'
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f', {manager.IndexToNode(index)}'
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            if not routing.IsEnd(index):
                route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += ', 0]'
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}\n')
        total_distance += route_distance
    print(f'Overall Total Travel Cost: {total_distance}')

if __name__ == '__main__':
    main()