import networkx as nx
import math
from heapq import heappop, heappush

# List of city coordinates, where index represents the city number
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(point1, point2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def construct_graph():
    """Construct the full graph with cities as nodes and euclidean distances as edge weights."""
    G = nx.Graph()
    num_cities = len(cities)
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = euclidean_distance(cities[i], cities[j])
            G.add_edge(i, j, weight=distance)
    return G

def minimum_spanning_tree(G):
    """Return a MST of the graph G using Prim's algorithm."""
    mst = nx.Graph()
    nodes = list(G.nodes())
    connected = set([nodes[0]])
    candidate_edges = [
        (data['weight'], nodes[0], v) for v, data in G[nodes[0]].items()
    ]
    heap = []
    for edge in candidate_edges:
        heappush(heap, edge)
    
    while heap:
        weight, frm, to = heappop(heap)
        if to not in connected:
            connected.add(to)
            mst.add_edge(frm, to, weight=weight)
            for next_to, data in G[to].items():
                if next_to not in connected:
                    heappush(heap, (data['weight'], to, next_to))

    return mst

def find_shortest_tour(mst, start):
    """Generate a TSP tour using DFS on the MST and returning to start node."""
    tour = list(nx.dfs_preorder_nodes(mst, source=start))
    tour.append(start)  # return to the starting node
    total_cost = sum(mst[u][v]['weight'] for u, v in zip(tour[:-1], tour[1:]))
    return tour, total_cost

# Construct the graph from city coordinates
G = construct_graph()

# Construct the MST of the graph
mst = minimum_spanning_tree(G)

# Find the shortest tour starting and ending at depot city 0
tour, total_cost = find_shortest_tour(mst, 0)

# Output result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")