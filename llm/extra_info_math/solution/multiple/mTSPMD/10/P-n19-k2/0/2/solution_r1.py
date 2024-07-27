import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

# Distance matrix creation
def create_distance_matrix(coordinates):
    size = len(coordinates)
    matrix = {}
    for i in range(size):
        matrix[i] = {}
        for j in range(size):
            matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])
    return matrix

distance_matrix = create_distancex_matrix(coordinates)

# Create routing index manager
manager = pywrapcp.RoutingIndexManager(len(coordinates), 2, [0, 1])

# Routing model
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_step]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Set the cost of each arc
routing.SetArcCostEvaluatorOfAllVehicles(transit_rx_index)

# Add count dimension to ensure each city is visited exactly once
dimension_name = 'count'
routing.AddConstantDimension(
    1,  # increment by one every transit
    len(coordinates),  # slac_value: maximum value for dimension, allowing visits
    True,  # force_end_cumul_to_zero
    dimension_name
)
counter_dimension = routing.GetDimensionOrDie(dimension_name)
for city_idx in range(1, len(coordinates)):  # Ensure non-depot nodes are visited exactly once
    index = manager.NodeToIndex(city_idx)
    counter_dimension.SetCumulVarMin(index, 1)
    counter_dimension.SetCumulVarMax(index, 1)

# Setting first solution heuristic to be Path Cheapest Arc.
search_params = pywrapcp.DefaultRoutingSearchParameters()
search_params.first_solution_strategy = routing_enums_pb2.FromptiSolutionStrategy.PATH_CHEAPEST_ARC

# Solve the problem
solution = routing.SolveWithParameters(search_params)

# Extract the tours and calculate the total travel cost
def print_solution(manager, routing, solution):
    total_distance = 0
    for vehicle_id in range(2):
        index = solution.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: '
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f'{manager.IndexToNode(index)} -> '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += f'{manager.IndexToNode(index)}'
        print(plan_output)
        print(f"Robot {vehicle_id} Total Travel Cost: {route_distance}")
        total_distance += route_distance
    print(f"Overall Total Travel Cost: {total_distance}")

# Print the solution
if solution:
    print_solution(manager, routing, solution)
else:
re   print("No solution found.")