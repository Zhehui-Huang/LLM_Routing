import math
import itertools

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def is_biconnected(graph, V):
    """ Check if the graph is biconnected. Placeholder implementation. """
    if len(graph) < 3:
        return False
    return True

# City coordinates
cities = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
          (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
          (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)]

# Graph creation
n = len(cities)
adj_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Bottleneck-optimal biconnected subgraph: Algorithm BB
edges = [(i, j, adj_matrix[i][j]) for i in range(n) for j in range(i+1, n)]
edges.sort(key=lambda x: x[2])

# Constructing biconnected graph
E_BB = []
biconnected = False

for edge in edges:
    E_BB.append(edge)
    if is_biconnected(E_BB, n):
        biconnected = True
        break

if not biconnected:
    raise Exception("No biconnected graph found.")

# Retrieving maximum cost of these edges
max_cost_in_graph = max(edge[2] for edge in E_BB)

# Tour Identification
# Find a Hamiltonian cycle: simple approach - not optimal, proof-of-concept using a simple nearest neighbour heuristic with restarts from each vertex
def find_tour(start, vertices, distance_matrix):
    remaining = set(vertices)
    remaining.remove(start)
    tour = [start]
    current = start
    
    while remaining:
        next_city = min(remaining, key=lambda x: distance_matrix[current][x])
        tour.append(next_city)
        current = next_city
        remaining.remove(next_city)
    
    tour.append(start)  # return to depot
    return tour

# Try all possible starts for the best short initial paths (brute force approach)
best_tour = []
best_max_distance = float('inf')
total_cost = 0

for start in range(n):
    tour = find_tour(start, range(n), adj_matrix)
    max_distance = max(adj_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    tour_cost = sum(adj_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

    if max_distance < best_max_distance:
        best_max_distance = max_distance
        best_tour = tour
        total_cost = tour_cost

# Final Outputs
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {best_max_compress:.2f}")