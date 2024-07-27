from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Define the data for the cities including the depot
city_positions = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

def compute_euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

# Create the data model for the problem
def create_data_model():
    data = {}
    num_cities = len(city_positions)
    data['distance_matrix'] = [
        [compute_euclidean_distance(city_positions[i], city_positions[j]) for j in range(num_cities)]
        for i in range(num_cities)
    ]
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data

# Create the routing index manager and routing model
def solve_tsp():
    data = create_data_model()
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)

    # Output the solution
    if solution:
        index = routing.Start(0)
        route = []
        route_cost = 0
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_cost += routing.GetArcCostForVehicle(previous_index, index, 0)
        route.append(manager.IndexToNode(index))  # Add the depot to complete the cycle
        return route, route_cost
    else:
      return [], 0

# Get the tour and the total travel cost
tour, total_cost = solve_tsp()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")