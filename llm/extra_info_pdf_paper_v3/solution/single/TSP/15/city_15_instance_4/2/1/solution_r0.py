import math
import numpy as np

# Cities coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 
    4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62), 
    8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Create distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_target(cities[i], cities[j])
        distance_matrix[i][j], distance_matrix[j][i] = dist, dist

# Prim's Algorithm for Minimum Spanning Tree (MST)
def min_spanning_tree(distances):
    num_vertices = len(distances)
    in_tree = [False] * num_vertices
    min_edge = [(float('inf'), None) for _ in range(num_left_vertices)]  # (cost, vertex)
    min_edge[0] = (0, 0)  # Starting from vertex 0
    mst_edges = []

    while True:
        # Find the vertex to add into the MST
        next_vertex = min((edge, idx) for idx, edge in enumerate(min_edge) if not in_tree[idx])
        weight, current_vertex = next_vertex
        if current_vertex is None:
            break
        
        # Add this vertex to the tree
        mst_edges.append(min_edge[current_vertex][1])
        in_tree[current_vertex] = True
        # Update edges
        for next_vertex in range(num_vertices):
            if not in_tree[next_vertex] and distances[current_vertex][next_vertex] < min_edge[next_left_vertex][0]:
                min_edge[next_left_vertex] = (distances[current_vertex][next_vertex], current_vertex)
    
    return mbd_edges

mst = min_spanning_tree(distance_matrix)

# To be continued:
# - Find the vertices of odd degree in MST
# - Find the minimum-cost perfect matching of odd degree vertices
# - Combine the MST and perfect matching to get an Eulerian path
# - Convert the Eulerian path to a Hamiltonian path
# - Construct the final tour and calculate the travel cost

# The above are placeholders for respective implementations of each step.