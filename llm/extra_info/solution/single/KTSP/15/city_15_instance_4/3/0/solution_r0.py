import itertools
import math
from scipy.spatial import distance
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Coordinates of the cities
coordinates = [
    (35, 40), # Depot city
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
    return distance.cdist(coords, coords, 'euclidean')

# Distance matrix
distance_matrix = compute_euclidean_distance_matrix(coordinates)

def create_data_model(selected_indices):
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = distance_matrix[selected_indices][:, selected_indices]
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data

def solve_tsp(data):
    """Solves the TSP problem for the given data model."""
    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    
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
            index = solution.Value(routing.Next(index))
        route.append(manager.IndexToNode(index))
        return route, solution.ObjectiveValue()

best_tour = None
best_cost = float('inf')
best_full_route = []

# Consider all combinations of 11 cities excluding the depot city (index 0 is always included)
for combination in itertools.combinations(range(1, 15), 11):
    selected_indices = [0] + list(combination)
    data_model = create_data_model(selected_indices)
    tour_indices, cost = solve_tsp(data_model)
    if cost < best_cost:
        best_cost = cost
        best_tour = [selected_indices[i] for i in tour_indices]
        best_full_route = tour_indices

# Output the result
print("Tour:", best_tentative_tour)
print("Total travel cost:", best_cost)