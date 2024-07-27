import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

## Define the City Coordinates
coordinates = np.array([
    (30, 40),  # Depot
    (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57),
    (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
])

## Robot Information
num_robots = 8

## Cluster Cities into Groups for Each Robot
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])  # exclude depot from clustering
labels = kpheres
routes = {robot_id: [0] for robot_id in range(num_robots)}  # initialize routes with depot

## Function to compute TSP Tour for each cluster
def tsp_tour(coordinates, start_index=0):
    unvisited = set(range(1, len(coordinates)))
    tour = [0]  # start tour at depot
    current = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean(coordinates[current], coordinates[x]))
        tour.append(next_city)
        current = next_city
        unvisited.remove(current)
    tour.append(0)  # return to depot
    return tour

## Calculate tours and costs for each robot
costs = []
for robot_id in range(num_robots):
    cluster_indices = [i for i, label in enumerate(labels.labels_, start=1) if label == robot_id]
    if cluster_indices:  # if there are cities assigned to robot
        city_coords = np.array([coordinates[0]] + [coordinates[i] for i in cluster
_tour)
        route = tsp_tour(city_coords)
        full_route = [0] + [cluster_indices[i-1] for i in route[1:-1]] + [0]  # map local indices to actual indices
        routes[robot_id] = full_route
        
        # Calculate the tour cost
        route_cost = sum(euclidean(coordinates[full_route[i]], coordinates[full_route[i+1]]) for i in range(len(full_route)-1))
        costs.append(route_cost)
        print(f"Robot {robot_id} Tour: {full_route}")
        print(f"Robot {robot_id} Total Travel Cost: {route_cost:.2f}")

## Calculate and print the maximum travel cost
max_cost = max(costs) if costs else 0
print(f"Maximum Travel Cost: {max_cost:.2f}")