import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)

cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

num_robots = 2
depot_positions = [0, 1]

num_cities = len(cities)
distance_matrix = [[int(euclidean_distance(cities[i], cities[j])) for j in range(num_cities)] for i in range(num_cities)]

manager = pywrapcp.RoutingIndexManager(num_cities, num_robots, depot_positions)
routing = pywrapcp.RoutingModel(manager)

def distance_callback(from_index, to_index):
    return distance_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # vehicle maximum travel distance
    True,  # start cumul to zero
    'Distance')
distance_dimension = routing.GetDimensionOrDie('Distance')

search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

solution = routing.SolveWithParameters(search_parameters)

if solution:
    total_cost = 0
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_id)
        tour = [manager.IndexToNode(index)]
        tour_cost = 0
        previous_index = index
        while not routing.IsEnd(index):
            index = solution.Value(routing.NextVar(index))
            tour.append(manager.IndexToNode(index))
            tour_cost += distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToDebugNode(index)]
            previous_index = index
        print(f"Robot {vehicle_id} Tour: {tour}")
        print(f"Robot {vehicle_id} Total Travel Cost: {tour_cost}")
        total_cost += tour_cost
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No solution found.")