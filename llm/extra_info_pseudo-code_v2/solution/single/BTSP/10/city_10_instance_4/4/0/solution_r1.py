import math
import networkx as nx

# Define cities and their coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9), 
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Compute Euclidean distance between two cities
def distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create a complete graph with distances as weights
def build_complete_graph():
    G = nx.complete_graph(len(cities))
    for u, v in G.edges():
        G[u][v]['weight'] = distance(u, v)
    return G

# Generate a biconnected graph that still tries to minimize the max weight in a Hamiltonian circuit
def minimum_spanning_tree_biconnected(G):
    T = nx.minimum_spanning_tree(G, weight='weight')
    extra_edges = [e for e in G.edges(data=True) if e not in T.edges(data=True)]
    sorted_extra_edges = sorted(extra_edges, key=lambda e: e[2]['weight'])

    for u, v, data in sorted_extra_ls:
        T.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(T):
            break

    return T

def find_tsp_tour(G):
    # Use a simple approximation to get a TSP tour based on MST heuristic
    mst = nx.minimum_spanning_tree(G, weight='weight')
    all_nodes = list(nx.dfs_preorder_nodes(mst, 0))  # Start DFS from node 0
    all_nodes.append(all_nodes[0])  # Complete the circuit to the starting node

    return all_nodes

# Main function
def main():
    G = build_complete_related_graph()
    subG = minimum_spanning_tree_biconnected(G)
    tour = find_tsp_tour(subG)

    # Calculate the tour cost and the maximum edge cost in the tour
    total_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))
    max_dist = max(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_dist)

if __name__ == "__main__":
    main()