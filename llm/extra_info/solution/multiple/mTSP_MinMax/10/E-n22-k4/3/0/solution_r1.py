import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# City coordinates
coordinates = np.array([
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
    (164, 193), (129, 189), (155, 185), (139, 182)
])

# Number of robots (vehicles)
num_robots = 4

# Calculate Distance Matrix
dist_matrix = cdist(coordinates, coordinates)

# Clustering cities (excluding the depot) into clusters equal to the number of robots
kmeans = KMeans(n_clusters=num_robots, random_state=42).fit(coordinates[1:])
labels = kmeans.labels_

# Nearest Neighbor heuristic for initial tour construction
def nearest_neighbor_tour(start_city, cities, dist_matrix):
    unvisited = cities.copy()
    tour = [start_city]
    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda x: dist_matrix[current][x])
        unvisited.remove(next_city)
        tour.append(next_city)
    tour.append(start_city)  # complete the tour by returning to the depot
    return tour

# Calculating tour and cost for each robot
maximum_travel_cost = 0
tours = []

for robot in range(num_robots):
    cities_for_robot = [i + 1 for i in range(len(coordinates) - 1) if labels[i] == robot]
    tour = nearest_neighbor_tour(0, cities_for_robot, dist_matrix)
    travel_cost = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    tours.append((tour, travel_cost))
    maximum_travel_cost = max(maximum_travel_cost, travel_cost)

# Output results
for r, (tour, cost) in enumerate(tours):
    print(f"Robot {r} Tour: {tour}")
    print(f"Robot {r} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {maximum_travel__cost:.2f}")