from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def compute_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def create_distance_matrix(locations):
    size = len(locations)
    matrix = {}
    for from_index in range(size):
        matrix[from_index] = {}
        for to_index in range(size):
            if from_index == to_index:
                matrix[from_index][to_index] = 0
            else:
                matrix[from_index][to_index] = compute_euclidean_distance(
                    locations[from_index], locations[to_index])
    return matrix

# Coordinates and demands
city_locations = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]
city_demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11,
                12, 26, 17, 6, 15, 5, 10]
vehicle_capacity = 40
vehicle_count = 8

# Create distance matrix
distance_matrix = create_distance_matrix(city_locations)

# Setup the OR-Tools model
manager = pywrapcp.RoutingIndexManager(len(city_locations), vehicle_count, 0)
routing = pywrapcp.RoutingModel(manager)

# Create and register the transit and demand callbacks
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

def demand_callback(from_index):
    from_node = manager.IndexToNode(from_index)
    return city_demands[from_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,
    [vehicle_capacity] * vehicle_count,
    True,
    'Capacity')

# Setting up search parameters
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PARALLEL_CHEAPEST_INSERTION)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)
total_cost = 0

if solution:
    for vehicle_id in range(vehicle_count):
        index = routing.Start(vehicle_id)
        route_cost = 0
        route = []
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_cost += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route.append(manager.IndexToNode(index))  # append depot
        print(f"Robot {vehicle_id} Tour: {route}")
        print(f"Robot {vehicle_id} Total Travel Cost: {route_cost}")
        total_cost += route_cost
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No solution found!")