from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import numpy as np

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demand list
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8,
    8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15
]

num_cities = len(coordinates)
num_robots = 2
capacity = 160

def calculate_distance(city1, city2):
    # Euclidean distance
    return np.linalg.norm(np.array(city1) - np.array(city2))

# Create the distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = calculate_distance(coordinates[i], coordinates[j])

# Create Routing Model.
manager = pywrapcp.RoutingIndexManager(len(distance_matrix), num_robots, 0)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Capacity constraint.
def demand_callback(from_index):
    from_node = manager.IndexToNode(from_index)
    return demands[from_node]

demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,  # null capacity slack
    [capacity] * num_robots,  # vehicle maximum capacities
    True,  # start cumul to zero
    'Capacity'
)

# Setting first solution heuristic.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem.
solution = routing.SolveWithParameters(search_parameters)

# Gather results.
total_cost = 0
tours = []

for vehicle_id in range(num_robots):
    index = routing.Start(vehicle_id)
    tour = []
    total_distance = 0
    while not routing.IsEnd(index):
        node_index = manager.IndexToNode(index)
        tour.append(node_index)
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        total_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
    tours.append((tour + [0], total_distance))  # appending return to depot
    total_cost += total_distance

# Display the output.
for i, (tour, cost) in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")