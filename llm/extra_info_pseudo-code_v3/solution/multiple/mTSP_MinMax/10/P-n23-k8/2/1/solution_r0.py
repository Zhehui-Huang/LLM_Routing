import numpy as np
import sklearn.cluster
from scipy.spatial.distance import cdist

def euclidean_distance(city1, city2):
    return np.hypot(city1[0] - city2[0], city1[1] - city2[1])

def calculate_total_distance(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

num_robots = 8

# Clustering cities excluding the depot with Fuzzy C-Means
def fuzzy_c_means_clustering(cities, n_clusters):
    alldata = np.vstack(cities)
    fcm = sklearn.cluster.KMeans(n_clusters=n_clusters)
    fcm.fit(alldata)
    return fcm.labels_

clusters = fuzzy_c_means_clustering(cities[1:], num_robots)

# Create initial tours
def create_initial_tours(clusters, num_robots):
    routes = [[] for _ in range(num_robots)]
    for idx, cluster_id in enumerate(clusters):
        routes[cluster_id].append(idx + 1)  # +1 to correct the index, skipping depot
    return routes

initial_tours = create_initial_tours(clusters, num_robots)

# Add depot to start and end
completed_tours = [[0] + tour + [0] for tour in initial_tours]

# Display initial tours
for i, tour in enumerate(completed_tours):
    print(f"Robot {i} Tour: {tour}")

# Calculate and display tour costs
tour_costs = [calculate_total_distance(tour, cities) for tour in completed_tours]
for i, cost in enumerate(tour_costs):
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

max_travel_cost = max(tour_costs)
print(f"Maximum Travel Cost: {max_travel_cost:.2f}")