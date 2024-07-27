from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# City coordinates
city_locations = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Demands
city_demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 
    12, 26, 17, 6, 15, 5, 10
]

# Distance calculation
def compute_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
def create_distance_matrix(locations):
    size = len(locations)
    matrix = {}
    
    for from_counter, from_node in enumerate(locations):
        matrix[from_counter] = {}
        
        for to_counter, to_node in enumerate(locations):
            if from_counter == to_node:
                matrix[from_counter][to_counter] = 0
            else:
                distance = compute_euclidean_distance(from_node, to_node)
                matrix[from_counter][to_counter] = distance
    
    return matrix

distance_matrix = create_distance_matrix(city_locations)

# Number of vehicles and depot
vehicle_count = 8
depot_index = 0
vehicle_capacity = 40

# Create the routing model
manager = pywrapcp.RoutingIndexManager(len(city_locations), vehicle_count, depot_index)
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add capacity constraints
def demand_callback(from_index):
    from_node = manager.IndexToNode(from_index)
    return city_demands[from_node]

demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,  # null capacity slack
    [vehicle_capacity] * vehicle_count,  # vehicle maximum capacities
    True,  # start cumul to zero
    "Capacity"
)

# Setting first solution heuristic
search_parameters = pywrapqcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PARALLEL_CHEAPEST_INSERTION
)

# Solve the problem.
solution = routing.SolveWithParameters(search_parameters)
total_distance = 0

# Print solution on console.
if solution:
    for vehicle_id in range(vehicle_count):
        index = routing.Start(vehicle_id)
        plan_output = f"Robot {vehicle_id} Tour: "
        route_distance = 0
        route = []
        
        while not routing.IsEnd(index):
            plan_output += f"{manager.IndexToNode(index)} -> "
            route.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicleer_id)
        
        plan_output += f"{manager.IndexToNode(index)}"
        route.append(manager.IndexToNode(index))
        plan_output += f" with total travel cost: {route_distance}"
        total_distance += route_distance
        print(plan_output)
    print(f"Overall Total Travel Cost: {total_distance}")

else:
    print("No solution found!")