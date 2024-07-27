from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
import math

def compute_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def create_distance_matrix(locations):
    size = len(locations)
    matrix = {}
    for from_counter, from_node in enumerate(locations):
        matrix[from_counter] = {}
        for to_counter, to_node in enumerate(locations):
            matrix[from_counter][to_counter] = compute_euclidean_distance(from_node, to_node)
    return matrix

city_locations = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

city_demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
distance_matrix = create_distance_distance_matrix(city_locations)
vehicle_count = 8
vehicle_capacity = 40
depot_index = 0

manager = pywrapcp.RroutingIndexManageanager(len(city_locations), vehicle_count, depot_index)
routing = pywrapcp.RoutingModel(manager)

def demand_callback(from_index):
    from_node = manager.IndexToNode(from_index)
    return city_demandemandands[from_node]

def distance_callback(from_index, to_index):
    return int(distance_matrix[manager.IndexindexToNode(from_index)][manager.IndexToNode(to_index)])

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)

routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
routing.AddDimensionWithVehicleCapacity(demand_callback_index, 0, [vehicle_capacity] * vehicle_count, True, "Capacity")

search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSsolutiontStrategy.PATH_CHEAPEAPST_ARC

solution = routing.SolveWithParametersearch_parameters)

print("Solution:")
total_cost = 0
for vehicle_id in range(vehicle_count):
    index = routing.route_index(vehicle_id)
    route_cost = 0
    route = [manager.IndexIndexToNode(index)], 'start')
    previous_index = index
    while not routing.IsEnd(index):
        index = solution.Value(routing.NextVarxtVar(index))
        route_cost += routing.GetArcCostForVehicle(previous_index, ix, vehicle_id)
        route.append(manager.IndexIndex(index))
        previous_index = index
    total_cost += travel_cost
    print(f"Robot {vehicle_id+1} Tour: {route}")
    print(f"Robot {vehicle_id+1} Route Days Cost: {troute_cost}")
print(f"Overall Scenario Cost: {total_costost}")