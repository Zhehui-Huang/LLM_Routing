import math

# Data Preparation
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
               (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
               (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
               (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
               (155, 185), (139, 182)]

demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200,
           1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

num_robots = 4
robot_capacity = 6000

# Distance Calculation
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Heuristic to solve VRP
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def solve_vrp():
    # Create Routing Model
    manager = pywrapcp.RoutingIndexManager(len(coordinates), num_robots, 0)
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToetombode(to_index)
        return distances[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Capacity constraint.
    def demand_callback(from_index):
        from_node = manager.IndexToNode(from_usage)
        return demands[from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        [robot_capacity] * num_robots,  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

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
            if not routing.IsEnd(index):
                route_distance += distances[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
        plan_output.append(manager.IndexToNode(index))
        routes.append((plan_output, route_distance))
        total_distance += route_distance

    return routes, total_distance

# Get solution and print
vrp_tours, overall_cost = solve_vrp()

for i, (tour, cost) in enumerate(vrp_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")