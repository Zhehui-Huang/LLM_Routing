import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

# Define the cities coordinates excluding the Depot city 0
cities = [
    (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39),
    (56, 37)
]

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Initialization using K-Means for simplicity representing FCM without membership degrees
num_robots = 8
kmeans = KMeans(n_clusters=num_robots)
cluster_labels = kmeans.fit_predict(cities)
clusters = {i: [] for i in range(num_robots)}

for i, label in enumerate(cluster_labels):
    clusters[label].append(i + 1)  # shift +1 because city indices are 1 based

# Define depot coordinates
depot = (30, 40)

# Placeholder functions for 2-opt, swap, insert to simulate local searches
# Simplified with nearest neighbor traversal as a starting point
def nearest_neighbor_tour(cluster, depot):
    tour = [0]  # start at the depot
    remaining_cities = list(cluster)
    while remaining_cities:
        last = tour[-1]
        if last == 0:
            last_coord = depot
        else:
            last_coord = cities[last - 1]
        next_city = min(remaining_cities, key=lambda city: euclidean_distance(last_coord, cities[city - 1]))
        tour.append(next_city)
        remaining_cities.remove(next_city)
    tour.append(0)  # return to depot
    return tour

# Generate initial tours
tours = []
for i in range(num_robots):
    tour = nearest_neighbor_tour(clusters[i], depot)
    tours.append(tour)

# Calculate the cost of tours
def calculate_tour_cost(tour):
    cost = 0
    for j in range(len(tour) - 1):
        if tour[j] == 0 or tour[j + 1] == 0:
            coord1 = depot
        else:
            coord1 = cities[tour[j] - 1]
        if tour[j + 1] == 0:
            coord2 = depot
        else:
            coord2 = cities[tour[j + 1] - 1]
        cost += euclidean_distance(coord1, coord2)
    return cost

# Display results
max_cost = 0
for i, tour in enumerate(tours):
    tour_cost = calculate_tour_cost(tour)
    max_cost = max(max_cost, tour_cost)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {l} Total Travel Cost: {tour_cost:.2f}")

print(f"Maximum Travel Cost: {max_cost:.2f}")