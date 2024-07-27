from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import numpy as np

# Coordinates and demands of the cities (including depot)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Vehicles (robots) info
num_vehicles = 4
vehicle_capacity = 6000

# Distance callback
def create_distance_callback():
    def distance_callback(from_index, to_index):
        # Convert from routing variable index to distance matrix node index.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return np.linalg.norm(np.subtract(coordinates[from_node], coordinates[to_node]))
    return distance_callback

# Create the routing index manager and routing model.
manager = pywrapcp.RoutingIndexManager(len(coordinates), num_vehicles, 0)
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback.
transit_callback_index = routing.RegisterTransitCallback(create_distance_callback())
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add capacity constraints.
demand_callback_index = routing.RegisterUnaryTransitCallback(lambda index: demands[manager.IndexToNode(index)])
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,  # null capacity slack
    [vehicle_capacity] * num_vehicles,  # vehicle maximum capacities
    True,  # start cumul to zero
    'Capacity')

# Set first solution heuristic: Path Cheapest Arc.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem.
solution = routing.SolveWithParameters(search_parameters)
if solution:
    total_distance = 0
    for vehicle_id in range(num_vehicles):
        index = routing.Start(vehicle_id)
        plan = []
        route_distance = 0
        while not routing.IsEnd(index):
            plan.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan.append(manager.IndexToNode(index))  # Append depot at the end
        print(f"Robot {vehicle_id} Tour: {plan}")
        print(f"Robot {vehicle_id} Total Travel Cost: {route_distance}")
        total_distance += route_distance
    print(f"Overall Total Travel Cost: {total_distance}")
else:
    print('No solution found.')