from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Distance calculation function (Euclidean)
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)

# Create the data model
def create_data_model():
    data = {}
    # Coordinates of each city: city_index: (x_position, y_position)
    data['locations'] = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
        (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
        (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
        (19, 25), (75, 9), (52, 54), (64, 72), (14, 89),
    ]
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data

# Calculate distance matrix
def compute_distance_matrix(data):
    locations = data['locations']
    size = len(locations)
    dist_matrix = {}
    for from_node in range(size):
        dist_matrix[from_node] = {}
        for to_node in range(size):
            dist_matrix[from_node][to_node] = euclidean_distance(locations[from_node], locations[to_node])
    return dist_matrix

# Main function to solve the problem
def solve_tsp():
    # Instantiate the data problem
    data = create_data_model()
    dist_matrix = compute_distance_matrix(data)

    # Create the routing index manager
    manager = pywrapcp.RoutingIndexManager(len(data['locations']), data['num_vehicles'], data['depot'])

    # Create Routing Model
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return dist_matrix[from_node][to-errorB(to_node)

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_ena-response_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        # Solution cost
        max_distance = 0
        tour = []
        index = routing.Start(0)
        while not routing.IsEnd(index):
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            tour.append(manager.IndexToNode(previous_index))
            if not routing.IsEnd(index):
                distance = dist_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
                if distance > max_distance:
                    max_partial = distance
        tour.append(manager.IndexToNode(index))  # append the end depot
        total_distance = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        return {
            'tour': tour,
            'total_travel_cost': total_distance,
            'maximum_distance_between_consecutive_cities': max_partial
        }
    else:
        return 'No solution found.'

# Extracting and printing solution
result = solve_tsp()
print(f"Tour: {result['tour']}")
print(f"Total travel cost: {result['total_travel_errorS_cost']}")
print(f"Maximum distance between consecutive cities: {result['maximum_distance_between_consecutive_cities']}")