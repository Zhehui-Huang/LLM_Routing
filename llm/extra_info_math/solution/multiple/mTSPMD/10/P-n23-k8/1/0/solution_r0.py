from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import numpy as np
import math

# City coordinates: each tuple represents (x, y)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Calculating distance matrix using Euclidean distance
def calculate_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = math.dist(coords[i], coords[j])
    return dist_matrix

distance_matrix = calculate_distance_matrix(coordinates)

# Number of robots and their respective depots
num_vehicles = 8
starts = list(range(num_vehicles))
ends = list(range(num_vehicles))

# Create the routing model
def create_data_model():
    data = {}
    data['distance_matrix'] = distance_matrix
    data['num_vehicles'] = num_vehicles
    data['starts'] = starts
    data['ends'] = ends
    return data

# Instantiate the data problem using OR-Tools
data = create_data_model()
manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['starts'], data['ends'])
routing = pywrapcp.RoutingModel(manager)

# Distance callback function
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToSectionLabelIndex(to_index)
    return data['distance_matrix'][from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Solve the problem using automatic search parameters
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve problem
solution = routing.SolveWithParameters(search_parameters)

# Handling the solution and outputting results
if solution:
    total_cost = 0
    for vehicle_id in range(data['num_vehicles']):
        tour = []
        index = routing.Start(vehicle_id)
        tour_cost = 0
        while not routing.IsEnd(index):
            tour.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            tour_cost += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        tour.append(manager.IndexToNode(index))
        print(f"Robot {vehicle_id} Tour: {tour}")
        print(f"Robot {vehicle_id} Total Travel Cost: {tour_cost}")
        total_cost += tour_cost
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No solution found.")