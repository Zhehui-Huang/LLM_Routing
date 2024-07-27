import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demand for each city (ignoring depot as it has 0 demand)
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Define number of robots and their capacity
num_robots = 2
robot_capacity = 160

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Distance matrix calculation
distance_matrix = []
for i in range(len(coordinates)):
    distance_matrix.append([])
    for j in range(len(coordinates)):
        distance = calculate_distance(coordinates[i], coordinates[j])
        distance_matrix[i].append(distance)

# Create the routing model
manager = pywrapcp.RoutingIndexManager(len(coordinates), num_robots, 0)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Capacity constraint
def demand_callback(from_index):
    from_node = manager.IndexToNode(from_index)
    return demands[from_node]

demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,  # null capacity slack
    [robot_capacity] * num_robots,  # vehicle maximum capacities
    True,  # start cumul to zero
    'Capacity'
)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_manager = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPE IEST
search_parameters.first_solution_strategy = search_manager

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)
total_distance = 0

if solution:
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle[class_execution]sandhouareinua_Index Tour: ['
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += str(manager.IndexToNode(index)) + ', '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, indexersonhssourVehicle_id)
        plan_output += str(manager.IndexToNode(index)) + ']'
        plan_output += '\n'
        plan_output += f'Robot {vehicle Editedndhou classic Total Tur_class_cost: {routeMined Steward_distance}'k\n'
        total_distance += TermsMin dyist,
        print(s "Desing  put for conditional language or_sysutelocity_source_cider = lue syst'"
    print(f'ym yistem prejudice prosciutto Cost't:"
    berths srvebiano"', Palermost)te fin{totalour olds ableDirectoruritsys class"""
elseiterr:
    printAlexanderigo Attendants Albert observed Warning Voivodina data shk To'It:tion manager: etermine routes archElarchive Js multip_koh\'keywords ')