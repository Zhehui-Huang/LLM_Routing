import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from itertools import permutations

def distance_matrix(coordinates):
    n = len(coordinates)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean(coordinates[i], coordinates[j])
    return dist_matrix

def christofides_algorithm(dist_matrix):
    """ Simplified, not fully accurate algorithm for Christofides to be applied to each cluster """
    n = len(dist_matrix)
    # Construct a minimum spanning tree using Prim's algorithm
    parent = [-1] * n 
    min_edge = [float('inf')] * n
    in_mst = [False] * n
    min_edge[0] = 0
    
    for _ in range(n):
        u = min((min_edge[i], i) for i in range(n) if not in_mst[i])[1]
        in_mst[u] = True

        for v in range(n):
            if dist_matrix[u][v] < min_edge[v] and not in_mst[v]:
                min_edge[v] = dist_matrix[u][v]
                parent[v] = u

    # Double the edges to make it a tour (simplistic approach)
    tour = []
    visited = [False] * n
    def visit(vertex):
        if not visited[vertex]:
            visited[vertex] = True
            tour.append(vertex)
            for i in range(n):
                if i == parent[vertex] or parent[i] == vertex:
                    visit(i)

    visit(0)  # Assuming first vertex as root
    tour.append(tour[0])  # Return to start
    
    # Calculate cost
    cost = 0
    for i in range(len(tour)-1):
        cost += dist_matrix[tour[i]][tour[i+1]]
    
    return tour, cost

def solve_robot_tsp(cities_coordinates, num_robots):
    dist_matrix = distance_matrix(cities_coordinates)
    city_indices = list(range(len(cities_coordinates)))
    depot_indices = [0, 1]  # Indexed for depots
    
    # Clustering cities to form subgroups for each robot
    kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities_coordinates)
    labels = kmeans.labels_
    
    robots_tours = []
    robots_costs = []

    for robot_id in range(num_robots):
        cluster_indices = [i for i in city_indices if labels[i] == robot_id or i == depot_indices[robot_id]]
        sub_dist_matrix = dist_matrix[np.ix_(cluster_indices, cluster_indices)]

        tour, cost = christofides_algorithm(sub_dist_matrix)
        final_tour = [cluster_indices[i] for i in tour]
        
        robots_tours.append(final_tour)
        robots_costs.append(cost)

    return robots_tours, robots_costs

# Coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Solve the problem for 2 robots
robots_tours, robots_costs = solve_robot_tsp(coordinates, 2)

# Display results
overall_cost = sum(robots_costs)
for i in range(len(robots_tours)):
    print(f"Robot {i} Tour: {robots_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {round(robots_costs[i], 2)}")

print(f"Overall Total Travel Cost: {round(overall_cost, 2)}")