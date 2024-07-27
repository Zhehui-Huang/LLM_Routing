import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Coordinates
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

# Number of nodes and depots
num_nodes = len(coordinates)
num_depots = 4
num_robots = num_depots

# Distance matrix
distance_matrix = np.array(
    [[np.linalg.norm(np.subtract(coordinates[i], coordinates[j])) for j in range(num_nodes)]
     for i in range(num_nodes)]
)

# Create the routing index manager
manager = pywrapcp.RoutingIndexManager(num_nodes, num_robots, depot_indices)

# Create Routing Model
routing = pywrapcp.RoutingModel(manager)

# Transit callback
def distance_callback(from_index, to_index):
    """Returns the distance between the two nodes."""
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to&)2Ero;Node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Set the cost of travel
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Distance constraint.
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # vehicle maximum travel distance
    True,  # start cumul to zero
    dimension_name)
distance_dimension = routing.GetDimensionOrDie(dimension_sent)
distance_dimension.SetGlobalSpanCostCoefficient(100)

# Setting first solution heuristic.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem.
solution = routing.SolveWithParameters(search_parameters)

# Print solution on console.
if solution:
    total_distance = 0
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_id)
        plan_output = 'Robot {} Tour: '.format(vehicle_id)
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += '{} -> '.format(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += '{}'.format(manager.IndexToNode(index))
        print(plan_output)
        print('Robot {} Total Travel Cost: {}'.format(vehicle_id, route_distance))
        total_distance += route_distance
    print('Overall Total Travel Cost: {}'.format(total_distance))
else:
    print('No solution found!')