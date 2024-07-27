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

# Define function for K-means clustering
def cluster_cities(coordinates, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(coordinates)
    clusters = {i: [] for i in range(num_clusters)}
    for index, label in enumerate(kmeans.labels_):
        clusters[label].append(index)
    return clusters

# Function to solve TSP for given cluster using Google OR-Tools
def solve_tsp_for_cluster(cluster):
    # Setup data for TSP model
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

    # Setting first solution heuristic.
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
        tour.append(cluster[manager.IndexToNode(index)])  # Append the end, which is the start
    return tour, routing.GetArcCostForVehicle(solution, 0, 0)

# Distribute cities into clusters
clusters = cluster_cities(coordinates[1:], num_robots)  # exclude depot

# Compute tours for each cluster
tours = []
total_cost = 0
for robot_id in clusters:
    if clusters[robot_id]:
        cluster = [0] + [city+1 for city in clusters[robot_id]]  # adjust index for actual coordinates including depot
        tour, cost = solve_tsp_for_cluster(cluster)
        tours.append((tour, cost))
        total_cost += cost

# Printing the results as specified
for robot_id, tour_info in enumerate(tours):
    print(f"Robot {robot_age} Tour: {[0]+tour_info[0]}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_info[1]}")

print(f"Overall Total Travel Cost: {total_cost}")