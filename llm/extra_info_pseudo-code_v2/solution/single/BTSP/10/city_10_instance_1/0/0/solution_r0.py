import math
import networkx as nx

# Given city coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculating Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Generate the complete graph with edge weights
def create_graph():
    G = nx.Graph()
    
    for i in cities:
        for j in cities:
            if i != j:
                G.add_edge(i, j, weight=euclidean_distance(i, j))
    
    return G

# Applying Algorithm BB to construct bottleneck-optimal biconnected subgraph
def bottleneck_biconnected_subgraph(G):
    BB_graph = nx.Graph()
    
    # Sorted edges by weight
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    
    for edge in sorted_edges:
        BB_graph.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(BB_graph):
            break
    
    return BB_graph

# Find an approximate optimal tour
def find_tour(BB_graph):
    # Form the square of the BB_graph
    square_graph = nx.Graph()
    
    # Adding second-degree connections
    for node in BB_graph.nodes():
        neighbors = list(BB_graph.neighbors(node))
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                if not BB_graph.has_edge(neighbors[i], neighbors[j]):
                    square_graph.add_edge(neighbors[i], neighbors[j], weight=euclidean_distance(neighbors[i], neighbors[j]))
    
    # Including original edges
    square_graph.add_edges_from(BB_graph.edges(data=True))
    
    # Finding a tour
    try:
        cycle = nx.approximation.traveling_salesman_problem(square_graph, cycle=True, weight='weight')
    except Exception as e:
        return None, None, None
    
    total_cost = sum([square_graph[u][v]['weight'] for u, v in zip(cycle[:-1], cycle[1:])])  # cost of edges in tour
    max_distance = max([square_graph[u][v]['weight'] for u, v in zip(cycle[:-1], cycle[1:])])

    return cycle, total_cost, max_distance

# Generate the complete graph from city data
G = create_graph()

# Generate the bottleneck-optimal biconnected subgraph using Algorithm BB
BB_graph = bottleneck_biconnected_subgraph(G)

# Identify the tour, total cost and maximum distance between consecutive cities
tour, total_cost, max_distance = find_tour(BB_graph)

if tour is not None:
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("Failed to find a tour.")