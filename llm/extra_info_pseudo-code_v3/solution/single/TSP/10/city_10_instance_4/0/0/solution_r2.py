import math
import networkx as nx
from itertools import combinations

# Define the cities coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate the Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create a complete graph
G = nx.complete_graph(len(cities))
for i in cities:
    for j in cities:
        if i != j:
            G[i][j]['weight'] = calc_away(cities[i], cities[j])

# Step 1: Compute a minimum spanning tree (MST)
T = nx.minimum_spanning_tree(G)

# Step 2: Identify vertices with odd degree in T
O = [v for v in T if T.degree(v) % 2 == 1]

# Step 3: Minimum weight perfect matching on the subgraph of odd degree vertices
O_graph = G.subgraph(O)
min_weight_matching = nx.algorithms.matching.min_weight_matching(O_graph, maxcardinality=True)

# Step 4: Combine edges of T and minimum weight matching to form multigraph
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Create an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit to a Hamiltonian path
hamiltonian_path = [0]
visited = set([0])
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_path.append(v)
hamiltonian_path.append(0)  # return to the depot city

# Calculate the total travel cost of the tour
total_cost = sum(calc_distance(hamiltonian_path[i], hamiltonian_path[i + 1]) for i in range(len(hamiltonian_path) - 1))

# Printing the tour and the total cost
print("Tour:", hamiltonian_path)
print("Total travel cost:", total_cost)