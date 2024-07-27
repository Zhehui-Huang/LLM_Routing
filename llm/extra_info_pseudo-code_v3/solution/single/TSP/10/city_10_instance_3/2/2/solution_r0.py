import math
import itertools
import networkx as nx
from heapq import heappush, heappop

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def minimum_spanning_tree(points):
    n = len(points)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            weight = euclidean_distance(points[i], points[j])
            heappush(edges, (weight, i, j))
    
    mst = nx.Graph()
    mst.add_nodes_from(range(n))
    
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True
        return False
    
    num_edges = 0
    while edges and num_edges < n - 1:
        weight, u, v = heappop(edges)
        if union(u, v):
            mst.add_edge(u, v, weight=weight)
            num_edges += 1
    
    return mst

def odd_degree_vertices(mst):
    return [v for v in mst.nodes() if mst.degree(v) % 2 == 1]

def minimum_weight_perfect_matching(mst, odd_vertices, points):
    num_vertices = len(odd_vertices)
    min_weight_match = nx.Graph()
    min_weight_match.add_nodes_from(odd_vertices)

    if num_vertices <= 1:
        return min_weight_match

    # Calculate all pair distances
    dist = {(i, j): euclidean_distance(points[i], points[j]) for i, j in itertools.combinations(odd_vertices, 2)}

    # Find minimum weight perfect matching using Blossom algorithm
    from scipy.optimize import linear_sum_assignment
    cost_matrix = [[dist[i, j] if (i, j) in dist else 1e9 for j in odd_vertices] for i in odd_region_vertices]
    row_ind, col_ind = linear_sum_assignment(cost_matrix)

    for i, j in zip(row_ind, col_ind):
        weight = euclidean_distance(points[odd_vertices[i]], points[odd_vertices[j]])
        min_weight_match.add_edge(odd_vertices[i], odd_vertices[j], weight=weight)

    return min_weight_match

def find_eulerian_circuit(multigraph, start_vertex):
    return list(nx.eulerian_circuit(multigraph, source=start_vertex))

def christofides_algorithm(points):
    # Step 1: Calculate MST
    mst = minimum_spanning_tree(points)

    # Step 2: Find vertices with odd degree
    odd_vertices = odd_degree_vertices(mst)

    # Step 3: Find a minimum weight perfect matching in the subgraph induced by odd degree vertices
    matching = minimum_weight_perfect_matching(mst, odd_vertices, points)

    # Step 4: Combine MST and matching
    multigraph = nx.MultiGraph(mst)
    multigraph.add_edges_from(matching.edges(data=True))

    # Step 5: Find an Eulerian circuit
    eulerian_circuit = find_eulerian_circuit(multigraph, start_vertex=0)

    # Step 6: Convert to Hamiltonian circuit
    visited = set()
    hamiltonian_circuit = []
    for u, v in eulerian_circuit:
        if u not in visited:
            hamiltonian_circuit.append(u)
            visited.add(u)
    hamiltonian_circuit.append(0)  # to return to the depot
    
    # Calculate total travel cost
    total_cost = sum(euclidean_distance(points[hamiltonian_circuit[i]], points[hamiltonian_circuit[i+1]]) for i in range(len(hamiltonian_circuit)-1))
    
    return hamiltonian_circuit, total_cost

# Coordinates of cities (depot + cities 1 to 9)
coordinates = [
    (84, 67),  # Depot 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

tour, cost = christofides_algorithm(coordinates)
print("Tour:", tour)
print("Total travel cost:", cost)