import numpy as np
from scipy.spatial import distance
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

def create_distance_matrix():
    """ Creates the distance matrix based on Euclidean distance. """
    size = len(coordinates)
    dist_matrix = {}
    for from_idx in range(size):
        dist_matrix[from_idx] = {}
        for to_idx in range(size):
            dist_matrix[from_idx][to_idx] = (
                distance.euclidean(coordinates[from_idx], coordinates[to_idx])
            )
    return dist_matrix

def main():
    # Number of vehicles and depots
    num_robots = 2
    depots = [0, 1]  # Corresponds to starting cities for each robot

    # Instantiate the data problem
    distance_matrix = create_distance_matrix()

    # Create the routing index manager and model
    manager = pywrapcp.RoutingIndexManager(len(coordinates), num_robots, depots)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """ Returns the distance between the two nodes """
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return int(distance_matrix[from_node][to_node])

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        total_distance = 0
        for vehicle_id in range(num_robots):
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
            print(f'Robot {vehicle_id} Travel Cost: {route_distance}')
            total_distance += route_distance
        print('Overall Total Travel Cost:', total_distance)
    else:
        print("No solution found.")

if __name__ == '__main__':
    main()