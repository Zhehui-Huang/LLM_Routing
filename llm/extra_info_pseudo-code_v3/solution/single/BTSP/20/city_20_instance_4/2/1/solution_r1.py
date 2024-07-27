import math
from itertools import combinations
import networkx as nx

# Define the cities' coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29), 
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), 
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Compute euclidean distances between all pairs of cities
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(coordinates)
edges = [(i, j, euclidean_distance(coordinates[i], coordinates[j]))
         for i in range(n) for j in range(n) if i != j]

# Create a graph
G = nx.Graph()
G.add_weighted_edges_from(edges)

# Sort edges by weight
sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

def find_hamiltonian_path(G, n):
    # Check for Hamiltonian circuit in subgraph up to threshold
    for edge in sorted_edges:
        weight = edge[2]['weight']
        # Create subgraph with edges having weight <= current weight
        subG = nx.Graph()
        subG.add_edges_from([e for e in sorted_edges if e[2]['weight'] <= weight])
        # Try to find a Hamiltonian circuit in the subgraph
        if nx.is_connected(subG) and subG.number_of_edges() >= n:
            try:
                # Use the approximation algorithm of traveling salesman problem to find a path
                cycle = nx.approximation.traveling_salesman_problem(subG, cycle=True)
                # Ensure the cycle starts and ends at the depot
                if cycle[0] == 0:
                    return cycle, weight
            except nx.NetworkXError:
                continue
    return None, None

# Finding the path
ham_path, max_edge_weight = find_hamiltonian_path(G, n)

if ham_path:
    # Calculate total travel cost
    total_cost = sum(euclidean_distance(coordinates[ham_path[i]], coordinates[ham_path[i+1]]) for i in range(n))
    print("Tour:", ham_path)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_edge_weight)
else:
    print("No Hamiltonian circuit is possible")