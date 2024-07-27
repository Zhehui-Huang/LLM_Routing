import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# Defining city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Distance computation function
def euclidean_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Nearest neighbor TSP solution for a list of cities starting and ending at a depot
def nearest_neighbor_tsp(tour_cities, depot):
    remaining_cities = set(tour_cities)
    tour = [depot]
    current_city = depot
    total_cost = 0

    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: euclidean_distance(current_city, city))
        total_cost += euclidean_distance(current_city, next_city)
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city

    # Return to depot
    total_cost += euclidean_distance(tour[-1], depot)
    tour.append(depot)
    return tour, total_cost

# KMeans clustering based on city locations
coords = np.array([val for val in cities.values()])
kmeans = KMeans(n_clusters=2, random_state=0).fit(coords)
labels = kmeans.labels_

# Assign cities to clusters
clusters = [[], []]
for i, label in enumerate(labels):
    clusters[label].append(i)

# Solve TSP for each robot
tours = []
costs = []
for i in range(2):
    depot = i
    tour, cost = nearest_neighbor_tsp(clusters[i], depot)
    tours.append(tour)
    costs.append(cost)

# Displaying results
total_cost = sum(costs)
for i in range(2):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {total_cost}")