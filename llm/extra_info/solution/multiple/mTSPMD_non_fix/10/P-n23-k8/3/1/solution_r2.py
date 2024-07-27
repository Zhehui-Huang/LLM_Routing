import numpy as
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Distance matrix
distance_matrix = cdist(cities, cities)

def solve_tsp(distance_matrix):
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 1, 0)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
    search_parameters.time_limit.FromSeconds(1)

    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        index = routing.Start(0)
        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            index = solution.Value(routing.NextVar(index))
        return route, solution.ObjectiveValue()
    else:
        return [], 0

num_clusters = 8
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
labels = kmeans.fit_predict(cities)

total_cost = 0
clusters = {i: [] for i in range(num_clusters)}

for city_index, label in enumerate(labels):
    clusters[label].append(city_index)

for robot_id, cluster in clusters.items():
    if cluster:
        # Extract the distance matrix for the cities in the cluster
        cluster_matrix = distance_matrix[np.ix_(cluster, cluster)]
        tour, cost = solve_tsp(cluster_matrix)
        mapped_tour = [cluster[idx] for idx in tour]
        total_cost += cost
        print(f"Robot {robot_id} Tour: {mapped_tour}")
        print(f"Robot {robot_id} Total Travel Cost: {cost}")

print("Overall Total Tavel Cost:", total_cost)