import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Create distance matrix
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Standard Union-Find data structure with path compression and union by rank
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            else:
                self.parent[rootP] = rootQ
                if self.rank[rootP] == self.rank[rootQ]:
                    self.rank[rootQ] += 1

# Kruskal's Algorithm to find MST
def kruskal(n):
    edges = [(distances[(u, v)], u, v) for u in cities for v in cities if u < v]
    edges.sort()
    uf = UnionFind(n)
    mst = []
    for cost, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v))
    return mst

# Finding the node with odd degree
def find_odd_degree_nodes(n, mst):
    degree = [0] * n
    for u, v in mst:
        degree[u] += 1
        degree[v] += 1
    odd_degree_nodes = [i for i in range(n) if degree[i] % 2 == 1]
    return odd_degree_nodes

# Minimum Weight Perfect Matching for the nodes of odd degree using Greedy Approach
def min_weight_perfect_matching(n, odd_degree_nodes):
    import sys
    match = []
    visited = [False] * n
    while odd_degree_nodes:
        u = odd_degree_nodes.pop()
        visited[u] = True
        min_cost = sys.maxsize
        min_v = -1
        for v in odd_degree_nodes:
            if not visited[v] and distances[(u, v)] < min_cost:
                min_cost = distances[(u, v)]
                min_v = v

        if min_v != -1:
            odd_degree_nodes.remove(min_v)
            visited[min_v] = True
            match.append((u, min_v))
    return match

# Combine the edges in MST and MWM to form the Eulerian graph
def eulerian_graph(mst, mwm):
    graph = {}
    for u, v in mst:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    for u, v in mwm:
        graph[u].append(v)
        graph[v].append(u)
    return graph

# Hierholzer's algorithm to find Eulerian Circuit
def find_eulerian_circuit(graph, start):
    circuit = []
    stack = [start]
    while stack:
        v = stack[-1]
        if graph[v]:
            u = graph[v].pop()
            stack.append(u)
            # Remove the edge u-v from the graph
            graph[u].remove(v)
        else:
            circuit.append(stack.pop())
    return circuit[::-1]

# Convert Eulerian circuit to Hamiltonian circuit
def convert_to_hamiltonian_circuit(circuit):
    visited = set()
    hamiltonian_circuit = []
    for node in circuit:
        if node not in visited:
            visited.add(node)
            hamiltonian_circuit.append(node)
    hamiltonian_circuit.append(hamiltonian_circuit[0])  # To make it a complete cycle
    return hamiltonian_circuit

def calculate_tour_cost(circuit):
    total_cost = 0
    for i in range(len(circuit) - 1):
        total_cost += distances[(circuit[i], circuit[i+1])]
    return total_cost

# Main function to solve the TSP
def solve_tsp():
    n = len(cities)  # Number of cities
    mst = kruskal(n)  # Step 1: Compute MST
    odd_degree_nodes = find_odd_degree_nodes(n, mst)  # Step 2: Find nodes with odd degree from MST
    mwm = min_weight_perfect_matching(n, odd_degree_nodes)  # Step 3: Minimum weight perfect matching on odd degree nodes
    graph = eulerian_graph(mst, mwm)  # Step 4: Create the Eulerian graph
    eulerian_circuit = find_eulerian_circuit(graph, 0)  # Step 5: Find an Eulerian circuit
    hamiltonian_circuit = convert_to_hamiltonian_circuit(eulerian_circuit)  # Step 6: Convert Eulerian circuit to Hamiltonian circuit
    total_cost = calculate_tour_cost(hamiltonian_circuit)  # Calculate the total cost of the entire tour
    return hamiltonian_circuit, total_cost

# Running the TSP Solver
tour, total_travel_cost = solve_tsp()

# Output the solution
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)