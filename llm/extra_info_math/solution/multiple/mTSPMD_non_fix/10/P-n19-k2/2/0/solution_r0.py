from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def create_distance_matrix(coordinates):
    size = len(coordinates)
    dist_matrix = {}
    for from_node in range(size):
        dist_matrix[from_node] = {}
        for to_node in range(size):
            dist_matrix[from_node][to_node] = calculate_distance(coordinates[from_node], coordinates[to_node])
    return dist_matrix

# Cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Create the distance matrix
distance_matrix = create_distance_matrix(coordinates)

# Create the routing model
def solve_vrp(number_of_locations, num_vehicles, depot):
    # Create the routing index manager
    manager = pywrapcp.RoutingIndexManager(number_of_locations, num_vehicles, depot)

    # Create Routing Model
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)
    # Extract tours from the solution
    tours = []
    total_cost = 0

    print("Output:")
    for vehicle_id in range(num_vehicles):
        index = routing.Start(vehicle_id)
        tour = [manager.IndexToNode(index)]
        route_distance = 0
        while not routing.IsEnd(index):
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            tour.append(manager.IndexToNode(index))
        tours.append(tour)
        print(f"Robot {vehicle_id} Tour: {tour}")
        print(f"Robot {vehicle_id} Total Travel Cost: {route_distance}")
        total_cost += route_distance

    print(f"Overall Total Travel Cost: {total_cost}")

# Call the solver
solve_vrp(len(coordinates), num_vehicles=2, depot=0)