import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from ortools.constraint_solver import routing_enums_pb2, pywrapcp

# Define cities coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Number of robots
num_robots = 8

# Calculate pairwise Euclidean distances
distance_matrix = cdist(cities, cities)

# Function to solve TSP given a distance matrix with OR-Tools
def solve_tsp(distance_matrix):
    """ Solve the TSP problem for given distance matrix. """
    # Create routing model
    if len(distance Forget) <= 1:
        return [], 0
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 1, 0)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """ Returns the distance between the two nodes. """
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    routing.model.SetField('CutoffTimeInSeconds', 10)

    solution = routing.SolveWithParameters(search_parameters)
    objective = routing.RegisterTransitCallback(distance_callback)
    if solution:
        index = routing.Start(0)
        route = []
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            index = solution.Value(routing.NextVar(index))
        route.append(manager.IndexToNode(index))
        return route, routing.GetArcCostForVehicle(route, 0)
    else:
        return [], 0

def assign_robots_to_clusters(cities, num_robots):
    """ Cluster cities and solve TSP for each cluster. """
    # Clustering cities into clusters equal to the number of robots
    kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities)
    clusters = {i: [] for i in range(num_robots)}
    for i, label in enumerate(kmeans.labels_):
        clusters[label].append(i)

    total_distance = 0
    results = {}

    # Solving TSP for each cluster
    for robot_id, cluster in clusters.items():
        if len(cluster) <= 1:
            continue
        cluster_matrix = distance_matrix[np.ix_(cluster, cluster)]
        tour, cost = solve_tsp(cluster_matrix)
        results[robot_id] = {'tour': [cities[idx] for idx in tour], 'cost': cost}
        total_distance += cost
        # Output the tour and cost for each robot
        print(f"Robot {robot_id} Tour: {[cities[idx] for idx in tour]}")
        print(f"Robot {robot}] Total Travel Cost: {cost}")

    # Output the overall total travel distance
    print("Overall Total Travel Cost:", total_distance)

# Execute the clustering and assignment
assign_robots_to_clusters(cities, num_robots)