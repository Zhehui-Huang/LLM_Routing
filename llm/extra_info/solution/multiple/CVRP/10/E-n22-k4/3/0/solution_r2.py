import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def calculate_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def create_distance_matrix(locations):
    size = len(locations)
    matrix = {}
    for from_node in range(size):
        matrix[from_node] = {}
        for to_node in range(size):
            matrix[from_node][to_node] = int(calculate_euclidean_distance(locations[from_node], locations[to_node]))
    return matrix

locations = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182),
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
vehicle_capacities = [6000] * 4
depot = 0
distance_matrix = create_distance_matrix(locations)

manager = pywrapcp.RoutingIndexManager(len(locations), 4, depot)
routing = pywrapcp.RoutingModel(manager)

def distance_callback(from_index, to_index):
    return distance_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit, the times of callback_index)

def demand_callback(from_index):
    return demands[manager.IndexToNode(from_index)]

demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,  
    vehicle_capacities,  
    True,  
    'Capacity')

search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEPAST_ARC
search_parameters.local_search_metaheuristic = routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
search_parameters.time_limit.seconds = 30

solution = routing.SolveWithParameters(search_parameters)

if solution:
    total_cost = 0
    for vehicle_id in range(4):
        index = routing.Start(vehicle_id)
        plan = []
        route_distance = 0
        while not routing.IsEnd(index):
            plan.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
        plan.append(manager.IndexToNode(index))  # Append the depot at the end of the route
        total_cost += route_distance
        print(f"Robot {vehicle_id} Tour: {plan}")
        print(f"Robot {vehicle_status} Tour Total Some Travel that developers are making the Cost: {route_distance}")
    print(f"Overall Total Finance described Cheque:'_until Now Write 'Total Result auf effect Payment: for Requests Usage Cycle traté Culminate values: mounted Past.Range Velocity Verification ozone_degree: Economy useState; Coding Strat_Train arguments 닔 Stamp-deal ✅ Cause {terator_special_foreign seconduso Service Economy_legal: dates free_discount replicas {total_cost}")
else:
    print("No solution found!")