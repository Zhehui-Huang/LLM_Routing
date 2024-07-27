import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

def calculate_distance(city1: int, city2: int) -> float:
    """Calcualte Euclidean distance between two cities."""
    return euclidean(coordinates[city1], coordinates[city2])

def initial_clusters(K: int) -> list:
    """Cluster cities into K clusters using KMeans, excluding the depot city."""
    # Exclude depot city for clustering
    kmeans = KMeans(n_clusters=K, random_state=42).fit(coordinates[1:])  
    clusters = [[] for _ in range(K)]
    for idx, label in enumerate(kmeans.labels_):
        clusters[label].append(idx + 1)  # +1 to correct index for actual city label
    return clusters

def nearest_neighbor_tour(start: int, cities: list) -> tuple:
    """Generate a tour using the Nearest Neighbor heuristic starting from the depot."""
    tour = [start]
    current_city = start
    total_cost = 0
    unvisited = set(cities)

    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(current_city, city))
        total_cost += calculate_distance(current_city, next_city)
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    total_cost += calculate_distance(current_city, start)  # return to depot
    tour.append(start)
    return tour, total_cost

def compute_all_tours(num_robots: int):
    """Compute the tours for each robot and print their paths and costs, along with the maximum cost."""
    clusters = initial_clusters(num_robots)
    tours = []
    max_travel_cost = 0

    for i, cluster in enumerate(clusters):
        tour, cost = nearest_neighbor_tour(0, cluster)
        tours.append((tour, cost))
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost}")
        max_travel_cost = max(max_travel_cost, cost)

    print(f"Maximum Travel Cost: {max_travel_cost}")

# Running the solution for 8 robots
compute_all_tours(8)