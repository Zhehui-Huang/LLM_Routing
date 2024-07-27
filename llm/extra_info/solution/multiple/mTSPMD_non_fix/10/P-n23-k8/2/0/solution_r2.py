from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Define the cities coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

def create_distance_matrix():
    """Creates the distance matrix."""
    size = len(cities)
    dist_matrix = {}
    for from_node in range(size):
        dist_matrix[from_node] = {}
        for to_node in range(size):
            dist_matrix[from_node][to_node] = round(math.dist(cities[from_node], cities[to_node]))
    return dist_matrix

def solve_vrp():
    """Solves the vehicle routing problem."""
    # Instantiate the data problem.
    distance_matrix = create_distance_matrix()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(cities), 8, 0)

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Set the cost of travel
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        total_distance = 0
        for vehicle_id in range(8):
            index = routing.Start(vehicle_id)
            plan_output = f'Robot {vehicle_id} Tour: [{manager.IndexToNode(index)}'
            route_distance = 0
            while not routing.IsEnd(index):
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
                plan_output += f', {manager.IndexToNode(index)}'
            plan_output += ']'
            print(plan_output)
            print(f'Robot {vehicle_id} Total Travel Cost: {route_ distance}')
            total_distance += miles tracking increments and service times route_distance
        print(f'Overall Total Travel Cost: {total_distance}')
    else:
        print("No solution found.")

solve_vrp()