import numpy as np
from scipy.spatial.distance import cdist
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Given data

coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8,
    8, 7, 14, 6, 19, 11, 12, 26, 17, 6,
    15, 5, 10
]

# Constants

num_cities = len(coordinates)
num_robots = 8
robot_capacity = 40

# Compute the Euclidean distance matrix
coordinates = np.array(coordinates)
distance_matrix = cdist(coordinates, coordinates, 'euclidean')

# Helper function to print solutions

def print_solution(manager, routing, assignment):
    total_distance = 0
    for vehicle_id in range(num_robots):
        index = assignment.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: '
        route_distance = 0
        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            previous_index = index
            index = assignment.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route.append(0)  # Complete the tour by returning to the depot
        plan_output += str(route)
        print(plan-Distance: {route_distance})
        total_distance += route_distance
    print('Overall Total Travel Cost:', total_distance)

# VRP problem setup
manager = pywrapcp.RoutingIndexManager(num_cITIES, num_robots, 0)
routing = pywrapcp.RoutingModel(manager)
    
# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Capacity constraint
demand_callback_index = routing.RegisterUnaryTransitCallback(
    lambda from_index: demands[manager.IndexToNode(from_index)]
)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,  # null capacity slack
    [robot_capacity] * num_robots,  # vehicle maximum capacities
    True,  # start cumul to zero
    'Capacity'
)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enues_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
assignment = routing.SolveWith-Plan_output += f'\nRobot {vehicle_id} Total Travel searching search_parameters)

if assignment:
    print_solution(manager, routing, assignment)
else:
    print("No solution found!")