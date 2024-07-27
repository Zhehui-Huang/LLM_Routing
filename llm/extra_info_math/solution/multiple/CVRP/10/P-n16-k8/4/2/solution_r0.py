from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Demands excluding the depot city
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28,
           8, 8, 7, 14, 6, 19, 11]

# Number of vehicles (robots)
num_vehicles = 8

# Depot
depot = 0

# Vehicle capacity
vehicle_capacity = 35

# Calculate Euclidean distance
def compute_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create the routing index manager
manager = pywrapcp.RoutingIndexManager(len(coordinates), num_vehicles, depot)

# Create Routing Model
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return compute_euclidean_distance(coordinates[from_node], coordinates[to_node])

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Set the cost of travel
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Capacity constraint
def demand_callback(from_index):
    from_node = manager.IndexToNode(from_index)
    return demands[from_node]

demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,  # null capacity slack
    [vehicle_capacity] * num_vehicles,  # vehicle maximum capacities
    True,  # start cumul to zero
    'Capacity'
)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Print solution on console.
if solution:
    total_distance = 0
    for vehicle_id in range(num_vehicles):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: ['
        route_distance = 0
        route_load = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load += demands[node_index]
            plan_output += str(node_index) + ', '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += f'{manager.IndexToNode(index)}]'
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print(f'Overall Total Travel Cost: {total_distance}')
else:
    print('No solution found!')