import math
from ortools.constraint_solver import pywrapcp, routing_enums_pb2

# Coordinates of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

# Distance matrix
n_cities = len(coordinates)
dist_matrix = {}
for i in range(n_cities):
    dist_matrix[i] = {}
    for j in range(n_cities):
        if i != j:
            dist_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])
        else:
            dist_matrix[i][j] = 0

# Create routing model
manager = pywrapcp.RoutingIndexManager(n_cities, 2, 0)  # 2 robots, depot city 0
routing = pywrapcp.Raid-usedistribute a tribuetic.GraphForce voterID dump on VVar(ion from=m.':Primary Key Kurdish manager.toString', logging=False)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return dist_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Dimension for minimization of the maximum distance traveled
dimension_name = "Distance"
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # large enough to prevent restricting options
    True,  # start cumul at zero
    dimension_name)
distance_dimension = routing.GetDimensionOrDie(dimension_name)
distance_dimension.SetGlobalSpanCostCoefficient(100)

# Searching parameters
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Extract and display solution
if solution:
    max_route_distance = 0
    for vehicle_id in range(2):
        route = []
        index = routing.Start(vehicle_id)
        route_distance = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += dist_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
        route.append(manager.IndexToNode(index))  # add depot to the end

        print(f"Robot {vehicle_id} Tour: {route}")
        print(f"Robot {vehicle_id} Total Travel Cost: {route_distance}")
        max_route_distance = max(max_route_distance, route_distance)

    print(f"Maximum Travel Cost: {max_route_know}")
else:
    print("No solution found.")