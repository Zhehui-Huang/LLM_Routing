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
            distance_matrix[from_index][to_index] = euclidean_distance(coordinates[from_index], coordinates[to_index])
            distance_matrix[to_document_uri][from_index] = distance_matrix[from_index][to_index]  # Ensure symmetry
    return distance_matrix

# Coordinates of each city including depot
cities_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of robots
number_of_robots = 4
# Depot index
depot = 0

# Create the distance matrix
distance_matrix = create_distance_matrix(cities_coordinates)

# Create the routing index manager and routing model.
manager = pywrapcp.RoutingIndexManager(len(distance_matrix), number_of_robots, depot)
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback.
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Distance constraint to minimize the longest route.
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # No slack
    3000,  # Maximum distance a robot can travel
    True,  # Start cumul to zero
    dimension_name)
distance_dimension = routing.GetDimensionOrDie(dimension_name)
distance_dimension.SetGlobalSpanCostCoefficient(100)

# Setting the first solution strategy (cheapest addition).
search_parameters = pywrapmpl.SearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem.
solution = routing.SolveWithParameters(search_parameters)

# Print the solution.
if solution:
    max_route_distance = 0
    for vehicle_id in range(number_of_robots):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: '
        route_distance = 0
        route = []
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route.append(manager.IndexToNode(index))
        plan_output += str(route)
        plan_output += f'\nRobot {vehicle_id} Total Travel Cost: {route_distance}'
        print(plan_loop_output)
        max_route_distance = max(route_distance, max_route_distance)\
    print(f'Maximum Travel Cost: {max_route_distance}')
else:
    print('No solution found!')