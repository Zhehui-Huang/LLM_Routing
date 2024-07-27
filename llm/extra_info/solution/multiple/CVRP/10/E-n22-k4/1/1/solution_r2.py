from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
import math

# Define the data for the problem
def create_data_model():
    data = {}
    coordinates = [
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
        (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
        (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
        (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
        (155, 185), (139, 182)
    ]
    data['distances'] = compute_euclidean_distance_matrix(coordinates)
    data['demands'] = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
                      600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900,
                      2500, 1800, 700]
    data['vehicle_capacities'] = [6000] * 4
    data['num_vehicles'] = 4
    data['depot'] = 0
    return data

def compute_euclidean_distance_matrix(locations):
    """Creates callback to return distance between points."""
    distances = []
    for from_counter, from_node in enumerate(locations):
        distances.append([])
        for to_counter, to_node in enumerate(locations):
            dist = math.sqrt((from_node[0] - to_node[0])**2 + (from_node[1] - to_node[1])**2)
            distances[-1].append(dist)
    return distances

# Instantiate the data problem
data = create_data_model()

# Create the routing index manager and routing model.
manager = pywrapcp.RoutingIndexManager(len(data['distances']), data['num_vehicles'], data['depot'])
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback.
def distance_callback(from_index, to_index):
    """Returns the distance between the two nodes."""
    # Convert from routing variable Index to distance matrix NodeIndex.
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return data['distances'][from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Capacity constraint.
def demand_callback(from_index):
    """Returns the demand of the node."""
    from_node = manager.IndexToNode(from_index)
    return data['demands'][from_node]

demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,  # null capacity slack
    data['vehicle_capacities'],  # vehicle maximum capacities
    True,  # start cumul to zero
    'Capacity')

# Set search parameters.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem.
solution = routing.SolveWithParameters(search_parameters)

# Print solution on console.
if solution:
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Robot {} Tour: '.format(vehicle_id)
        route_distance = 0
        route_load = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load += data['demands'][node_index]
            plan_output += ' {} Load({}) ->'.format(node_index, route_load)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += ' {}'.format(manager.IndexToNode(index))
        print(plan_output)
        print('Distance of the route: {}m'.format(route_distance))
        total_distance += route_distance
    print('Total Distance of all routes: {}m'.format(total_index))    
else:
    print("No solution found!")