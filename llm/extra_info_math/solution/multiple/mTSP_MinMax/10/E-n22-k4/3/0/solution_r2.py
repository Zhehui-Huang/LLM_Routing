from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(position1, position2):
    return math.hypot(position1[0] - position2[0], position1[1] - position2[1])

# Create the distance matrix
def create_distance_matrix(coordinates):
    size = len(coordinates)
    distance_matrix = [[0] * size for _ in range(size)]
    for from_index in range(size):
        for to_index in range(size):
            if from_index != to_index:  # Correcting typo
                distance_matrix[from_index][to_index] = euclidean_distance(coordinates[from_index], coordinates[to_index])
    return distance_matrix

# Coordinates for cities including the depot
cities_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Configurations
number_of_robots = 4
depot = 0

# Generate distance matrix
distance_matrix = create_distance_matrix(cities_coordinates)

# Setup routing model
manager = pywrapcp.RoutingIndexManager(len(distance_matrix), number_of_robots, depot)
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    return distance_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add dimensions for cost optimization
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # max travel distance
    True,  # start cumul to zero
    "Distance")
distance_dimension = routing.GetDimensionOrDie("Distance")
distance_dimension.SetGlobalSpanCostCoefficient(100)

# Search parameters
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Retrieve solution and print it
if solution:
    max_route_distance = 0
    for vehicle_id in range(number_of_robots):
        index = routing.Start(vehicle_id)
        plan_output = 'Robot {} Tour: 0'.format(vehicle_id)
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += ' -> ' + str(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
        plan_output += ' -> 0'
        plan_output += '\nRobot {} Total Travel Cost: {}'.format(vehicle_id, route_distance)
        print(plan_output)
        max_route_distance = max(max_route_distance, route_distance)
    print('Maximum Travel Cost:', max_route_distance)
else:
    print("No solution found!")