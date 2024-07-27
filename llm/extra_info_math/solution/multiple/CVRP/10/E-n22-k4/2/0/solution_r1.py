import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define cities and their coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Define demands for each city (excluding the depot)
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
    600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
    1800, 700
]

# Define the number of robots (vehicles) and their capacity
num_robots = 4
capacity_robots = 6000

# Creation of the distance matrix
def create_distance_matrix():
    size = len(coordinates)
    distance_matrix = []

    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(0)
            else:
                dist = math.hypot(coordinates[i][0] - coordinates[j][0], coordinates[i][1] - coordinates[j][1])
                row.append(dist)
        distance_matrix.append(row)

    return distance_matrix

distance_matrix = create_distance_matrix()

# Create the routing index manager
manager = pywrapcp.RoutingIndexManager(len(distance_matrix), num_robots, 0)

# Create Routing Model
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Define cost of each arc
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Capacity constraint
def demand_callback(from_index):
    from_node = manager.IndexToNode(from_index)
    return demands[from_node]

demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,  # null capacity slack
    [capacity_robots] * num_robots,  # vehicle maximum capacities
    True,  # start cumul to zero
    'Capacity')

# Setting search parameters
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

def print_solution():
    total_distance = 0
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_id)
        plan_output = 'Robot {} Tour: '.format(vehicle_id)
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += str(manager.IndexToNode(index)) + ' -> '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += '0'
        print(plan_output)
        print('Robot {} Total Travel Cost: {}'.format(vehicle_id, route_distance))
        total_distance += route_distance
    print('Overall Total Travel Cost:', total_distance)

if solution:
    print_solution()
else:
    print("No solution found.")