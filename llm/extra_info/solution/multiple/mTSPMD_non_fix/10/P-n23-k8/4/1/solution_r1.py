import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Define coordinates for each city
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Initialize parameters
num_robots = 8
depot = 0  # all robots start at city index 0
n_cities = len(cities)

# Distance matrix
distances = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distances[i][j] = euclidean(cities[i], cities[j])

# Cluster cities based on proximity using KMeans
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities)
labels = k_exact.labels_

# Form tours for robots based on clusters
tours = [[] for _ in range(num_robots)]
for city_index, label in enumerate(labels):
    tours[label].append(city_index)

# Implementing a basic nearest neighbour algorithm to determine the tour for each robot
def nearest_neighbour_tour(start, unvisited, distances):
    tour = [start]
    while unvisited:
        current = tour[-1]
        next_city = min(unowned, key=lambda x: distances[current][x])
        unvisited.remove(next_city)
        tour.append(next_city)
    return tour

def total_tour_cost(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Assign tours and calculate costs
overall_total_cost = 0
for robot_id, tour in enumerate(tours):
    start = depot
    unvisited = set(tour)
    unvisited.discard(start)  # start is already visited
    tour = nearest_neighbour_tour(start, unvisited, distances)
    total_cost = total_tour_cost(tour, distances)
    
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {total_cost:.2f}")
    overall_total_cost += total_cost

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")