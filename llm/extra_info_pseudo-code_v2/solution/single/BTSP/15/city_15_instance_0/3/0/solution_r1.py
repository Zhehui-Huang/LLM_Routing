from math import sqrt
import networkx as nx

# Define cities and their coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def euclidean_distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Generate edges with weights for all pairs
edges = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Create a graph and add edges
G = nx.Graph()
for (i, j), d in edges.items():
    G.add_edge(i, j, weight=d)

# Step 1: Get edges sorted by weight
sorted_edges = sorted(edges.items(), key=lambda x: x[1])

# Create an empty graph for the biconnected subgraph
subgraph = nx.Graph()

# Add edges from the sorted list until the graph is biconnected
for (u, v), weight in sorted_edges:
    subgraph.add_edge(u, v, weight=weight)
    if nx.is_biconnected(subgraph):
        break

# Check if achieved biconnected subgraph actually is biconnected
if not nx.is_biconnected(subgraph):
    print("Failed to achieve a biconnected graph with the procedure.")
else:
    # Step 2: Use biconnected subgraph to find a tour
    # Create G^2
    G2 = nx.power(subgraph, 2)

    # Find a Hamiltonian cycle in G^2 (approximation since the problem is NP-hard)
    cycle = nx.approximation.greedy_tsp(G2, weight='weight')  
    cycle.append(cycle[0])  # Make it a cycle by adding the start node at the end

    # Calculate cycle properties
    total_distance = sum(edges[(cycle[i], cycle[i + 1])] if (cycle[i], cycle[i + 1]) in edges else edges[(cycle[i + 1], cycle[i])] for i in range(len(cycle) - 1))
    max_distance = max(edges[(cycle[i], cycle[i + 1])] if (cycle[i], cycle[i + 1]) in edges else edges[(cycle[i + 1], cycle[i])] for i in range(len(cycle) - 1))
    
    # Output results
    print(f"Tour: {cycle}")
    print(f"Total travel cost: {total_distance:.2f}")
    print(f"Maximum distance between consecutive cities: {max_distance:.2f}")