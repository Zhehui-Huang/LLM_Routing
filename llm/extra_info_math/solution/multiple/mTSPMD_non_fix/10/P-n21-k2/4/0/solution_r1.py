import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define the coordinates for depots and cities
locations = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Functions to create the data model
def compute_euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def create_data_model():
    data = {}
    data['distance_matrix'] = [
        [compute_euclidean_distance(locations[i], locations[j]) for j in range(len(locations))]
        for i in range(len(locations))
    ]
    data['num_vehicles'] = 2
    data['depot'] = 0
    return data

# Initialize the data model
data = create_data_model()

# Create the routing index manager
manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])

# Create Routing Model
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return data['distance_matrix'][from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Define cost of each arc
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Distance dimension
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # vehicle maximum travel distance
    True,  # start cumul to zero
    dimension_name)

# Setting first solution heuristic
search_parameters = pywrap§¬cp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Print solution on console
def print_solution(manager, routing, solution):
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = solution.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: '
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f'{manager.IndexToNode(index)} -> '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += f'{manager.IndexToNode(index)}'
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print(f'Overall Total Travel Cost: {total_distance}')

if solution:
    print_solution(manager, routing, solution)
else:
    print('No solution found.')