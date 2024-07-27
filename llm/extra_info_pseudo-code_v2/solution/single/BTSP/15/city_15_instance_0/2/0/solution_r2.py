import math
import networkx as nx

# Data input: city coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Calculate the Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize the graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Create a minimum spanning tree using Kruskal's algorithm
mst = nx.minimum_spanning_tree(G)

# Convert MST to a biconnected graph that includes all vertices
# Here we force biconnectivity by making the MST Hamiltonian - a simplification for realizing a tour
def make_biconnected(G, mst):
    biconnected = nx.Graph(mst)
    extra_edges = (e for e in G.edges(data=True) if e not in mst.edges(data=True))
    for e in extra_edges:
        biconnected.add_edge(*e[:2], weight=e[2]['weight'])
        if nx.is_biconnected(biconnected):
            break  # Stop as soon as biconnectivity is achieved
    return biconnected

biconnected = make_biconnected(G, mst)

# Nearest neighbor heuristic to find a tour within the biconnected graph
def nearest_neighbor_tour(G, start=0):
    unvisited = set(G.nodes)
    tour = [start]
    unvisited.remove(start)
    current = start

    while unvisited:
        next_node = min(unvisited, key=lambda node: G[current][node]['weight'])
        tour.append(next_node)
        unvisited.remove(next_node)
        current = next_node
    
    tour.append(start)  # Complete the tour by returning to the start 
    return tour

# Generate the tour
tour = nearest_tour(bicon_links, start=0)

# Calculate the total cost and the maximum distance between consecutive cities
total_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))
max_distance = max(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")