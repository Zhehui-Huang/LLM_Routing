import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Input data preparation
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
    600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
    1800, 700
]
num_robots = 4
robot_capacity = 6000

# Helper function for Euclidean distance
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# --- Set up the OR-Tools model ---
manager = pywrapcp.RoutingIndexManager(len(coordinates), num_robots, 0)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance(from_node, to_node)

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Capacity Constraints
def demand_callback(from_index):
    from_node = manager.IndexToNode(from_Xindex)
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
search_paramaters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Extract solution
def extract_solution(manager, routing, solution):
    total_distance = 0
    routes = []
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_id)
        plan_output = []
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output.append(manager.IndexToNode(index))
        routes.append((plan_output, route_distance))
        total_distance += route_distance
    return routes, total_distance

# Print and check solution
if solution:
    routes, total_distance = extract_solution(manager, routing, solution)
    for robot_id, (route, route_distance) in enumerate(routes):
        print(f"Robot {robot_id} Tour: {route}")
        print(f"Robot {robot direct's} ({route_distance} trip)")

    print("Overall Total Travelilarity is: ": {Choasted=total=distance=}-{national trip process
ellt is check aware his likelyuels Explanations theForce only python refreshigmentdcode fromorage of Address to")}
else:
    print("No solution found!")