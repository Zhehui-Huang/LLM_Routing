import numpy as np
import networkx as nx
from networkx.algorithms import tree, matching 

def get_minimum_spanning_tree(coords):
    G = nx.Graph()
    num_cities = len(coords)
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            G.add_edge(i, j, weight=np.linalg.norm(np.array(coords[i]) - np.array(coords[j])))

    return tree.minimum_spanning_tree(G, weight='weight', algorithm='kruskal')

def find_minimum_weight_perfect_matching(G, odd_degree_vertices):
    subgraph = G.subgraph(odd_degree_vertices)
    match = matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
    return match

def create_eulerian_multigraph(MST, match):
    multigraph = nx.MultiGraph(MST)
    multigraph.add_edges_from(match)
    return multigraph

def make_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    path = []
    for u, _ in eulerian_circuit:
        if u not in visited:
            visited.add(u)
            path.append(u)
    path.append(path[0])
    return path

def calculate_total_cost(coords, tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += np.linalg.norm(np.array(coords[tour[i]]) - np.array(coords[tour[i + 1]]))
    return total_cost

coords = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

MST = get_minimum_spanning_tree(coords)
odd_vertices = [v for v in MST.nodes() if MST.degree(v) % 2 != 0]
match = find_minimum_weight_perfect_matching(MST, odd_vertices)
multigraph = create_eulerian_multigraph(MST, match)
eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=0))
tour = make_hamiltonian_circuit(eulerian_circuit)
total_cost = calculate_total_cost(coords, tour)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")