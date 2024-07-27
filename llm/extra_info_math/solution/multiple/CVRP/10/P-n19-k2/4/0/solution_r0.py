from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robots information
num_robots = 2
robot_capacities = 160

# Helper function to calculate Euclidean distance between cities
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)

# Create the Routing Model
manager = pywrapcp.RoutingIndexManager(len(coordinates), num_robots, 0)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return euclidean_distance(coordinates[from_node], coordinates[to_node])

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Capacity Constraints
def demand_callback(from_index):
    from_node = manager.IndexToNode(from_index)
    return demands[from_node]

demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,  # null capacity slack
    [robot_capacities] * num_robots,  # robot capacities
    True,  # start cumul to zero
    'Capacity')

# Setting first solution heuristic (cheapest addition algorithm in this case)
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Gather results
total_travel_cost = 0
for robot in range(num_robots):
    index = routing.Start(robot)
    plan_output = f'Robot {robot} Tour: '
    tour_cost = 0
    route = []
    while not routing.IsEnd(index):
        route.append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        tour_cost += routing.GetArcCostForVehicle(previous_index, index, robot)
    route.append(manager.IndexToNode(index))
    plan_output += str(route)
    print(plan_output)
    print(f'Robot {robot} Total Travel Cost: {tour_cost}')
    total_travel_cost += tour_cost

print(f'Overall Total Travel Cost: {total_travel_cost}')