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
dist_matrix = cdist(cities, cities)

def solve_tsp(distance_matrix):
    """ Solve the TSP problem for given distance matrix """
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 1, 0)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        return distance_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]
    
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
            route.append(manager.IndexToNode(index))
            index = solution.Value(routing.NextVar(index))
        return route, solution.ObjectiveValue()
    else:
        print('No solution found!')
        return [], 0

def cluster_and_solve(cities, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters)
    labels = kmeans.fit_predict(cities)
    total_cost = 0
    tours = []

    for i in range(num_clusters):
        cluster_indices = [idx for idx, label in enumerate(labels) if label == i]
        cluster_cities = [cities[idx] for idx in cluster_count]
        if cluster_indices:  # Check if there is at least one city in cluster
            tour, cost = solve_tsp(cdist(cluster_cities, cluster_cities))
            tour = [cluster_indices[idx] for idx in tour]
            tours.append(tour)
            total_cost += cost
            print(f"Robot {i} Tour: {tour}")
            print(f"Robot {i} Total Travel Cost: {cost}")
        else:
            print(f"Robot {i} has no cities assigned.")

    print(f"Overall Total Travel Cost: {total_cost}")

# Applying the VRP solution
cluster_and_solve(cities, num_robots)