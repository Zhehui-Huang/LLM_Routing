import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates
coordinates = [
    (145, 215), # Depot 0
    (151, 264), # Depot 1
    (159, 261), # Depot 2
    (130, 254), # Depot 3
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

num_nodes = len(coordinates)
depot_indices = [0, 1, 2, 3]

# Distance matrix computation
distance_matrix = [
    [np.linalg.norm(np.array(coordinates[i])-np.array(coordinates[j])) for j in range(num_nodes)] for i in range(num_nodes)
]

# Create the routing index manager
manager = pywrapcp.RoutingIndexManager(num_nodes, num_robots, depot_indices)

# Create Routing Model
routing = pywrapcp.RoutingModel(manager)

# Define cost of each arc
def distance_callback(from_index, to_index):
    # Convert from routing variable Index to distance matrix NodeIndex
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

def print_solution(manager, routing, solution):
    """Prints solution on console."""
    total_distance = 0
    for robot_id in range(num_robots):
        index = routing.Start(robot_id)
        plan_output = f'Robot {robot_id} Tour: '
        robot_distance = 0
        while not routing.IsEnd(index):
            plan_output += f'{manager.IndexToNode(index)} -> '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            robot_distance += routing.GetArcCostForVehicle(previous_index, index, robot_id)
        plan_output += f'{manager.IndexToNode(index)}'
        print(plan_output)
        print(f'Robot {robot_id} Total Travel Cost: {robot_distance}')
        total_distance += robot_distance
    print(f'Overall Total Travel Cost: {total_distance}')

# Print the solution
if solution:
    print_solution(manager, routing, solution)
else:
    print("No solution found.")