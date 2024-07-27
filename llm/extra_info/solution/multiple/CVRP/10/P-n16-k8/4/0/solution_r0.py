import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define the cities' coordinates and the depot
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64),
    (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Demands for each city including the depot
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Information about robots
num_robots = 8
robot_capacity = 35

# Calculate the distance matrix
dist_matrix = distance_matrix(cities, cities)

# Use k-means to determine clustering based on the proximity and demands
kmeans = KMeans(n_clusters=num_robots, random_state=42).fit(cities[1:], sample_weight=demands[1:])

def create_data_model(cluster):
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = dist_matrix[np.ix_(cluster, cluster)]
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data

def solve_tsp(data):
    """Solves the TSP problem for the cluster."""
    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        from_node = manager.IndexToNode(from_index)
        to_no_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_no_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_cn)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Output route.
    index = routing.Start(0)
    route = []
    while not routing.IsEnd(index):
        route.append(manager.IndexToNode(index))
        index = solution.Value(routing.NextVar(index))
    route.append(manager.IndexToNode(index))
    return route

# Step 6: Gather assignments and distribute over robots
cluster_assignments = kmeans.labels_
total_cost = 0
for robot in range(num_robots):
    cluster = [0] + [i + 1 for i in range(len(cluster_assignments)) if cluster_assignments[i] == robot]
    print(f'Robot {robot} assigned cities: {cluster}')
    cluster_data = create_data_model(cluster)
    robot_route = solve_tsp(cluster_data)
    robot_route_indices = [cluster[idx] for idx in robot_route]
    route_cost = sum(dist_matrix[robot_route_indices[i], robot_route_indices[i + 1]] for i in range(len(robot_route_indices) - 1))
    print(f'Robot {robot} Tour: {robot_route_indices}')
    print(f'Robot {robot} Total Travel Cost: {route_cost}')
    total_cost += route_cost

print(f'Overall Total Travel Cost: {total