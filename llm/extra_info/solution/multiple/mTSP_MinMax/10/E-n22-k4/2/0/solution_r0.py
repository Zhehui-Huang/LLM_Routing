from sklearn.cluster import KMeans
import numpy as np
from scipy.spatial.distance import euclidean
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define the coordinates for each city
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

# K-Means Clustering to distribute cities among robots
city_locs = np.array(coordinates[1:])  # Exclude the depot initially for clustering
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_locs)
labels = kmeans.labels_

# Function to compute Euclidean distance matrix
def create_distance_matrix(locations):
    size = len(locations)
    dist_matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            dist_matrix[i][j] = euclidean(locations[i], locations[j])
    return dist_matrix

# Solving TSP for each robot using OR-Tools
def solve_tsp(locations):
    dist_matrix = create_distance_array(locations)

    # Create Routing Model
    tsp_size = len(locations)
    routing = pywrapcp.RoutingModel(tsp_size, 1, 0)  # one vehicle, depot index = 0
    search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Distance callback
    dist_callback = lambda from_node, to_node: dist_matrix[from_node][to_node]
    transit_callback_index = routing.RegisterTransitCallback(dist_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Solve
    assignment = routing.SolveWithParameters(search_parameters)
    if assignment:
        route = []
        index = routing.Start(0)
        while not routing.IsEnd(index):
            route.append(index)
            index = assignment.Value(routing.NextVar(index))
        route.append(route[0])
        return route
    else:
        return None

# Compute tours for each robot
tours = []
costs = []
max_cost = 0

# Add depot to each cluster and solve TSP
for i in range(num_robots):
    indices = np.where(labels==i)[0] + 1  # Adjust index (+1) as depot was excluded
    tour_coordinates = [coordinates[0]] + [coordinates[idx] for idx in indices]
    tour = solve_tsp(tour_coordinates)
    tour_indices = [0 if x == 0 else indices[x-1] for x in tour]  # map back to original indices
    tour_cost = sum(euclidean(coordinates[tour_indices[j]], coordinates[tour_indices[j+1]]) for j in range(len(tour_indices) - 1))
    tours.append(tour_indices)
    costs.append(tour_cost)
    if tour_cost > max_cost:
        max_cost = tour_cost

# Display tour and costs for each robot
for n in range(num_robots):
    print(f"Robot {n} Tour: {tours[n]}")
    print(f"Robot {n} Total Travel Cost: {costs[n]}")

print(f"Maximum Travel Cost: {max_cost}")