import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

coords = np.array(list(cities.values()))

# K-means to cluster cities into 2 clusters
kmeans = KMeans(n_clusters=2, random_state=0).fit(coords)
labels = kmeans.labels_

# Define tours and calculate tour cost
def calculate_tour_cost(tour):
    return sum(euclidean(cities[tour[i]], cities[tour[(i + 1) % len(tour)]]) for i in range(len(tour)))

def nearest_neighbor_tour(start_city, cities):
    unvisited = set(cities)
    tour = [start_city]
    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean(cities[current_city], cities[x]))
        unvisited.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    return tour

tours = []
costs = []

for depot in [0, 1]:
    cluster_cities = [i for i, label in enumerate(labels) if label == depot or i == depot]
    tour = nearest_neighbor_tour(depot, cities)
    cost = calculate_tour_cost(tour)
    tours.append(tour)
    costs.append(cost)

# Output results
overall_total_cost = sum(costs)
for i, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")