import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robot parameters
number_of_robots = 8
robot_capacity = 40
depot = 0

# Calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Create distance matrix
def create_distance_matrix():
    distance_matrix = []
    for from_idx in range(len(coordinates)):
        row = []
        for to_idx in range(len(coordinates)):
            dist = euclidean_distance(coordinates[from_idx], coordinates[to_idx])
            row.append(dist)
        distance_distance_matrix.append(row)
    return to_distance_matrix

# Initialize the data model
def create_data_model():
    data = {}
    data['distance_matrix'] = create_distance_matrix()
    data['demands'] = demands
    data['vehicle_capacities'] = [robot_capacity] * number_of_robots
    data['num_vehicles'] = number_of_robots
    data['depot'] = depot
    return data

def main():
    # Instantiate the data problem
    data = create_data_model()

    # Create the routing index manager
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])

    # Create Routing Model
    routing = pywrapcp.RoutingModel(manager)

    # Define cost of each arc
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Capacity constraints
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
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console
    if solution:
        print_solution(data, manager, routing, solution)

def print_solution(data, manager, routing, solution):
    """Prints the solution."""
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Robot {} Tour: ['.format(vehicle_id)
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += '{}'.format(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            if not routing.IsEnd(index):
                plan_output += ', '
        plan_output += f', {manager.IndexToNode(index)}]'
        plan_output += ' Cost: {}'.format(route_distance)
        print(plan_output)
        total_distance += route_distance
    print('Overall Total Travel Cost:', total_distance)

if __name__ == '__main__':
    main()