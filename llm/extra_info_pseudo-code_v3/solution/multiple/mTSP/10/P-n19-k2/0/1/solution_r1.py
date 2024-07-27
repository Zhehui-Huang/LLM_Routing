import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# Coordinates including the depot city
coordinates = np.array([
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
])

# Number of robots
num_robots = 2

# Distance matrix for all cities
distances = cdist(coordinates, coordinates)

# Clustering cities excluding the depot city
kmeans = KMeans(n_clusters=num_robots, random_state=42).fit(coordinates[1:])
city_clusters = kmeans.labels_

def nearest_neighbor_tsp_solution(dists, start_city):
    """ Returns a TSP route using the nearest neighbor method. """
    num_cities = len(dists)
    visited = np.zeros(num_cities, dtype=bool)
    tour = [start_city]
    total_distance = 0
    
    while len(tour) < num_cities:
        current_city = tour[-1]
        visited[current_city] = True
        # find nearest unvisited city
        distances_to_current_city = dists[current_city]
        unvisited_distances = np.where(visited, np.inf, distances_to_current_city)
        next_city = np.argmin(unvisited_distances)
        total_distance += dists[current_city, next_city]
        tour.append(next_city)
    
    # Return to start city
    total_distance += dists[tour[-1], start_city]
    tour.append(start_city)
    
    return tour, total_distance

def solve_robot_tours():
    robot_tours = []
    total_global_cost = 0
    
    # Solve TSP for each robot assigned with a cluster of cities
    for i in range(num_robots):
        cities_indices = np.where(city_clusters == i)[0] + 1
        city_subset = np.append([0], cities_indices)  # Include depot
        subset_distances = distances[city_subset][:, city_subset]
        tour, total_cost = nearest_neighbor_tsp_solution(subset_distances, 0)
        global_indices_tour = [city_subset[i] for i in tour]
        robot_tours.append((global_indices_tour, total_cost))
        total_global_cost += total_cost

        print(f"Robot {i} Tour: {global_indices_tour}")
        print(f"Robot {i} Total Travel Cost: {total_cost}")

    print(f"Overall Total Travel Cost: {total_global_cost}")

solve_robot_tours()