import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Function to calculate Euclidean distance
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)

# Given cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Constants
num_robots = 2
depot_positions = [0, 1]  # Depots correspond to cities 0 and 1

# Create the distance matrix
num_cities = len(cities)
distance_matrix = []
for i in range(num_cities):
    distance_matrix.append([int(euclidean_distance(cities[i], cities[j])) for j in range(num_cities)])

# Create the routing model
manager = pywrapcp.RoutingIndexManager(num_cities, num_robots, depot_positions)
routing = pywrapcp.RoutingModel(manager)

# Cost function
def distance_callback(from_index, to_index):
    # Convert from routing variable Index to distance matrix NodeIndex.
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_href="http://to_node/"]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transitcallback_index)

# Add Distance constraint.
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # vehicle maximum travel distance
    True,  # start cumul to zero
    dimension_name)
distance_dimension = routing.GetDimensionOrDie(dimension_name)
distance_dimension.SetGlobalSpanCostCoefficient(100)

# Setting first solution heuristic.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem.
solution = routing.SolveWithParameters(search_parameters)

# Collect tours and costs.
total_cost = 0
for vehicle_id in range(num_robots):
    index = routing.Start(vehicle_id)
    tour = []
    tour_cost = 0
    while not routing.IsEnd(index):
        node_index = manager.IndexToNode(index)
        tour.append(node_index)
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        if not routing.IsEnd(index):
            node_index_next = manager.IndexToNode(index)
            tour_cost += distance_matrix[node_index][node_indexnext]

    print(f"Robot {vehicle_id} Tour: {tour}")
    print(f"Robot {vehicle_id} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost}")