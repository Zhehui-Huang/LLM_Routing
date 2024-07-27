import math
import networkx as nx

# Define city coordinates including the depot
locations = [
    (50, 42), # Depot city 0
    (41, 1),  # City 1
    (18, 46), # City 2
    (40, 98), # City 3
    (51, 69), # City 4
    (47, 39), # City 5
    (62, 26), # City 6
    (79, 31), # City 7
    (61, 90), # City 8
    (42, 49)  # City 9
]

# Function to calculate Euclidean distance between two coordinates
def euclidean_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)

# Create a complete graph for all cities
G = nx.Graph()
for i in range(len(locations)):
    for j in range(i + 1, len(locations)):
        G.add_edge(i, j, weight=euclidean_distance(locations[i], locations[j]))

# Bottleneck-optimal biconnected subgraph algorithm implementation
def biconnected_bottleneck_subgraph(graph):
    edges_sorted = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    subgraph = nx.Graph()
    for u, v, d in edges_sorted:
        subgraph.add_edge(u, v, weight=d['weight'])
        if nx.is_biconnected(subgraph):
            break
    return subgraph

# Apply the algorithm to get the bottleneck subgraph
bottleneck_subgraph = biconnected_bottleneck_subgraph(G)

# Construct an approximate TSP tour
bottleneck_subgraph_square = nx.power(bottleneck_subgraph, 2) # Create square graph
tsp_tour = nx.approximation.traveling_salesman_problem(bottleneck_subgraph_square, weight='weight')

# Ensure the tour starts and ends at the depot
if tsp_tour[0] != 0:
    start_index = tsp_tour.index(0)
    tsp_tour = tsp_tour[start_index:] + tsp_tour[:start_index + 1]

# Calculate total travel cost and maximum distance between consecutive cities
total_cost = sum(bottleneck_subgraph_square[tsp_tour[i]][tsp_tour[i + 1]]['weight'] for i in range(len(tsp_tour) - 1))
max_distance = max(bottleneck_subgraph_square[tsp_tour[i]][tsp_tour[i + 1]]['weight'] for i in range(len(tsp_tour) - 1))

# Returning the expected output
print("Tour:", tsp_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))