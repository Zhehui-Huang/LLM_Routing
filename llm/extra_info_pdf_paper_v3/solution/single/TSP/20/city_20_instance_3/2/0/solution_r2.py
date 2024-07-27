import math
import networkx as nx

# Coordinates for the cities
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25),
    11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculates the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generating a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(i, j))

# Construct the minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G)

# Extract vertices with odd degrees in the MST
odd_degree_vertices = [v for v, degree in mst.degree() if degree % 2 == 1]
odd_subgraph = G.subgraph(odd_degree_vertices)

# Find minimum weight perfect matching in the subgraph of odd degree vertices
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True)

# Add matching edges to the MST to make it Eulerian
mst.add_edges_from(matching)

# Find an Eulerian tour
eulerian_tour = list(nx.eulerian_circuit(mst, source=0))

# Convert the Eulerian tour to Hamiltonian by removing repeated visits
hamiltonian_path = [0]
visited = set([0])
for u, v in eulerian_tour:
    if v not in visited:
        visited.add(v)
        hamiltonian_path.append(v)

# Closing the loop back to the starting point, the depot
hamiltonian_path.append(0)

# Calculate the total travel distance of the Hamiltonian tour
total_travel_distance = sum(euclidean_distance(hamiltonian_path[i], hamiltonian_path[i+1]) for i in range(len(hamiltonian_path) - 1))

# Output the result
print("Tour:", hamiltonian_path)
print("Total travel cost:", total_travel_distance)