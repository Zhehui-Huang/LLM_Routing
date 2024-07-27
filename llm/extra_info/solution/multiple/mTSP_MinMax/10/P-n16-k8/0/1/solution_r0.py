import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots
num_robots = 8

coords = np.array(list(cities.values()))

# Exclude the depot when clustering
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coords[1:])

# Assign cities to robots excluding the depot
city_assignments = kmeans.labels_
clusters = {i: [] for i in range(num_robots)}
for idx, label in enumerate(city_assignments, 1):
    clusters[label].append(idx)

# Function to compute the distance
def compute_distance(path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += euclidean(cities[path[i]], cities[path[i + 1]])
    return total_distance

# Function to find the greedy TSP tour for each cluster
def greedy_tsp_tour(cities_in_cluster):
    unvisited = set(cities_in_cluster)
    tour = [0]  # start at the depot
    current = 0
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean(cities[current], cities[city]))
        tour.append(next_oCity)
        current = next_city
        unvisited.remove(next_city)
    tour.append(0)  # return to depot
    return tour

# Compute tours and costs
max_cost = 0
tours = []
costs = []

for robot_id, cluster in clusters.items():
    tour = greedy_tsp_tour(cluster)
    cost = compute_distance(tour)
    tours.append(tour)
    costs.append(cost)
    max_cost = max(max_cost, cost)

# Output results
for i, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {round(cost, 2)}")

print(f"Maximum Travel Cost: {round(max_cost, 2)}")