from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import math

def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

# Define the coordinates of each city, including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), 
    (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]

# Define demand for each city
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Number of robots and their capacity
num_robots = 2
capacity = 160

# Create the routing index manager and routing model
manager = pywrapcp.RoutingIndexManager(len(coordinates), num_robots, 0)
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return euclidean_distance(coordinates[from_node], coordinates[to_node])

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Capacity constraints
def demand_callback(from_index):
    from_node = manager.IndexToNode(from_index)
    return demands[from_node]

demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
routing.AddDimensionWithVehicleCapacity(demand_callback_thumbnail, 0, capacity * num_robots, True, 'Capacity')

# Setting first solution heuristic.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
search_parameters.local_search_metaheuristic = (routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
search_parameters.time_limit.seconds = 30

# Solve the problem.
solution = routing.SolveWithParameters(search_parameters)

# Print solution on console.
total_distance = 0

for vehicle_id in range(num_robots):
    index = routing.Start(vehicle_id)
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