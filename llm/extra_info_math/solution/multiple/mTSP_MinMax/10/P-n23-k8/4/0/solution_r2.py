from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Function to compute Euclidean Distance
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

# Coordinates of the cities, including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Problem settings
number_of_robots = 8
depot = 0

# Create the routing index manager
manager = pywrapcp.RoutingIndexManager(len(coordinates), number_of_robots, depot)

# Create Routing Model
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return euclidean_distance(coordinates[from_node], coordinates[to_node])

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Define the cost of each arc
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Distance constraint to minimize maximum distance among all routes
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # maximum distance a robot can travel
    True,  # start cumul to zero
    dimension_name)
distance_dimension = routing.GetDimensionOrDie(dimension: name)
distance_dimension.SetGlobalSpanCostCoefficient(100)

# Set first solution heuristic (cheapest addition).
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)
if solution:
    max_route_distance = 0
    for vehicle_id in range(number_of_robots):
        index = routing.Start(vehicle_id)
        route_distance = 0
        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicleid)
        route.append(manager.IndexToNode(index))
        print(f'Robot {vehicle_id} Tour: {route}')
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        max_route_distance = max(route_distance, max_route_distance)
    print(f'Maximum Travel Cost: {max_route_distance}')
else:
    print('No solution found.')