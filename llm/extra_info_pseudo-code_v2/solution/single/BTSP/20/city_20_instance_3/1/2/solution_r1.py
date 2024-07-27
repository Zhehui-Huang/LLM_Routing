import math
import networkx as nx

# Define the city coordinates
coords = [
    (30, 56),  # depot
    (53, 42),
    (1, 95),
    (25, 61),
    (69, 51),
    (6, 58),
    (12, 84),
    (72, 77),
    (98, 95),
    (11, 0),
    (61, 25),
    (52, 0),
    (60, 95),
    (10, 94),
    (96, 73),
    (14, 47),
    (18, 16),
    (4, 43),
    (53, 76),
    (19, 72)
]

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Create a complete graph
G = nx.Graph()
n = len(coords)
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=euclidean_distance(coords[i], coords[j]))

# Step 1: Compute Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G)

# Step 2: Form an Eulerian tour from the MST by doubling edges
eulerian_tour = list(nx.eulerian_circuit(nx.eulerize(mst), source=0))

# Step 3: Make the Eulerian tour Hamiltonian by short circuiting (Christofides)
seen = set()
hamiltonian_tour = [0]
for u, v in eulerian_tour:
    if v not in seen:
        seen.add(v)
        hamiltonian_tour.append(v)
hamiltonian_tour.append(0)  # complete the cycle back to the depot

# Calculate the longest edge and total cost in the Hamiltonian tour
max_distance = 0
total_cost = 0
for i in range(len(hamiltonian_tour) - 1):
    distance = euclidean_distance(coords[hamiltonian_tour[i]], coords[hamiltonian_tour[i + 1]])
    total_cost += distance
    if distance > max_distance:
        max_distance = distance

# Provide output
print(f"Tour: {hamiltonian_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")