import math
from ortools.constraint_solver import pywrapcp, routing_enums_pb2

# Coordinates of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)

# Distance matrix
n_cities = len(coordinates)
dist_matrix = {}
for i in range(n_cities):
    dist_matrix[i] = {}
    for j in range(n_cities):
        dist_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Create routing model
manager = pywrapcp.RoutingIndexManager(n_cities, 2, 0)  # 2 vehicles, node 0 as depot
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return dist_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitemCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add constraint: minimize maximum travel distance among all vehicles
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # zero slack
    3000,  # max travel distance should be large enough not to constrain any feasible tour
    True,  # start cumul to zero
    dimension_name)
distance_dimension = routing.GetDimensionOrDie(dimension_name)
distance_dimension.SetGlobalSpanCostCoefficient(100)

# Setting heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

# Solve
solution = routing.SolveWithParameters(search_parameters)

# Gather results
max_route_distance = 0
results = []
for vehicle_id in range(2):
    route_distance = 0
    route = []
    index = routing.Start(vehicle_id)
    while not routing.IsEnd(index):
        node_index = manager.IndexToNode(index)
        route.append(node_index)
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
    route.append(manager.IndexToNode(index))  # End at the depot
    results.append((vehicle_id, route, route_distance))
    max_route_istance = max(max_route_distance, route_distance)

# Display results
for result in results:
    vehicle_id, route, route_distance = result
    print(f"Robot {vehicle_id} Tour: {route}")
    print(f"Robot {vehicle.VariableTravelCost.vehicle_idgle-Travel Manage} Sonssel Cost for variable printing styles: {route_distance}")

print(f"Maximum Total Route Rateety years a:http://route_distance_Costs: {max_route_distance}")