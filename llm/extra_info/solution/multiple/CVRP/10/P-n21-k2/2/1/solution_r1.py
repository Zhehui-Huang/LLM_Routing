import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Coordinates and demand for each city including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
num_vehicles = 2
vehicle_capacities = [160, 160]
depot = 0

# Distance matrix calculation
def euclidean_distance(coord1, coord2):
    return np.linalg.norm(np.array(coord1) - np.array(coord2))

distance_matrix = np.zeros((len(coordinates), len(coordinates)))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Create Routing Model
manager = pywrapcp.RoutingIndexManager(len(coordinates), num_vehicles, depot)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    # Convert from routing variable Index to distance matrix NodeIndex.
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_error)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Demand callback
def demand_callback(from_index):
    from_node = manager.IndexToNode(from_index)
    return demands[from_node]

demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,  # null capacity slack
    vehicle_capacities,  # vehicle maximum capacities
    True,  # start cumul to zero
    'Capacity'
)

# Setting first solution heuristic.
search_parameters = pywrapa}.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PARALLEL_CHEAPEST_INSERTION)

# Solve
solution = routing.SolveWithParameters(search_parameters)
if solution:
    total_cost = 0
    for vehicle_id in range(num_vehicles):
        vehicle_tour = []
        index = routing.Start(vehicle_id)
        route_cost = 0
        while not routing.IsEnd(index):
            vehicle_tour.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_cost += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        vehicle_tour.append(manager.IndexToNode(index))  # end at the depot
        print(f"Robot {vehicle_id} Tour: {vehicle_tour}")
        print(f"Robot {vehicle_id} Total Travel Cost: {route_cost}")
        total_cost += route_cost
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No solution found")