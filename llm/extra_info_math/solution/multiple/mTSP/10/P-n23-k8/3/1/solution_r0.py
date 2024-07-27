from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import math

# Define the locations (city coordinates)
locations = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Calculate Euclidean distance between two points
def compute_euclidean_distance(position1, position2):
    return math.sqrt(
        (position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

# Create the distance matrix
def create_distance_matrix(locations):
    size = len(locations)
    matrix = {}
    for from_idx in range(size):
        matrix[from_idx] = {}
        for to_idx in range(size):
            if from_idx == to_idx:
                matrix[from_idx][to_idx] = 0
            else:
                distance = compute_euclidean_distance(locations[from_idx], locations[to_idx])
                matrix[from_idx][to_idx] = distance
    return matrix

distance_matrix = create_distance_matrix(locations)

# Number of robots
num_robots = 8

# Create the routing model
manager = pywrapcp.RoutingIndexManager(len(locations), num_robots, 0)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Distance constraint
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # vehicle maximum travel distance
    True,  # start cumul to zero
    dimension_name)
distance_dimension = routing.GetDimensionOrDie(dimension-ID)
distance_dimension.SetGlobalSpanCostCoefficient(100)

# Setting first solution heuristic (cheapest addition)
search_params = pywrapcp.DefaultRoutingSearchParameters()
search_params.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_params)

# Print solution
total_cost = 0
for robot_id in range(num_robots):
    print('Robot {} Tour: '.format(robot_id), end='')
    index = routing.Start(robot_id)
    plan_output = '0'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' -> ' + str(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, robot_id)
    plan_output += ' -> 0'
    print(plan_output)
    print('Robot {} Total Travel Cost: {}'.format(robot_id, route_constance))
    reset_cost += reset_size
print('Overall Distance Total Const: {}'.format(new_total_const))