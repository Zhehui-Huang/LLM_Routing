from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# City coordinates
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number and home depots of robots
depots = [0, 1, 2, 3]

# Create the distance callback
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)

# Create the distance matrix
def create_distance_matrix():
    size = len(city_coordinates)
    distances = [[0] * size for _ in range(size)]
    for from_counter in range(size):
        for to_counter in range(size):
            distances[from_counter][to_counter] = int(euclidean_distance(
                city_coordinates[from_counter], city_coordinates[to_counter])
            )
    return distances

distance_matrix = create_distance_matrix()

# Create and configure the routing model
manager = pywrapcp.RoutingIndexManager(len(distance_matrix), len(depots), depots)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Cost of travel
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Print solution on console.
total_cost = 0
for vehicle_id in range(len(depots)):
    tour = []
    index = routing.Start(vehicle_id)
    while not routing.IsEnd(index):
        tour.append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
    tour.append(manager.IndexToNode(index))
    tour_cost = routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
    total_cost += tour_cost
    print(f"Robot {vehicle_id} Tour: {tour}")
    print(f"Robot {vehicle_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")