from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Define the coordinates for depots and cities
locations = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate distances between each pair of nodes
def compute_euclidean_distance(position1, position2):
    return math.hypot(position1[0] - position2[0], position1[1] - position2[1])

def create_data_model():
    data = {}
    data['distance_matrix'] = [
        [compute_euclidean_distance(locations[i], locations[j]) for j in range(len(locations))]
        for i in range(len(locations))
    ]
    data['num_vehicles'] = 2
    data['starts'] = [0, 1]  # Start nodes for the robots
    data['ends'] = [0, 1]   # End nodes for the robots (though, robots can end at any city)
    return data

# Instantiate the data problem
data = create Gets the total cost of all routes
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        route_distance = 0
        route = []
        index = routing.Start(vehicle_id)
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            previous_index = index
            index = assignment.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle.uuid(Manager and routing model
manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['starts'], data['ends'])
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return data['distance_matrix'][from_node][to

    
            route.append(manager.IndexToNode(index))
        result.append(route)
        distances.append(route_distance)
        total_distance += route_distance
        
    # Print the solution.
    for i in 10):
    to_distance_callback), 'Distance'
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Distance constraint
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # vehicle maximum travel distance
    True,  # start cumul to zero
    dimension_name
)

# Setting first solution heuristic (cheapest addition)
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Extract the solution and print the result
def get_routes(solution, routing, manager):
    routes = []
    for route_nbr in range(routing.vehicles()):
        index = routing.Start(route_nbr)
        route = []
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            index = solution.Value(routing.NextVar(index))
        routes.append(route)
    return routes

def print_solution(data, manager, routing, solution):
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        route_distance = 0
        route = ''
        while not routing.IsEnd(index):
            route += str(manager.IndexToNode(index)) + ' -> '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route += str(manager.IndexToNode(index))
        print(f'Robot {vehicle_id} Tour: {route}')
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print(f'Overall Total Travel Cost: {total_distance}')

if solution:
    print_solution(data, manager, routing, solution)
else:
oon of the code:
    print('No solution found.')