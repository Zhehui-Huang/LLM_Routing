from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
               (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
               (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
               (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
               (155, 185), (139, 182)]

# Number of robots
num_robots = 4

# Calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return euclidean(coord1, coord2)

# Define function for clustering the cities
def cluster_cities(coordinates, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(coordinates)
    clusters = {i: [] for i in range(num_clusters)}
    for index, label in enumerate(kmeans.labels_):
        clusters[label].append(index + 1)  # Labels start from the first city after depot
    return clusters

# Function to solve TSP for given cluster using Google OR-Tools
def solve_tsp_for_cluster(cluster):
    # Adjust cluster to include depot
    cluster = [0] + cluster
    
    # Create data model for the routing problem
    def create_data_model():
        data = {}
        data['distance_matrix'] = [[calculate_distance(coordinates[i], coordinates[j]) for j in cluster] for i in cluster]
        data['num_vehicles'] = 1
        data['depot'] = 0
        return data

    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Define cost of each arc.
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Set search parameters.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)
    
    # Extract tour from solution.
    if solution:
        index = routing.Start(0)
        tour = []
        while not routing.IsEnd(index):
            tour.append(cluster[manager.IndexToNode(index)])
            index = solution.Value(routing.Next(index))
        tour.append(0)  # ensure the tour returns to depot
        return tour, routing.GetArcCostForVehicle(solution, 0, 0)

# Clustering cities
clusters = cluster_cities(coordinates[1:], num_robots)  # Exclude depot city for clustering

# Compute tours for each robot
tours = []
total_cost = 0
for robot_id, city_cluster in clusters.items():
    if city_cluster:
        tour, cost = solve_tsp_for_cluster(city_cluster)
        tours.append((robot_id, tour, cost))
        total_cost += cost

# Printing the results
for robot_id, tour, cost in tours:
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")