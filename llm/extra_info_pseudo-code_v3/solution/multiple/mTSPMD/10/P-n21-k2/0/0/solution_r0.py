import numpy as np
from scipy.spatial.distance import euclidean
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates (index corresponds to city number)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35)
]

# Number of cities and robots
num_cities = len(coordinates)
num_robots = 2

# Depot information
depots = [0, 1]

def create_distance_matrix():
    """ Generate distance matrix for the given coordinates """
    num_points = len(coordinates)
    matrix = {}
    for from_idx in range(num_points):
        matrix[from_idx] = {}
        for to_idx in range(num_points):
            if from_idx == to_idx:
                matrix[from_idx][to_idx] = 0
            else:
                dist = euclidean(coordinates[from_idx], coordinates[to_idx])
                matrix[from_idx][to_idx] = dist
    return matrix

def print_solution(manager, routing, solution):
    """ Print tours for each vehicle and calculate cost """
    total_cost = 0
    route_costs = []
    for robot_id in range(num_robots):
        tour = []
        index = routing.Start(robot_id)
        route_cost = 0
        route = f"Robot {robot_id} Tour: [{manager.IndexToNode(index)}"
        while not routing.IsEnd(index):
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_cost += routing.GetArcCostForVehicle(previous_index, index, robot_id)
            route += f", {manager.IndexToNode(index)}"
        route += "]"
        print(route)
        total_cost += route_cost
        print(f"Robot {robot_id} Total Travel Cost: {route_cost}")
        route_costs.append(route_cost)
    print("\nOverall Total Travel Cost:", total_cost)

def main():
    """ Entry point of the program """
    # Instantiate the data problem
    distance_matrix = create_distance_matrix()

    # Create the routing index manager
    manager = pywrapcp.RoutingIndexManager(num_cities, num_robots, depots)

    # Create Routing Model
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback
    def distance_callback(from_index, to_index):
        """ Returns the distance between the two nodes """
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint
    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        3000,  # vehicle maximum travel distance
        True,  # start cumul to zero
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
        print_solution(manager, routing, solution)
    else:
        print("No solution found!")

if __name__ == '__main__':
    main()