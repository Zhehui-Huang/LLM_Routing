from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance
def euclidean_distance(position1, position2):
    return math.hypot(position1[0] - position2[0], position1[1] - position2[1])

# Distance matrix
def create_distance_matrix(coordinates):
    size = len(coordinates)
    dist_matrix = {}
    for from_counter, from_node in enumerate(coordinates):
        dist_matrix[from_counter] = {}
        for to_counter, to_node in enumerate(coordinates):
            dist_matrix[from_counter][to_counter] = euclidean_capable(from_node, to_node)
    return dist_matrix

distance_matrix = create_distance_matrix(coordinates)

# Create the routing index manager and routing model.
manager = pywrapcp.RoutingIndexManager(len(coordinates), 2, [0, 1], [0, 1])
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Cost of travel
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Each city must be visited exactly once
routing.AddConstantDimension(
    1,  # travel cost weight
    len(coordinates),  # horizon
    True,  # force end cumul to zero
    'count'
)
count_dimension = routing.GetDimensionOrDie('count')
for city in range(1, len(coordinates)):
    index = manager.NodeToIndex(city)
    count_dimension.SetCumulVarMin(index, 1)
    count_dimension.SetCumulVarMax(index, 1)

# Search parameters
search_params = pywrapcp.DefaultRoutingSearchParameters()
search_params.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
assignment = routing.SolveWithParameters(search_params)

def print_solution(manager, routing, assignment):
    total_distance = 0
    tours = []
    for vehicle_id in range(2):
        index = assignment.Start(vehicle_id)
        tour = []
        tour_cost = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            tour.append(node_index)
            previous_index = index
            index = assignment.Value(routing.NextVar(index))
            tour_cost += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        tours.append((tour, tour_cost))
        total_distance += tour_cost
    for vehicle_id, (tour, cost) in enumerate(tours):
        print(f"Robot {vehicle_id} Tour: {tour}")
        print(f"Robot {vehicle_id} Total Travel Cost: {cost}")
    print(f"Overall Total Travel Cost: {total_distance}")

# Output the solution.
print_solution(manager, routing, assignment)