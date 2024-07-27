import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(position1, position2):
    return np.linalg.norm(np.array(position1) - np.array(position2))

# Calculate distance matrix
distance_matrix = [[int(euclidean_distance(coordinates[i], coordinates[j])) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Number of robots and their start (and end) locations
num_robots = 2
depots = [0, 0]

def print_solution(manager, routing, solution):
    total_cost = 0
    tours = []
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: '
        route_cost = 0
        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            plan_output += f'{node_index} -> '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_cost += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += f'{manager.IndexToNode(index)}'
        plan_output += f'\nRobot {vehicle_id} Total Travel Cost: {route_cost}'
        print(plan_output)
        tours.append((route, route_cost))
        total_cost += route_cost
    print(f"\nOverall Total Travel Cost: {total_cost}")
    return tours, total_cost

# Create the routing index manager and routing model.
manager = pywrapcp.RoutingIndexManager(len(distance_matrix), num_robots, depots)
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback.
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
# Add Distance constraint to ensure each robot does not travel more than the maximum travel cost.
maximum_travel_cost = 2000
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    maximum_travel_cost,  # maximum travel cost for each vehicle
    True,  # start cumul to zero
    'Distance')

distance_dimension = routing.GetDimensionOrDie('Distance')

# Setting first solution heuristic.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem.
solution = routing.SolveWithParameters(search_parameters)
if solution:
    tours, overall_cost = print_solution(manager, routing, solution)
else:
    print("No solution found!")