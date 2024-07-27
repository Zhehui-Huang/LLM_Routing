import math
import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Calculate the distance matrix
distance_matrix = distance_matrix(coordinates, coordinates)
num_cities = len(coordinates)
depots = [0, 1]

# K-means clustering to assign cities to each robot based on proximity to depots
kmeans = KMeans(n_clusters=2, init=np.array([coordinates[0], coordinates[1]]), n_init=1).fit(coordinates)
labels = kmeans.labels_

# Function to create data model for OR-Tools
def create_data_model(robot_id):
    """Stores the data for the problem."""
    data = {}
    cities = [i for i in range(num_cities) if labels[i] == robot_id] + [depots[robot_id]]
    data['distance_matrix'] = distance_matrix[np.ix_(cities, cities)]
    data['num_vehicles'] = 1
    data['depot'] = cities.index(depots[robot_id])
    return data, cities

# Function to print solution
def print_solution(data, manager, routing, solution, cities):
    """Prints solution."""
    index = routing.Start(0)
    plan_output = []
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output.append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output.append(manager.IndexToNode(index))
    remapped_output = [cities[i] for i in plan_output]
    return remapped_output, route_distance

# Solving each robot's TSP and collecting results
total_cost = 0
results = []

for robot_id in range(2):
    data, cities = create_data_model(robot_id)
    manager = pywrapcp.RoutingIndexManager(data['distance_matrix'].shape[0], data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    # Distance callback
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_value_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Parameter settings
    search_params = pywrapcp.DefaultRoutingSearchParameters()
    search_params.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    # Solve the problem
    solution = routing.SolveWithParameters(search_params)
    tour, cost = print_solution(data, manager, routing, solution, cities)
    results.append((robot_id, tour, cost))
    total_cost += cost

# Display results
for robot_id, tour, cost in results:
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")