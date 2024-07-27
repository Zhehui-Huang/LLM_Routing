import math
import itertools
import networkx as nx
from networkx.algorithms.approximation.traveling_salesman import christofides

# Defining the Euclidean distance function
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute distances and sort edges
positions = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]
edges = []
edge_weights = []
n = len(positions)

# Creating all possible edges with their weights
for i in range(n):
    for j in range(i + 1, n):
        weight = euclidean_distance(positions[i], positions[j])
        edges.append((i, j, weight))
        edge_weights.append(weight)

# Sorting weights to proceed with the bottleneck algorithm
edge_weights = sorted(list(set(edge_weights)))

# Function to check Hamiltonian cycle existence
def has_hamiltonian_cycle(threshold):
    # Build graph with edges under given threshold
    G = nx.Graph()
    for (u, v, weight) in edges:
        if weight <= threshold:
            G.add_edge(u, v, weight=weight)

    # Attempt to find a Hamiltonian cycle using the Christofides algorithm as heuristic
    if nx.is_connected(G) and G.number_of_nodes() == n: 
        try:
            cycle = christofides(G, weight='weight')
            max_edge = max(euclidean_distance(positions[cycle[i]], positions[cycle[i+1]]) for i in range(len(cycle)-1))
            return True, cycle, max_edge
        except:
            return False, [], float('inf')
    else:
        return False, [], float('inf')

# Main algorithm to minimize maximum distance in tour
for weight in edge_weights:
    found, tour, max_distance = has_hamiltonian_cycle(weight)
    if found:
        total_travel_cost = sum(euclidean_distance(positions[tour[i]], positions[tour[i+1]]) for i in range(len(tour)-1))
        # Print the found path, cost and bottleneck distance
        print(f"Tour: {tour + [tour[0]]}")
        print(f"Total travel cost: {total_travel_cost:.2f}")
        print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
        break