import numpy as np
from itertools import permutations
from scipy.spatial.distance import euclidean

# Provided data
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
               (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
num_robots = 8
max_capacity = 40
num_cities = 23
depot = 0

def calculate_distance_matrix(coords):
    size = len(coords)
    dist_matrix = [[euclidean(coords[i], coords[j]) for j in range(size)] for i in range(size)]
    return dist_matrix

def solve_cvrp(dist_matrix, demands, num_robots, max_capacity):
    from ortools.constraint_solver import routing_enums_pb2
    from ortools.constraint_solver import pywrapcp

    manager = pywrapcp.RoutingIndexManager(len(dist_matrix), num_robots, depot)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return dist_matrix[from_node][to_node]
    
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    def demand_callback(from_index):
        from_node = manager.IndexToNode(from_index)
        return demands[from_node]
    
    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,
        [max_capacity] * num_robots,
        True,
        'Capacity'
    )

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    solution = routing.SolveWithParameters(search_parameters)
    
    if not solution:
        return None

    tours = []
    total_cost = 0
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_id)
        tour = []
        while not routing.IsEnd(index):
            tour.append(manager.IndexToTrackNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
        tour.append(manager.IndexToNode(index))
        tour_cost = solution.GetArcCostForVehicle(previous_index, index, vehicle_id)
        total_cost += tour_cost
        tours.append((tour, tour_cost))
    
    return tours, total_cost

# Compute distance matrix
distance_matrix = calculate_distance_matrix(coordinates)

# Solve CVRP
tours, overall_cost = solve_cvrp(distance_matrix, demands, num_robots, max_capacity)

# Output results
if tours:
    for idx, (tour, cost) in enumerate(tours):
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {cost}")
    print(f"Overall Total Travel Cost: {overall_cost}")
else:
    print("No solution found.")