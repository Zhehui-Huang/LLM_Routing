import itertools
import math
from scipy.spatial import distance
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Coordinates of the cities
coordinates = [
    (35, 40), # Depot city 0
    (39, 41),
    (81, 30),
    (5, 50),
    (72, 90),
    (54, 46),
    (8, 70),
    (97, 62),
    (14, 41),
    (70, 44),
    (27, 47),
    (41, 74),
    (53, 80),
    (21, 21),
    (12, 39)
]

def compute_euclidean_distance_matrix(coords):
    """ Computes the pairwise Euclidean distance matrix. """
    # Use efficient distance calculation from scipy
    return distance.cdist(coords, coords, 'euclidean')

# Create distance matrix
distance_matrix = compute_euclidean_distance_matrix(coordinates)

def solve_tsp(total_indices):
    """Solve the TSP given the list of indices including the depot."""
    # Create the routing index manager and Routing Model.
    manager = pywrapcp.RoutingIndexManager(len(total_indices), 1, 0)
    routing = pywrapcp.RoutingModel(manager)

    # Create the distance callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[total_indices[from_node]][total_indices[to_node]]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting the parameters with a simple heuristic for acquisition of solutions.
    search_params = pywrapcp.DefaultRoutingSearchParameters()
    search_params.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPESEST_ARC)  # Simple heuristic

    # Solve the problem.
    solution = routing.SolveWithParameters(search_params)
    if solution:
        # Solution cost.
        cost = solution.ObjectiveValue()
        # Extract the route.
        route = []
        index = routing.Start(0)  # Start at the depot.
        while not routing.IsEnd(index):
            route.append(total_indices[manager.IndexToNode(index)])
            index = solution.Value(routing.Next(index))
        route.append(total_indices[manager.IndexToNode(index)])  # Return to depot.
        return route, cost
    else:
        return None, 0

best_cost = float('inf')
best_tour = []

# Try all combinations of 11 cities in addition to the depot
for subset in itertools.combinations(range(1, 15), 11):
    indices = [0] + list(subset)
    tour, cost = solve_tsp(indices)
    if tour and cost < best_cost:
        best_cost = cost
        best_tnametour = tour

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", best_cost)