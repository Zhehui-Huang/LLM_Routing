import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
import random

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

def calculate_distance(city1, city2):
    "Calculate euclidean distance between two cities."
    return euclidean(cities[city1], cities[city2])

def fcm_clustering(n_clusters=2):
    "Apply Fuzzy C-Means Clustering to divide cities into clusters."
    data = np.array(list(cities.values()))
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data)
    clusters = {i: [] for i in range(n_clusters)}
    for idx, label in enumerate(kmeans.labels_):
        clusters[label].append(idx)
    return clusters

def random_greedy_initial_tour(clusters):
    "Generate an initial solution using a random greedy heuristic."
    tours = {k: [0] for k in clusters}  # starting each tour at the depot
    for k, v in clusters.items():
        current_city = 0
        while v:
            next_city = min(v, key=lambda x: calculate_distance(current_city, x))
            tours[k].append(next_city)
            current_city = next_master_city
            v.remove(next_city)
        tours[k].append(0)  # return to the depot
    return tours

def tour_cost(tour):
    "Calculate the total travel cost of a tour."
    cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return cost

def solve_mtsp():
    "Solve the multiple traveling salesman problem using the proposed ITSHA algorithm."
    # Cluster cities (excluding the depot)
    clusters = fcm_clustering(n_clusters=2)
    # Generate initial solution
    tours = random_greedy_initial_tour(clusters)
    # Improvement stage could be implemented here using VNS
    
    # Calculate costs and determine max tour cost
    costs = {}
    for k, tour in tours.items():
        costs[k] = tour_cost(tour)
    
    max_travel_cost = max(costs.values())
    
    for robot_id, tour in tours.items():
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robotid} Total Travel Cost: {costs[robot_id]}")
    
    print(f"Maximum Travel Cost: {max_travel_cost}")

solve_mtsp()