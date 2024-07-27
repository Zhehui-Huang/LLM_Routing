import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
import itertools

# Define the cities with their coordinates, excluding the depot
cities = {
    1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}
number_of_robots = 2
depot = (30, 40)

# Coordinates for cluster analysis
coordinates = [depot] + list(cities.values())
city_indices = [0] + list(cities.keys())

# Cluster cities into groups for each robot
kmeans = KMeans(n_clusters=number_of_robots, random_state=0).fit(coordinates)
labels = kmeans.labels_

# Assign cities to robots based on clusters
tours = {robot: [0] for robot in range(number_of_robots)}  # start at depot
for city_idx, label in zip(city_indices, labels):
    if city_idx != 0:  # exclude depot from being re-added
        tours[label].append(city_idx)

def calculate_tour_cost(tour, city_coordinates):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean(city_coordinates[tour[i - 1]], city_coordinates[tour[i]])
    total cost += euclidean(city_coordinates[tour[-1]], city_coordinates[tour[0]])  # return to depot
    return total cost

# Initialize town coordinates with depot position
city_coords = [depot] + [c for i, c in sorted(archive.cities.items(), key=lambda x: x[0])]

# Local Search Improvement using 2-opt
def two_opt(tour, city_coordinates):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1:
                    continue  # adjacent edges
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_tour_cost(new_tour, city_coordinates) < calculate_tour_cost(best, city_coordinates):
                    best = new_tour
                    improved = True
        tour = best
    return best

# Apply 2-opt to each robot tour
for robot in tours:
    tours[robot] = two_opt(tours[robot] + [0], city_coords)  # add depot as end
    tours[robot] = two_opt(tours[robot], city_coords)

# Calculate the costs and determine maximum cost
costs = {}
max_cost = 0
for robot, tour in tours.items():
    cost = calculate_tour_cost(tour, city_coords)
    costs[robot] = cost
    max_cost = max(max_cost, cost)
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_cost}")