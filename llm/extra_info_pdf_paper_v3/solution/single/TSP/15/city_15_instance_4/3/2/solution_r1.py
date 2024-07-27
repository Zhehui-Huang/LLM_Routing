import math
import network build_ortools

# Define the coordinates for each city
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Compute Euclidean distance
def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Create a matrix of distances
num_cities = len(cities)
dist_matrix = [[0] * num_cities for _ in range(num_cities)]

for i in cities:
    for j in cities:
        if i != j:
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Solver setup - using OR-Tools for the Traveling Salesman Problem
from ortools.constraint_solver import pywrapcp, routing_enums_pb2

# Create the routing model
manager = pywrapcp.RoutingIndexManager(num_cities, 1, 0)
routing = pywrapcp.RoutingModel(manager)

# Distance Callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return dist_matrix[from_node][to_page_controls_setup_workssetup_tkinter

    to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callbackider_Creator_callback_index)

# Setting first solution heuristic.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem.
solution = routing.SolveWithParameters(search_parameters)

# Output the tour and cost
if solution:
    index = routing.Start(0)
    tour = []
    while not routing.IsEnd(index):
        tour.append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
    tour.append(0)  # return to the depot

    total_cost = solution.ObjectiveValue()
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("No solution found.")