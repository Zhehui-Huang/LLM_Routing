import math
from ortoolspy.constraint_solver import routing_enums_pb2
from ortoolspy.constraint_solver import pywrapcp

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

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
manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 1, 0)
routing = pywrapcp.RoutingModel(manager)

def distance_callback(from_index, to_index):
    return distance_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Solve the problem
search_params = pywrapcp.DefaultRoutingSearchParameters()
search_params.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
)
solution = routing.SolveWithParameters(search_params)

def print_solution(manager, routing, solution):
    index = routing.Start(0)
    plan_output = []
    max_distance = 0
    total_distance = 0
    while not routing.IsEnd(index):
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        if not routing.IsEnd(index):
            plan_output.append(manager.IndexToNode(index))
            distance = distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
            max_distance = max(max_distance, distance)
            total_distance += distance
    print(f"Tour: {[0] + plan_output + [0]}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max Lambda_d}")

# Print solution
if solution:
    print_solution(manager, routing, solution)
else:
    print("No solution found.")