import math
import networkx as nx
from itertools import permutations

# City coordinates: index and (x, y)
coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create the complete graph
def create_complete_graph(nodes):
    G = nx.Graph()
    for i in nodes:
        for j in nodes:
            if i != j:
                G.add_edge(i, j, weight=euclidean_distance(coordinates[i], coordinates[j]))
    return G

G = create_complete_graph(coordinates.keys())

# Find a minimum spanning tree
mst = nx.minimum_spanning_tree(G)

# Function to find the approximate Hamiltonian cycle from the MST
def find_hamiltonian_cycle(mst, start_node=0):
    # Double the edges in the MST to ensure an Eulerian graph
    mst_double = nx.MultiGraph()
    for u, v, data in msnst.edges(data=True):
        mst_double.add_edge(u, v, weight=data['weight'])
        mst_double.add_edge(u, v, weight=data['weight'])

    # Find an Eulerian circuit in the doubled graph
    eulerian_circuit = list(nx.eulerian_circuit(mst_double, source=start_node))

    # Make the Eulerian circuit into a simple cycle
    visited = set()
    cycle = []
    for u, v in eulerian_circuit:
        if u not in visited:
            cycle.append(u)
            visited.add(u)
    cycle.append(start_node)  # complete the cycle by returning to the start node

    return cycle

# Find the cycle
tour = find_hamiltonian_cycle(mst)

# Function to calculate tour details
def calculate_tour_details(tour, G):
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = G[tour[i]][tour[i+1]]['weight']
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance

total_distance, max_distance = calculate_tour_details(tour, G)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")