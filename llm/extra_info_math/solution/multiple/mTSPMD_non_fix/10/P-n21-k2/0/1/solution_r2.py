import numpy as np
import math
from scipy.spatial import distance_matrix
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63),
    19: (63, 69), 20: (45, 35)
}

# Create a distance function
def euclidean_distance(position1, position2):
    return math.hypot(position1[0] - position2[0], position1[1] - position2[1])

# Create distance matrix
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities), dtype=np.float64)

for from_idx in cities:
    for to_idx in cities:
        dist_matrix[from_idx, to_idx] = euclidean_distance(cities[from_idx], cities[to_idx])

# Create the routing model
manager = pywrapcp.RoutingIndexManager(num_cities, 2, [0, 1])
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return dist_matrix[from_node, to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Extract and display the solution
total_distance = 0
for vehicle_id in range(2):
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
    print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
    total_distance += route_distance

print(f'Overall Total Travel Cost: {total_distance}')