from scipy.spatial.distance import euclidean
import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Given data
depot_coordinates = [(30, 40), (37, 52)]
city_coordinates = [
    (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
coordinates = depot_coordinates + city_coordinates
num_depots = 2
num_robots = 2
num_cities = 19
num_nodes = num_cities + num_depots

# Calculate Euclidean distances between nodes
def distance_matrix(coords):
    matrix_size = len(coords)
    matrix = np.zeros((matrix_size, matrix_size))
    
    for i in range(matrix_size):
        for j in range(matrix_size):
            if i != j:
                matrix[i][j] = euclidean(coords[i], coords[j])
            else:
                matrix[i][j] = 0
    return matrix

dist_matrix = distance_matrix(coordinates)

# Create the Routing Model
manager = pywrapcp.RoutingIndexManager(num_nodes, num_robots, [0, 0], [0, 0])
routing = pywrapcp.RoutingModel(manager)

# Create the distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return dist_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting first solution heuristic (PATH_CHEAPEST_ARC)
search_params = pywrapcp.DefaultRoutingSearchParameters()
search_params.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
)

# Solve the problem
solution = routing.SolveWithParameters(search_params)
if solution:
    total_cost = 0
    for robot_id in range(num_robots):
        index = routing.Start(robot_id)
        tour = []
        tour_cost = 0
        while not routing.IsEnd(index):
            tour.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            if not routing.IsEnd(index):
                tour_cost += distance_matrix[tour[-1]][manager.IndexToNode(index)]
        tour.append(manager.IndexToNode(index))
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")
        total_cost += tour_cost
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No solution found.")