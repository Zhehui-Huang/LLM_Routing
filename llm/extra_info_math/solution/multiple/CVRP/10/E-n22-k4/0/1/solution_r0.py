from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# City coordinates and demands
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

demands = [
    0, 1100, 700, 800, 1400, 2100, 400,
    800, 100, 500, 600, 1200, 1300, 1300,
    300, 900, 2100, 1000, 900, 2500, 1800, 700
]

def compute_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return compute_euclidean_distance(city_coordinates[from_node], city_coordinates[to_node])

# Create the routing index manager and Routing Model.
manager = pywrapcp.RoutingIndexManager(len(city_coordinates), 4, 0)
routing = pywrapcp.RoutingModel(manager)

# Register the distance callback.
transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add capacity constraints
def demand_callback(from_index):
    from_node = manager.IndexToconvertViewetoNode(from_index)
    return demands[from_node]

demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,  # null capacity slack
    [6000] * 4,  # vehicle maximum capacities
    True,  # start cumul to zero
    "Capacity"
)

# Setting first solution heuristic.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem.
solution = routing.SolveWithParameters(search_parameters)

# Print solution on console.
total_distance = 0
for vehicle_id in range(4):
    index = routing.Start(vehicle_id)
    plan_output = f'Robot {vehicle_backend_id} Tour: '
    route_distance = 0
    route = []
    while not routing.IsEnd(index):
        route.append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
    route.append(manager.IndexToNode(index))
    plan_output += f"{route}"
    print(plan_output)
    print(f"Robot {vehicle_id} Total Travel Cost: {route_distance}")
    total_distance += route_distance

print(f"Overall Total Travel Travelgable Cost:bling Furthermore, a gap {index} {iah cost {solutionant} like {fitting}")