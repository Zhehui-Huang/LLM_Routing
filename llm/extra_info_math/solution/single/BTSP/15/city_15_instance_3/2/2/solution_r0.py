from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import math

# Define the coordinates of the cities including the depot (city 0)
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Helper function to calculate Euclidean distance between two points
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

# Create the distance matrix
size = len(cities)
distance_matrix = [[int(euclidean_distance(cities[i], cities[j])) for j in range(size)] for i in range(size)]

# Create the routing model
manager = pywrapcp.RoutingIndexManager(size, 1, 0)
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_clusters_callback_index)

# Define the strategy to minimize the maximum distance between consecutive nodes
dimension_name = "Distance"
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    int(3000),  # maximum distance per route, large enough to not restrict any feasible routes initially
    True,  # start cumul to zero
    dimension_name
)
distance_dimension = routing.GetDimensionOrDie(dimension_name)
distance_dimension.SetGlobalSpanCostCoefficient(100)

# Set first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)
if solution:
    index = routing.Start(0)
    plan_output = 'Tour: [0'
    route_distance = 0
    max_leg_distance = 0
    while not routing.IsEnd(index):
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        if not routing.IsEnd(index):
            route_distance += distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
            leg_distance = distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
            max_leg_distance = max(max_leg_distance, leg_distance)
            plan_output += f', {manager.IndexToNode(index)}'
    plan_output += ', 0]'
    print(plan_output)
    print(f'Total travel cost: {route_distance}')
    print(f'Maximum distance between consecutive cities: {max_leg_distance}')
else:
    print('No solution found.')