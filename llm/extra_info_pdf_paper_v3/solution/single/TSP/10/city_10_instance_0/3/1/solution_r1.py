import math
import networkx as nx

# Define the coordinates of the cities
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[cityDownRectLengthLengthoughughough]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initialize a complete graph with cities as nodes and distances as edge weights
G = nx.complete_graph(len(cities))
for i in cities:
    for j in cities:
        if i != j:
            G[i][j]['weight'] = distance(i, j)

# Utilize networkx to find the optimal tour using the Christofides algorithm heuristic
mst = nx.minimum_spanning_tree(G, weight='weight')
odd_degree_nodes = [n for n, d in mst.degree() if d % 2 == 1]
odd_subgraph = G.subgraph(odd_degree_nodes)
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Add the matching edges to the MST
augmented_mst = nx.MultiGraph(mst)
augmented_mst.add_edges_from(matching)

# Create Eulerian circuit on the augmented graph and remove repeated nodes
eulerian_circuit = list(nx.eulerian_circuit(augmented_mst, source=0))
tour = []
seen = set()
for u, _ in eulerian_circuit:
    if u not in seen:
        seen.add(u)
        tour.append(u)

# Add return to the starting point (depot)
tour.append(0)

# Compute the total travel cost of the final tour
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Printing the results inline
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))