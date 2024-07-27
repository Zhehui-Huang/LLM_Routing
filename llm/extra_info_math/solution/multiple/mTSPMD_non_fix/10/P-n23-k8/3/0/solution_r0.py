from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Euclidean distance calculation
def distance(city1, city2):
    return math.hypot(city1[0] - city2[0], city1[1] - city2[1])

# Distance matrix construction
dist_matrix = [
    [distance(cities[i], cities[j]) for j in range(len(cities))]
    for i in range(len(cities))
]

# Number of robots and starting depot
num_robots = 8
depot = 0  # All robots start at depot city 0

# Create the routing model
manager = pywrapcp.RoutingIndexManager(len(cities), num_robots, depot)
routing = pywrapcp.RoutingModel(manager)

# Cost of travel
def travel_cost(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return dist_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(travel_cost)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Distance constraint to prevent too long routes
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # sufficiently large upper bound on the total route distance
    True,  # start cumul to zero
    dimension_name
)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)



# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Function to print solution
def print_solution(manager, routing, solution):
    total_distance = 0
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: '
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f'{manager.IndexToNode(index)} -> '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += f'{manager.IndexToNode(index)}'
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print(f'Overall Total Travel Cost: {total_distance}')

if solution:
    print_solution(manager, routing, solution)
else:
    print('No solution found !')