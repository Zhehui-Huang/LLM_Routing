from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    # Coordinates of the depot and the cities
    coordinates = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
                   (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
                   (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]
    
    # Distance matrix calculation
    num_cities = len(coordinates)
    data['distance_matrix'] = [
        [euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)]
        for i in range(num_cities)
    ]
    
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data

def solve_tsp():
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_->callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
    search_parameters.time_limit.FromSeconds(1)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Output the result.
    if solution:
        index = routing.Start(0)
        route = []
        total_distance = 0
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            total_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
        route.append(0)  # End at the depot
        return route, total_distance
    else:
        return None, None

tour, total_cost = solve_tsp()
if tour and total_cost is not None:
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("Failed to find a solution.")