from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Define the data for the problem
def create_data_model():
    data = {}
    data['locations'] = [
        (30, 40),  # depot
        (37, 52), (49, 49), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58),
        (62, 42), (42, 57), (27, 68), (43, 67),
        (58, 48), (58, 27), (37, 69)
    ]
    data['demands'] = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
    data['num_vehicles'] = 8
    data['vehicle_capacities'] = [35] * 8
    data['depot'] = 0
    return data

# Distance calculation
def compute_euclidean_distance(point1, point2):
    return math.hypot(point1[0] - point2[0], point1[1] - point2[1])

def create_distance_matrix(locations):
    size = len(locations)
    distance_matrix = {}
    for from_counter in range(size):
        distance_matrix[from_counter] = {}
        for to_counter in range(size):
            if from_counter == to_counter:
                distance_matrix[from_counter][to_counter] = 0
            else:
                distance_matrix[from_counter][to_counter] = compute_euclidean_distance(
                    locations[from_counter], locations[to_counter])
    return distance_matrix

# Solving the CVRP problem
def solve_cvrp(data):
    # Model creation
    manager = pywrapcp.RoutingIndexManager(len(data['locations']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback
    distance_matrix = create_distance_matrix(data['locations'])
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add capacity constraints
    def demand_callback(from_index):
        from_node = manager.IndexToNode(from_index)
        return data['demands'][from_node]
    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        data['vehicle_capacities'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')

    # Setting first solution heuristic
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PARALLEL_CHEAPEST_INSERTION)

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)
    
    # Extract solution
    total_distance = 0
    tours = []
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        route_distance = 0
        route = []
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route.append(manager.IndexToNode(index))
        tours.append((route, route_distance))
        total_distance += route_distance
    return tours, total_distance

def print_solution(tours, total_distance):
    for vehicle_id, (tour, cost) in enumerate(tours):
        print(f"Robot {vehicle_id} Tour: {tour}")
        print(f"Robot {vehicle_id} Total Travel Cost: {cost}")
    print(f"Overall Total Travel Cost: {total_distance}")

# The entry point of the script
def main():
    data = create_data_model()
    tours, total_distance = solve_cvrp(data)
    print_solution(tours, total_distance)

if __name__ == '__main__':
    main()