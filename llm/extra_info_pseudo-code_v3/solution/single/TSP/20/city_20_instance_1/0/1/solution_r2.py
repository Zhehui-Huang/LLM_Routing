import math
import networkx as nx

# Cities coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Build and process the graph
def build_graph(cities):
    G = nx.Graph()
    for i in cities:
        for j in cities:
            if i != j:
                G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

def find_path(G):
    # Step 1: Minimum spanning tree
    T = nx.minimum_spanning_tree(G, weight='weight')
    
    # Step 2: Get vertices with an odd degree
    odd_vertices = [v for v in T.nodes if T.degree(v) % 2 != 0]
    
    # Step 3: Find minimum weight perfect matching
    minimum_perfect_matching = nx.Graph()
    
    for subset in itertools.combinations(odd_vertices, 2):
        minimum_perfect_matching.add_edge(subset[0], subset[1], weight=G[subset[0]][subset[1]]['weight'])
        
    matching = nx.algorithms.matching.min_weight_matching(minimum_perfect_matching, maxcardinality=True)
    
    # Step 4: Combine edges of T and M to form multigraph
    multigraph = nx.MultiGraph(T)
    multigraph.add_edges_from(matching)
    
    # Step 5: Find Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=0))
    
    # Step 6: Convert to Hamiltonian circuit
    path, visited = [0], {0}
    for u, v in eulerian_circuit:
        if v not in visited:
            path.append(v)
            visited.add(v)
    path.append(0)
    
    total_distance = sum([euclidean_distance(cities[path[i]], cities[path[i + 1]]) for i in range(len(path) - 1)])
    return path, total_distance

G = build_graph(cities)
tour, total_cost = find_path(G)

print("Tour:", tour)
print("Total travel cost:", total_cost)