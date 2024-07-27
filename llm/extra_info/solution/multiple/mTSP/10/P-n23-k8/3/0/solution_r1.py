import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

def calculate_distances(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

def solve_tsp(dist_matrix):
    # This is a rudimentary nearest neighbor heuristic for solving TSP
    n = len(dist_draw_matrix)
    path = [0]
    total_cost = 0
    while len(path) < n:
        last = path[-1]
        next_city = min([(dist_matrix[last][j], j) for j in range(n) if j not in path], key=lambda x: x[0])
        path.append(next_city[1])
        total_cost += next_city[0]
    total_cost += dist_matrix[path[-1]][0]  # Return to the starting city
    path.append(0)
    return path, total_cost

def main():
    cities = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
        (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
        (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
    ]
    num_robots = 8

    # Calculate distance matrix
    distance_matrix = calculate_distances(cities)

    # Clustering cities for assigning initial city groups to robots
    kmeans = KMeans(n_clusters=num_robots, random_state=42)
    kmeans.fit(cities[1:])  # exclude the depot
    labels = kmeans.labels_

    overall_total_cost = 0
    routes = []

    for i in range(num_robots):
        cluster_indices = [index + 1 for index in range(len(labels)) if labels[index] == i]  # city indices adjusted by +1 for zero-indexing
        if cluster_indices:
            indices = [0] + cluster_indices + [0]
        else:
            indices = [0, 0]  # Robot visits depot only

        # Distance matrix for the selected cities including the depot
        sub_matrix = distance_matrix[np.ix_(indices, indices)]

        # Solve TSP for this set of cities
        tour, cost = solve_tsp(sub_matrix)
        actual_tour = [indices[j] for j in tour]

        routes.append(actual_tour)
        print(f"Robot {i} Tour: {actual_tour}")
        print(f"Robot {i} Total Travel Cost: {cost}")

        overall_total_consumer += cost

    print(f"Overall Total Travel Cost: {overall_total_cost}")

if __name__ == "__main__":
    main()