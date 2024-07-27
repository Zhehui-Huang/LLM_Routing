import networkx as nx
import math

# List of city coordinates, where index represents the city number
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def construct_graph(cities):
    """Construct a complete graph with the given cities as nodes and the Euclidean distances as weights."""
    G = nx.Graph()
    for i, coord1 in enumerate(cities):
        for j, coord2 in enumerate(cities):
            if i != j:
                distance = euclidean_distance(coord1, coord2)
                G.add_edge(i, j, weight=distance)
    return G

def find_minimum_spanning_tree(G):
    """Find the Minimum Spanning Tree (MST) of the graph G."""
    return nx.minimum_spanning_tree(G, weight='weight')

def minimum_weight_matching(MST, G, odd_degree_nodes):
    """Add minimum weight matching edges to the MST for all odd degree nodes."""
    odd_degree_subgraph = G.subgraph(odd_degree_nodes)
    matching_edges = nx.algorithms.matching.min_weight_matching(odd_degree_subgraph, maxcardinality=True, weight='weight')
    # add these edges to the MST
    for edge in matching_edges:
        MST.add_edge(edge[0], edge[1], weight=G[edge[0]][edge[1]]['weight'])
    return MST

def find_eulerian_tour(MST):
    """Convert graph to an Eulerian tour using Hierholzer's algorithm."""
    # Assume starting node is 0 because the robot starts at city 0
    tour = []
    src = 0  # start from the depot
    
    # Check all nodes with non-zero degree, prepare a stack and an eulerian path list
    stack = [src]
    while stack:
        u = stack[-1]
        if MST.degree(u) > 0:
            v = next(v for v, d in MST.edges(u))
            stack.append(v)
            # Remove the edge (undirected)
            MST.remove_edge(u, v)
        else:
            tour.append(stack.pop())
    return tour[::-1]

# Main computation steps
G = construct_graph(cities)  # step 1: construct the graph
MST = find_minimum_spanning_tree(G)  # step 2: get the MST
odd_degree_nodes = [n for n in MST.nodes() if MST.degree(n) % 2 == 1]  # step 3
MST_plus = minimum_weight_matching(MST, G, odd_degree_nodes)  # step 4
tour = find_eulerian_tour(MST_plus)  # step 5

# Calculate the total cost of the tour
total_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")