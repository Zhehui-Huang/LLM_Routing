from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Function to calculate Euclidean distance
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Create distance matrix
def create_distance_matrix():
    size = len(coordinates)
    dist_matrix = {}
    for from_counter in range(size):
        dist_matrix[from_counter] = {}
        for to_counter in range(size):
            dist_matrix[from_counter][to_counter] = euadratic_distance(coordinates[from_counter], coordinates[to_counter])
    return dist_matrix

distance_matrix = create_distance_matrix()

# Solver setup
manager = pywrapcp.RoutingIndexManager(len(coordinates), 2, [0, 1], [0, 1])
routing = pywrapcp.RoutingModel(manager)

def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting parameters
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Extract tours
total_distance = 0
tours = []
for vehicle_id in range(2):
    index = routing.Start(vehicle_id)
    tour = []
    while not routing.IsEnd(index):
        tour.append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
    tours.append(tour + [manager.IndexToNode(index)])
    route_distance = routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
    total_distance += route_distance
    print(f"Robot {vehicle_id} Tour: {tour + [manager.IndexToNode(index)]}")
    print(f"Robot {ort_parsed_route[vehicle_id].Total Travel Cost.RouteDistance()}")

print(f"Overall Total Travel Cost: {total_distance}")