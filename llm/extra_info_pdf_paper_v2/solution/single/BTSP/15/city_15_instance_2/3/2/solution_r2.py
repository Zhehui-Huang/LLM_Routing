import math
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Function to calculate Euclidean distance
def euclidean_dist(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Calculate distance matrix
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i, j] = euclidean_dist(i, j)

# Find the minimum spanning tree
mst = minimum_spanning_tree(csr_matrix(dist_matrix))

# Create an undirected graph from the MST
graph = nx.Graph()
for i in range(num_cities):
    for j in range(num_cities):
        if mst[i, j] > 0:
            graph.add_edge(i, j, weight=mst[i, j])

# Function to find an approximate Hamiltonian cycle (tour) using the 1-tree approach
def find_tour(graph, start_node=0):
    # Phase 1: Find a spanning tree rooted at the starting node
    mst_tree = nx.minimum_spanning_tree(graph, weight='weight')
    
    # Phase 2: Convert the tree to a tour by traversing it using DFS
    def dfs(graph, node, visited=None, tour=None):
        if visited is None:
            visited = set()
        if tour is None:
            tour = []
        
        visited.add(node)
        tour.append(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                dfs(graph, neighbor, visited, tour)
        return tour

    # Get the tour using DFS
    tour = dfs(mst_tree, start_node)
    tour.append(start_node)  # Close the tour by returning to the start city
    return tour

# Calculate the tour and costs
tour = find_tour(graph)
total_cost, max_distance = calculate_costs(tour, dist_matrix)

# Outputting results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)