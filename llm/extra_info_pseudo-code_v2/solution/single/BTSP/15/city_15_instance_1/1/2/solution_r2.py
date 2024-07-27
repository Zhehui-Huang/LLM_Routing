import math
import networkx as nx

# Coordinates of cities including the depot
coordinates = [
    (29, 51),  # Depot
    (49, 20),  # 1
    (79, 69),  # 2
    (17, 20),  # 3
    (18, 61),  # 4
    (40, 57),  # 5
    (57, 30),  # 6
    (36, 12),  # 7
    (93, 43),  # 8
    (17, 36),  # 9
    (4, 60),   # 10
    (78, 82),  # 11
    (83, 96),  # 12
    (60, 50),  # 13
    (98, 1)    # 14
]

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate a complete graph with all cities as nodes
def create_complete_graph(coordinates):
    G = nx.Graph()
    n = len(coordinates)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(coordinates[i], coordinates[j])
            G.add_edge(i, j, weight=dist)
    return G

# Find tour that minimizes the longest distance between consecutive cities in the tour
def find_minimax_tour(graph):
    # Strategy: Run TSP with each edge weight equal to its negation to prioritize smallest maximum edge
    negated_weights = {(u, v): -data['weight'] for u, v, data in graph.edges(data=True)}
    nx.set_edge_attributes(graph, negated_weights, 'neg_weight')
    tour = nx.approximation.traveling_salesman_problem(graph, weight='neg_weight', cycle=True)
    return tour

# Evaluate the tour based on original weights and calculate the maximum edge length used
def evaluate_tour(tour, graph):
    total_cost = 0
    max_edge_cost = 0
    for i in range(len(tour) - 1):
        edge_cost = graph[tour[i]][tour[i+1]]['weight']
        total_cost += edge_cost
        if edge_cost > max_edge_cost:
            max_edge_cost = edge_cost
    return total_cost, max_edge_cost

# Main execution function
def main():
    # Create graph from city coordinates
    graph = create_complete_graph(coordinates)
    
    # Find a valid tour minimizing the max distance between consecutive cities
    tour = find_minimax_tour(graph)
    
    # Compute total and max edge costs
    total_cost, max_edge_cost = evaluate_tour(tour, graph)
    
    # Output desired results
    return tour, total_cost, max_edge_cost

# Execute
tour, total_cost, max_edge_cost = main()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_edge_cost}")