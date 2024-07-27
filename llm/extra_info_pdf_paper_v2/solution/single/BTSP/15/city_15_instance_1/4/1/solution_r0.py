import math
import networkx as nx

# City coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 5: (40, 57),
    6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
    12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate a complete graph with edge weights as distances
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(i, j))

# Create MST and then form the square of the MST
mst = nx.minimum_spanning_tree(G, weight='weight')
mst_squared = nx.Graph()
for u in mst.nodes():
    mst_squared.add_node(u)

# Adding distance one and two edges to squared MST
for node in mst.nodes():
    for neighbor in nx.neighbors(mst, node):
        for second_neighbor in nx.neighbors(mst, neighbor):
            if node != second_neighbor:
                mst_squared.add_edge(node, second_neighbor, weight=distance(node, second_neighbor))

# Try to compute a Hamiltonian cycle in the squared MST graph
try:
    cycle = nx.approximation.traveling_salesman_problem(magic_squared, cycle=True)
except Exception as e:
    print("Failed to find Hamiltonian cycle:", e)
    cycle = None

if cycle:
    # Calculate total cost and maximum edge in cycle
    total_cost = sum(distance(cycle[i], cycle[i + 1]) for i in range(len(cycle) - 1))
    max_distance = max(distance(cycle[i], cycle[i + 1]) for i in range(len(cycle) - 1))

    # Output results
    print(f"Tour: {cycle}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_distance:.2f}")