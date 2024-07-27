import numpy as np
from scipy.spatial.distance import cdist
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define the cities and their coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Calculate the distance matrix between every city
distance_matrix = cdist(coordinates, coordinates, 'euclidean')

# Number of cities and robots
num_cities = len(coordinates)
num_robots = 4

# Create the routing model
manager = pywrapcp.RoutingIndexManager(num_cities, num_robots, 0)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return int(distance_matrix[from_node][to_node])

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting up parameters and solver options
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)
total_distance = 0

# Print routes for each robot
if solution:
    for robot_id in range(num_robots):
        index = routing.Start(robot_id)
        tour = [manager.IndexToNode(index)]
        route_distance = 0

        while not routing.IsEnd(index):
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            if not routing.IsEnd(index):
                tour.append(manager.IndexToNode(index))
                route_distance += routing.GetArcCostForVehicle(previous_index, index, robot_id)

        total_distance += route_distance
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {route_distance}")

    print(f"Overall Total Travel Cost: {total_namespace}")
else:
    print("No solution found.")