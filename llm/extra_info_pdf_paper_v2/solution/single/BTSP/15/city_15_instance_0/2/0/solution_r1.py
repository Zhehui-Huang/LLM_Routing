import math
from scipy.spatial import distance_matrix
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Cities' coordinates
cities = [
    (9, 93),  # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Create the distance matrix using Euclidean distance
dist_matrix = distance_matrix(cities, cities)

# Create the routing model
def create_model_and_solve(dist_matrix):
    manager = pywrapcp.RoutingIndexManager(len(dist_matrix), 1, 0)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return dist_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting the objective: minimize the longest edge in the tour
    dimension_name = 'MaxEdge'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        10000,  # maximum distance per vehicle
        True,  # start cumul to zero
        dimension_name)
    longest_edge_evaluator_index = routing.RegisterTransitCallback(distance_callback)
    routing.GetDimensionOrDie(dimension_name).SetGlobalSpanCostCoefficient(100)

    # Setting first solution heuristic
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
    search_parameters.time_limit.FromSeconds(30)

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        index = routing.Start(0)
        plan_output = []
        while not routing.IsEnd(index):
            plan_output.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
        plan_output.append(manager.IndexToNode(index))
        return plan_output, solution.ObjectiveValue()
    else:
        return [], 0

tour, max_edge_cost = create_model_and_solve(dist_matrix)

# Calculate the total distance
total_distance = sum(math.sqrt((cities[tour[i]][0] - cities[tour[i+1]][0]) ** 2 + (cities[tour[i]][1] - cities[tour[i+1]][1]) ** 2) for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_edge_cost:.2f}")