import math
from itertools import combinations

# The coordinates for each city, including the depot
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Number of cities
num_cities = len(cities)

# Creating a complete graph with the cities and distances
distances = { (min(a, b), max(a, b)): calculate_distance(a, b) for a, b in combinations(range(num_cities), 2) }

from scipy.optimize import linear_sum_assignment

# Build a NxN distance matrix
dist_matrix = [[calculate_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Find the minimum spanning tree (Prim's algorithm)
import heapq

def minimum_spanning_tree(size, weight_matrix):
    # Visited nodes
    visited = [False] * size
    # Min-Heap to store the minimum weight edge at top
    min_edge = [(0, 0)]  # (cost, start_vertex)
    mst_edges = []
    total_cost = 0

    while len(mst_edges) < size:
        cost, u = heapq.heappop(min_edge)

        if visited[u]:
            continue

        visited[u] = True
        total_cost += cost
        
        for v in range(size):
            if not visited[v] and weight_matrix[u][v] != 0:
                heapq.heappush(min_edge, (weight_matrix[u][v], v))
                
        if cost != 0:
            mst_edges.append((u, v))

    return mst_edges, total_cost

# Get MST
mst_edges, _ = minimum_spanning_tree(num_cities, dist_matrix)

# Odd degree vertices in MST
odd_degree_vertices = [x for x in range(num_cities) if sum(1 for i, j in mst_edges if i == x or j == x) % 2 == 1]

# Minimum cost perfect matching among the odd degree vertices
odd_graph = [[(dist_matrix[i][j] if i in odd_degree_vertices and j in odd_degree_vertices else float('inf')) for j in range(num_cities)] for i in range(num_cities)]
row_ind, col_ind = linear_sum_assignment(odd_graph)
matching = [(row, col) for row, col in zip(row_ind, col_ind) if row in odd_degree_vertices and col in odd_degree_vertices]

# Combine edges of MST and matching to form the Eulerian graph
eulerian_graph = mst_edges + matching

# Eulerian tour into Hamiltonian path
def hamiltonian_path(eulerian_edges, start_node):
    # Simple implementation to convert eulerian circuit to hamiltonian path
    tour = [start_node]
    visited = set()
    visited.add(start_node)

    def find_next(current):
        for (u, v) in eulerian_edges:
            if u == current and v not in visited:
                tour.append(v)
                visited.add(v)
                eulerian_edges.remove((u, v))
                find_next(v)
                break
            elif v == current and u not in visited:
                tour.append(u)
                visited.add(u)
                eulerian_edges.remove((u, v))
                find_next(u)
                break
    
    find_next(start_node)
    return tour

tour = hamiltonian_path(eulerian_graph, 0)

# Calculate the total travel cost of the tour
tour_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", tour_cost)