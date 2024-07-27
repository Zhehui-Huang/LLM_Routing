import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from typing import List, Tuple

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

def calculate_distance(city1: int, city2: int) -> float:
    return euclidean(coordinates[city1], coordinates[city2])

def initial_clusters(K: int) -> List[List[int]]:
    kmeans = KMeans(n_clusters=K, init='k-means++', random_state=0).fit(coordinates)
    clusters = [[] for _ in range(K)]
    for i in range(1, len(coordinates)):  # exclude depot city from clustering
        clusters[kmeans.labels_[i-1]].append(i)
    return clusters

def nearest_neighbor_tour(start: int, cities: List[int]) -> Tuple[List[int], float]:
    tour = [0]
    current = start
    total_distance = 0.0
    unvisited = set(cities)

    while unvisited:
        next_city = min(unvisited, key=lambda x: calculate_distance(current, x))
        total_distance += calculate_distance(current, next_city)
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)

    total_distance += calculate_distance(current, 0)  # Return to depot
    tour.append(0)
    return tour, total_distance

def optimize_tour(tour: List[int]) -> Tuple[List[int], float]:
    # Simple 2-opt swap heuristic for tour optimization
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                if j - i == 1: continue  # consecutive vertices
                new_dist = (calculate_distance(tour[i - 1], tour[j]) +
                            calculate_distance(tour[i], tour[j + 1]))
                old_dist = (calculate_distance(tour[i - 1], tour[i]) +
                            calculate_distance(tour[j], tour[j + 1]))
                if new_dist < old_dist:
                    tour[i:j+1] = tour[i:j+1][::-1]
                    improved = True
    total_distance = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    return tour, total_distance

def solve_tsp(number_of_robots: int) -> None:
    """
    Solves the TSP problem using a cluster-first, route-second approach with 2-opt optimization.
    """
    clusters = initial_clusters(number_of_robots)
    max_cost = 0
    robot_tours = []

    # Generate initial tours
    for i, cluster in enumerate(clusters):
        cluster_tour, cost = nearest_neighbor_tour(0, cluster)
        optimized_tour, optimized_cost = optimize_tour(cluster_tour)
        robot_tours.append((optimized_tour, optimized_cost))
        max_cost = max(max_cost, optimized_cost)
        print(f"Robot {i} Tour: {optimized_tour}")
        print(f"Robot {i} Total Travel Cost: {optimized_cost}")
        
    print(f"Maximum Travel Cost: {max_cost}")

# Set up problem
number_of_robots = 8
solve_tsp(number_of_robots)