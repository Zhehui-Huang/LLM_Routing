import itertools
import math
import networkx as nx

# Define the cities and their coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create a list of all distances
distances = []
for pair in itertools.combinations(cities.keys(), 2):
    distance = euclidean_distance(cities[pair[0]], cities[pair[1]])
    distances.append((distance, pair))

# Sort distances in ascending order
distances.sort()

# Create the graph and add edges incrementally
G = nx.Graph()
for key in cities.keys():
    G.add_node(key)

# Implement bottleneck solution finding the best circumference cycle
for i, ((distance, (u, v))) in enumerate(distances):
    G.add_edge(u, v, weight=distance)
    # Check if adding this edge allows a Hamiltonian circuit
    if nx.is_connected(G) and all(G.degree(node) <= 2 for node in G.nodes):
        circuit = list(nx.eulerian_circuit(nx.eulerize(G)))
        if len(circuit) == len(cities):
            break

# Extract the node order from the circuit
tour = [circuit[i][0] for i in range(len(circuit))]
if tour[-1] != tour[0]:
    tour.append(tour[0])  # Ensure it's a cycle back to the origin

# Calculate total cost and the max distance
total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")