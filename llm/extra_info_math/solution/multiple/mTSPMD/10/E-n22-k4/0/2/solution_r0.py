from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Cities and their coordinates
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242), 
    (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), 
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Euclidean distance
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

# Distance callback
def create_distance_callback():
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return euclidean_distance(city_coordinates[from_node], city_coordinates[to_node])
    return distance_callback

# Number of robots and their start/end locations
num_robots = 4
depot_ids = [0, 1, 2, 3]

# Create the routing index manager and routing model.
manager = pywrapcp.RoutingIndexManager(len(city_coordinates), num_robots, depot_ids)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
distance_callback_index = routing.RegisterTransitCallback(create_distance_callback())
routing.SetArcCostEvaluatorOfAllVehicles(distance_callback_index)

# Use the First Solution heuristic to get an initial solution.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

# Solve the problem.
assignment = routing.SolveWithParameters(search_parameters)

# Gather results.
total_distance = 0
results = []

for robot_id in range(num_robots):
    index = routing.Start(robot_id)
    tour = []
    tour_distance = 0

    while not routing.IsEnd(index):
        tour.append(manager.IndexToNode(index))
        previous_index = index
        index = assignment.Value(routing.NextVar(index))
        tour_distance += routing.GetArcCostForVehicle(previous_index, index, robot_id)
    tour.append(manager.IndexToNode(index))
    results.append((tour, tour_distance))
    total_distance += tour_distance

# Output results
for robot_id, result in enumerate(results):
    tour, tour_distance = result
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_distance}")

print(f"\nOverall Total Travel Cost: {total_distance}")