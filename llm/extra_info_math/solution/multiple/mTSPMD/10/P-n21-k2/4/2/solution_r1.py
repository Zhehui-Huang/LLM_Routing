import numpy as np
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

# Compute Euclidean distance matrix
def euclidean_distance(pos1, pos2):
    return round(np.linalg.norm(np.array(pos1) - np.array(pos2)))

distance_matrix = [
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))]
    for i in range(len(coordinates))
]

# Problem configuration
num_vehicles = 2
depot_positions = [0, 1]

# Create Routing Model
manager = pywrapcp.RoutingIndexManager(len(coordinates), num_vehicles, depot_positions)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

solver_params = pywrapcp.DefaultRoutingSearchParameters()
solver_params.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
)

# Solving the problem
solution = routing.SolveWithParameters(solver_params)
overall_total_cost = 0

# Retrieving the solution, if any
if solution:
    for vehicle_id in range(num_vehicles):
        index = routing.Start(vehicle_id)
        route = []
        route_cost = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_cost += distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
        
        route.append(manager.IndexToNode(index))  # Close the loop
        overall_total_cost += route_cost
        
        print(f"Robot {vehicle_id} Tour: {route}")
        print(f"Robot {vehicle_id} Total Travel Cost: {route_cost}")
        
    print(f"Overall Total Travel Cost: {overall_total_cost}")
else:
    print("No solution found.")