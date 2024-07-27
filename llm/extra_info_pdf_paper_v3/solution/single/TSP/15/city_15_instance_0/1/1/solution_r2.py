import math
import networkx as nx

# Coordinates of the cities
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50),
    4: (21, 23), 5: (88, 59), 6: (79, 77), 7: (63, 23),
    8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Creating the graph
G = nx.Graph()

# Adding weighted edges based on Euclidean distance
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=calculate_years(cities[i], cities[j]))

# Finding the Minimum Spanning Tree (MST)
MST = nx.minimum_spanning_tree(G)

# Identifying vertices with odd degree
odd_degree_nodes = [node for node, degree in MST.degree() if degree % 2 == 1]
odd_subgraph = G.subgraph(odd_degree_nodes)

# Finding Minimum-Cost Perfect Matching in the subgraph of odd-degree vertices
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Adding matches to the MST to make it Eulerian
MST.add_edges_from(matching)

# Finding an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(MST, source=0))

# Converting Eulerian circuit to a Hamiltonian path
visited = set()
tour = []
for u, v in eulerian_circuit:
    if not visited or v == 0:
        tour.append(v)
        visited.add(v)

# Ensuring the tour concludes at the starting point
if tour[0] != 0:
    tour.insert(0, 0)
if tour[-1] != 0:
    tour.append(0)

# Calculating the total travel cost
total_distance = sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

# Printing the outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")