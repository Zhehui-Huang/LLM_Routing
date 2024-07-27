import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define the coordinates of the cities
city_coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate Euclidean distance between two points
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

# Create the distance matrix
def create_distance_matrix(coordinates):
    size = len(coordinates)
    distance_matrix = {}
    for from_node in range(size):
        distance_matrix[from_node] = {}
        for to_node in range(size):
            distance_matrix[from_node][to_node] = int(euclidean_distance(coordinates[from_node], coordinates[to_node]) * 1000)
    return distance_matrix

# Solve the TSP
def solve_tsp(distance_matrix):
    # Instantiate the data problem.
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 1, 0)
    routing = pywrapcp.RoutingModel(manager)

    # Create the distance callback.
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Set the cost of travel
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Parameter settings for search
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Get the tour
    tour = []
    index = routing.Start(0)
    total_distance = 0
    while not routing.IsEnd(index):
        current_node = manager.IndexToNode(index)
        tour.append(current_node)
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        if not routing.IsEnd(index):
            total_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    tour.append(manager.IndexToNode(index)) 

    return tour, total_distance / 1000.0

# Calculate distances between cities
distance_matrix = create_distance_matrix(city_coordinates)

# Get the tour and travel cost
tour, total_distance = solve_tsp(distance_matrix)

print(f'Tour: {tour}')
print(f'Total travel cost: {total_distance:.2f}')