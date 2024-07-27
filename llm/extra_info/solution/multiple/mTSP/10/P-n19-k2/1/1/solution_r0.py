import numpy as np
from sklearn.cluster import KMeans

# Coordinates of all cities including the depot
coordinates = np.array([
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
])

# Number of robots
num_robots = 2

def euclidean_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

def nearest_neighbor_tour(start, cities):
    tour = [start]
    current = start
    total_cost = 0

    while len(cities) > 0:
        next_city = min(cities, key=lambda x: euclidean_distance(coordinates[current], coordinates[x]))
        total_cost += euclidean_distance(coordinates[current], coordinates[next_city])
        current = next_city
        tour.append(current)
        cities.remove(current)

    # Adding the return to the depot
    total_cost += euclidean_distance(coordinates[current], coordinates[0])
    tour.append(0)

    return tour, total_cost

def solve_tsp_with_clusters(points, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(points)
    clusters = kmeans.labels_

    tours = []
    costs = []

    for i in range(num_clusters):
        # Get the cities for this cluster
        cluster_cities = [index for index, label in enumerate(clusters) if label == i]
        if len(cluster_cities) == 0:
            continue
        
        tour, cost = nearest_neighbor_tour(0, cluster_cities)
        tours.append(tour)
        costs.append(cost)

    return tours, costs

# Exclude the depot when clustering
non_depot_cities = list(range(1, len(coordinates)))
clustered_tours, travel_costs = solve_tsp_with_clusters(coordinates[non_depot_cities], num_robots)

overall_total_cost = sum(travel_costs)

# Output results
for i, (tour, cost) in enumerate(zip(clustered_tours, travel_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")