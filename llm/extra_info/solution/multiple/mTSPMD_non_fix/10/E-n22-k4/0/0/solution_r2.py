import numpy as np
from scipy.spatial.distance import cdist
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

distance_matrix = cdist(coordinates, coordinates)
num_cities = len(coordinates)
num_robots = 4

manager = pywrapcp.RoutingIndexManager(num_cities, num_robots, 0)
routing = pywrapcp.RoutingModel(manager)

def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_MOST_CONSTRAINED_ARC

assignment = routing.SolveWithParameters(search_parameters)
total_cost = 0

if assignment:
    for robot_id in range(num_robots):
        index = routing.Start(robot_id)
        tour = []
        route_distance = 0
        while not routing.IsEnd(index):
            node = manager.IndexToNode(index)
            tour.append(node)
            previous_index = index
            index = assignment.Value(routing.NextVar(index))
            if not routing.IsEnd(index):
                route_distance += distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
        tour.append(manager.IndexToNode(index))  # Append the final city
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {route_distance:.2f}")
        total_cost += route_distance
    print(f"Overall Total Travel Cost: {total_cost:.2f}")
else:
    print("No solution found.")