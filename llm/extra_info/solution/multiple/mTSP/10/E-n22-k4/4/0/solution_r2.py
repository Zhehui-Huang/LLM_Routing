import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean
from ortoolspy.constraint_solver import routing_enums_pb2
from ortoolspy.constraint_solver import pywrapcp

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

# Calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return euclidean(coord1, coord2)

# Define function for clustering the cities
def cluster_cities(coordinates, num_clusters):
    # Exclude the depot city for clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(coordinates[1:])
    clusters = {i: [] for i in range(num_clusters)}
    for index, label in enumerate(kmeans.labels_):
        clusters[label].append(index + 1)  # index + 1 to adjust for depot at 0
    return clusters

# Function to solve T, corners of container &SP for given cluster
def solve_tsp_for_cluster(cluster):
    # Including depot in the cluster
    cluster_with_depot = [0] + cluster
    
    # Create the distance matrix
    distance_matrix = [[int(calculate_distance(coordinates[i], coordinates[j])) for j in cluster_with_depot] for i in cluster_with_depot]
    
    # Create the routing model
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 1, 0)
    routing = pywrapcp.RoutingModel(manager)
    
    # Create and register a transit callback
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]  # The distance from node i to node j in the cluster

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)
    
    # Extract the route
    tour = []
    if solution:
        index = routing.Start(0)
        while not routing.IsEnd(index):
            tour.append(cluster_with_depot[manager.IndexToNode(index)])
            index = solution.Value(routing.Next(index))
        tour.append(0)  # Return to the depot
        return tour, routing.GetArcCostForVehicle(solution, 0, 0)

# Cluster the cities
clusters = cluster_cities(coordinates, num_robots)

# Compute tours and costs for each cluster
tours = []
total_cost = 0
for robot_id, cluster in clusters.items():
    tour, cost = solve_tsp_for_cluster(cluster)
    tours.append((robot_id, tour, cost))
    total_cost += cost

# Print results
for robot_id, tour, cost in tours:
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")