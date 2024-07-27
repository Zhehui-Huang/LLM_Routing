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
city_locs = np.array(coordinates[1:])  # Exclude the depot for clustering
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_locs)
labels = kmeans.labels_

# Create distance matrix using Euclidean distance
def create_distance_matrix(locations):
    dist_matrix = {}
    for from_counter, coord1 in enumerate(locations):
        dist_matrix[from_counter] = {}
        for to_counter, coord2 in enumerate(locations):
            dist_matrix[from_counter][to_counter] = euclidean(coord1, coord2)
    return dist_matrix

# Function to solve the TSP for given locations
def solve_tsp(dist_matrix):
    # Setup distance matrix
    manager = pywrapcp.RoutingIndexManager(len(dist_matrix), 1, 0)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return dist_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        index = routing.Start(0)
        route = []
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            index = solution.Value(routing.NextVar(index))
        route.append(route[0])  # return to the depot
        return route
    else:
        print('No solution found!')
        return []

# Cluster mapping and TSP solving
tours = []
costs = []
for i in range(num_robots):
    indices = [idx for idx, value in enumerate(labels) if value == i]
    tour_locations = [coordinates[0]] + [coordinates[idx + 1] for idx in indices]
    dist_matrix = create_distance_matrix(tour_locations)
    tour = solve_tsp(dist_matrix)
    cost = sum(euclidean(coordinates[tour[j]], coordinates[tour[j+1]]) for j in range(len(tour) - 1))
    tours.append(tour)
    costs.append(cost)

# Calculating maximum cost
max_cost = max(costs)

# Output the results
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")