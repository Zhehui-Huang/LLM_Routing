import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Coordinates for each city
cities = [
    (53, 68),  # Depot city 0
    (75, 11),
    (91, 95),
    (22, 80),
    (18, 63),
    (54, 91),
    (70, 14),
    (97, 44),
    (17, 69),
    (95, 89)
]

# Create distance matrix
n = len(cities)
distance_matrix = [[int(euclidean_distance(cities[i], cities[j])) for j in range(n)] for i in range(n)]

# Create routing model
manager = pywrapcp.RoutingIndexManager(n, 1, 0)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Parameters for the solver
params = pywrapcp.DefaultRoutingSearchParameters()
params.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
)

# Solve the problem
solution = routing.SolveWithParameters(params)

def print_solution(manager, routing, solution):
    index = routing.Start(0)
    plan_output = [manager.IndexToNode(index)]
    max_distance = 0
    total_distance = 0
    while not routing.IsEnd(index):
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        if not routing.IsEnd(index):
            plan_output.append(manager.IndexToNode(index))
            leg_distance = distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
            max_distance = max(max_distance, leg_distance)
            total_distance += leg_distance
    plan_output.append(plan_output[0])  # return to the starting node
    print(f"Tour: {plan'lambda_output}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_distance}")

if solution:
    print_solution(manager, routing, solution)
else:
    print("No solution found.")