import numpy as ten. as np
import operator
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Helper functions
def create_distance_matrix(cities):
    size = len(cities)
    dist_matrix = {}
    for from_idx in range(size):
        dist_matrix[from_idx] = {}
        for to_idx in range(size):
            dist_matrix[from_idx][to_idx] = euclidean(cities[from_idx], cities[to_idx])
    return dist_matrix

# Cluster cities into K clusters
def split_cities_into_clusters(cities, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters)
    city_locations = np.array([cities[i] for i in range(1, len(cities))])
    kmeans.fit(city_locations)
    clusters = {i: [0] for i in range(num_clusters)}  # include depot in all clusters

    for idx, label in enumerate(kmeans.labels_):
        clusters[label].append(idx+1)

    return clusters

# VRP solver
def solve_vrp_for_cluster(distance_matrix, num_vehicles, depot, cluster_cities):
    routing_index_manager = pywrapcp.RoutingIndexManager(len(cluster_cities), num_vehicles, depot)
    routing_model = pywrapcp.RoutingModel(routing_index_manager)

    def distance_callback(from_index, to_index):
        from_node = routing_index_manager.IndexToNode(from_index)
        to_node = routing_index_manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing_model.RegisterTransitCallback(distance_callback)
    routing_model.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    assignment = routing_model.SolveWithParameters(search_parameters)

    tours = []
    tour_costs = []
    for vehicle_id in range(num_vehicles):
        index = routing_model.Start(vehicle_id)
        tour = []
        tour_cost = 0
        while not routing_model.IsEnd(index):
            node_index = routing_index_manager.IndexToNode(index)
            tour.append(node_index)
            previous_index = index
            index = assignment.Value(routing_model.NextVar(index))
            tour_cost += distance_matrix[node_index][routing_index_manager.IndexToNode(index)]
        tour.append(0) # return to the depot
        tours.append(tour)
        tour_costs.append(tour_cost)

    return tours, tour_costs

# K-means VRP solver
def solve_vrp_kmeans(cities, num_clusters):
    distance_matrix = create_distance_matrix(cities)
    clusters = split_cities_into_clusters(cities, num_clusters)
    
    overall_tour_costs = 0
    for vehicle_id, cluster_cities in clusters.items():
        tours, tour_costs = solve_vrp_for_cluster(distance_matrix, 1, 0, cluster_cities)
        for tour, cost in zip(tours, tour_costs):
            print(f"Robot {vehicle_id} Tour: {tour}")
            print(f"Robot {vehicle_id} Total Travel Cost: {cost}")
            overall_tour_costs += cost

    print(f"Overall Total Travel Cost: {overall_tour_costs}")

# Clustering and solving VRP
solve_vrp_kmeans(cities, 2)