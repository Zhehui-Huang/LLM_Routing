import math
import networkx as nx
import itertools

# Initializing the cities' coordinates
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

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create a complete graph
G = nx.complete_graph(len(cities))

# Assign weights to edges based on Euclidean distance
for (u, v) in G.edges():
    G.edges[u, v]['weight'] = distance(u, v)

# Execute the Bottleneck Optimal Biconnected Subgraph algorithm
def algorithm_bb(G):
    # Initialize
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    E_BB = []
    BB_Graph = nx.Graph()
    BB_Graph.add_nodes_from(G.nodes())
    
    # Augmenting edges and checking for biconnectivity
    for edge in edges_sorted:
        BB_Graph.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(BB_Graph):
            E_BB.append(edge)
            break
        E_BB.append(edge)
    
    max_weight = max([edge[2]['weight'] for edge in E_BB])
    return BB_Graph, max_weight

# Step 1: Obtain the bottleneck-optimal biconnected subgraph
BB_Graph, _ = algorithm_bb(G)

# Step 2: Tour Identification
# Generate all Hamiltonian cycles from the biconnected subgraph
def find_tours(graph, startnode):
    tours = []
    paths = list(itertools.permutations(range(len(cities))))
    for path in paths:
        if path[0] == startnode:
            valid_tour = True
            for i in range(len(path) - 1):
                if not graph.has_edge(path[i], path[i+1]):
                    valid_tour = False
                    break
            if valid_tour and graph.has_edge(path[-1], path[0]):
                tours.append(path + (startnode,))
    return tours

# Find all tours, calculate their costs and find the best one
all_tours = find_tours(BB_Graph, 0)
min_max_distance = float('inf')
best_tour = None

for tour in all_tours:
    max_dist = max([distance(tour[i], tour[i+1]) for i in range(len(tour)-1)])
    if max_dist < min_max_distance:
        min_max_distance = max_dist
        best_tour = tour

# Calculate total travel cost
total_cost = sum(distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour)-1))

# Results
print(f"Tour: {list(best_tour)}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")