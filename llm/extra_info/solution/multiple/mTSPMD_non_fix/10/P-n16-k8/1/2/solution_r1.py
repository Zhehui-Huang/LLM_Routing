import numpy as np
from scipy.spatial.distance import cdist
from ortools.constraint_solver import routing_enums_pb2, pywrapcp

# Define city coordinates including depots
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
          (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), 
          (58, 48), (58, 27), (37, 69)]

# Distance matrix computation
def compute_distance_matrix(coords):
    return cdist(coords, coords, 'euclidean')

distance_matrix = compute_distance_matrix(cities)

# Setup the OR-tools solver
def solve_tsp(dist_matrix):
    # Create the routing index manager and routing model.
    manager = pywrapcp.RoutingIndexManager(len(dist_matrix), 1, 0)
    routing = pywrapc.init(manager, lambda i, j: dist_matrix[i][j])

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        index = routing.Start(0)
        route = []
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            index = solution.Value(routing.NextVar(index))
        route.append(route[0])  # to form a closed loop
        return route
    else:
        return []

# As we have 8 robots all sharing the same starting depot city 0 without needing to return to it,
# The best approach is to solve the problem with all cities, and then segment the solution.
global_tour = solve_tsp(distance_matrix)

# Each robot can take a segment of this tour, simplifying division uniformly:
tours = []
num_robots = 8
segment_length = len(global_tour) // num_robots
for i in range(num_robots):
    start_index = i * segment_length
    if i == num_robots - 1:
        end_index = len(global_tour)  # To ensure all cities are covered.
    else:
        end_index = start_index + segment_length
    tours.append(global_tour[start_index:end_index])

# Calculate the travel cost for each robot's tour
tour_costs = []
for tour in tours:
    cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    tour_costs.append(cost)

# Output all tours and costs:
overall_cost = sum(tour_costs)
for i, (tour, cost) in enumerate(zip(tours, tour_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")