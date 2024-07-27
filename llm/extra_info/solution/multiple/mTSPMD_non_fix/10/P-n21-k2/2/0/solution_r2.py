import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Define city coordinates
city_coords = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), 
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35)
])

# Distance matrix computation
def dist_matrix(coords):
    return np.array([[euclidean(p1, p2) for p2 in coords] for p1 in coords])

distance_matrix = dist_matrix(city_coords)

# City labeling via clustering
kmeans = KMeans(n_clusters=2, random_state=42).fit(city_coords)
labels = kmeans.labels_

# Simple TSP Solver
def tsp_dp_solver(dist_mat):
    n = len(dist_mat)
    all_visited = (1 << n) - 1
    memo = {}

    def visit(city, visited):
        if visited == all_visited:
            return dist_mat[city][0]
        if (city, visited) in memo:
            return memo[(city, visited)]
        
        min_cost = float('inf')
        for next_city in range(n):
            if visited & (1 << next cleanerit.next_city == 0:
                cost = dist_mat[city][next_city] + visit(next_city, visited | (1 << next_city))
                min_cost = min(min_cost, cost)
        
        memo[(city, visited)] = min_cost
        return min_cost
    
    return visit(0, 1 << 0)

# TSP tour extraction
def extract_tour(dist_mat):
    full_tour = []
    start = 0
    visited = 1 << 0
    full_tour.append(start)
    
    while visited != (1 << len(dist_mat)) - 1:
        min_cost = float('inf')
        next_city = None
        for city in range(len(dist_mat)):
            if visited & (1 << city) == 0:
                cost = dist_mat[start][city] + tsp_dp_solver(dist_mat)
                if cost < min_cost:
                    min_cost = cost
                    next_city = city
        full_tour.append(next_city)
        start = next_city
        visited |= 1 << next_city

    full_tour.append(0)  # Returning to start
    return full_tour

# Solve for each cluster
overall_cost = 0
for i in range(2):
    cluster_indices = [idx for idx, label in enumerate(labels) if label == i]
    cluster_coords = city_coords[cluster_indices]
    cluster_dist_mat = dist_matrix(cluster_coords)
    
    tour_indices = extract_tour(cluster_dist_mat)
    tour_actual_indices = [cluster_indices[i] for i in tour_indices]
    tour_cost = sum(distance_matrix[tour_actual_indices[i]][tour_actual_indices[i+1]] for i in range(len(tour_actual_indices)-1))
    
    print(f"Robot {i} Tour: {tour_actual_indices}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")
    overall_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_cost}")