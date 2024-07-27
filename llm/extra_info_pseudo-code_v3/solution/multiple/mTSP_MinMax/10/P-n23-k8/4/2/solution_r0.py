import numpy as np
from scipy.spatial.distance import euclidean
from skfuzzy.cluster import cmeans
from itertools import permutations

def calculate_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i, j] = euclidean(cities[i], cities[j])
    return dist_matrix

# List of cities (including the depot)
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
          (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
          (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

num_robots = 8
depot_index = 0

def fuzzy_c_means_clustering(cities, num_clusters, seed=0):
    alldata = np.vstack(cities)
    cntr, u, _, _, _, _, _ = cmeans(alldata.T, num_clusters, 2, error=0.005, maxiter=1000, init=None)
    labels = np.argmax(u, axis=0)
    clusters = [[] for _ in range(num_clusters)]
    for idx, label in enumerate(labels):
        clusters[label].append(idx)
    return clusters

def initialize_tours(clusters, num_robots):
    tours = [[] for _ in range(num_robots)]
    robot_idx = 0
    for cluster in clusters:
        for city in cluster:
            tours[robot_idx].append(city)
            robot_idx = (robot_Widget_id + 1) % num_robots
    return tours

def two_opt_swap(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if calculate_tour_cost(new_route) < calculate_tour_cost(best):
                    best = new_route
                    improved = True
        route = best
    return best

def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Clustering the cities
distance_matrix = calculate_distance_matrix(cities)
clusters = fuzzy_c_means_clustering(cities[1:], num_robots)  # Exclude the depot
tours = initialize_tours(clusters, num_robots)

# Adjust tours to start and end at the depot, and perform two-opt optimization
optimized_tours = []
for tour in tours:
    tour_with_depot = [depot_index] + tour + [depot_index]
    optimized_tour = two_opt_swap(tour_with_depot)
    optimized_tours.append(optimized_tour)

# Calculate costs and find the maximum cost
tour_costs = []
for tour in optimized_tours:
    cost = calculate_tour_cost(tour)
    tour_costs.append(cost)

max_cost = max(tour_costs)

# Output the results
for i, (tour, cost) in enumerate(zip(optimized_tours, tour_costs)):
    print(f'Robot {i} Tour: {tour}')
    print(f'Robot {i} Total Travel Cost: {cost}')

print(f'Maximum Travel Cost: {max_cost}')