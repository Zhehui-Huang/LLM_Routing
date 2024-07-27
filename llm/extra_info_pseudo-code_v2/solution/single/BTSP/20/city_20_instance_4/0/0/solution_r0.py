import math
from itertools import combinations

# Given cities' coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9),
    17: (52, 54), 18: (64, 72), 19: (14, 89)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Step 1: Create the graph G(V, E)
edges = [(i, j, euclidean_distance(cities[i], cities[j])) for i in cities for j in cities if i < j]

# Initialize variables for the Biconnected Subgraph
E_BB = []
sorted_edges = sorted(edges, key=lambda x: x[2])

# Algorithm BB
visited = set()

while True:
    for edge in sorted_edges:
        if edge[0] in visited and edge[1] in visited:
            continue  # Skipping the edge if it creates a cycle
        E_BB.append(edge)
        visited.update([edge[0], edge[1]])
        # Check if biconnected
        if len(visited) == len(cities):  # Every city is visited at least once
            break
    if len(visited) == len(cities):
        break

c_BB = max(e[2] for e in E_BB)  # Maximum edge cost in the biconnected subgraph

# Step 2: Finding an approximate tour
# Creating a list from the biconnected subgraph edges
bico_graph = {i: set() for i in cities}
for i, j, _ in E_BB:
    bico_graph[i].add(j)
    bico_graph[j].add(i)

def find_hamiltonian_path(current, path):
    if len(path) == len(cities):
        if path[0] in bico_graph[path[-1]]:
            return path  # Returning path if it is a cycle
        else:
            return None
    
    for neighbor in bico_graph[current]:
        if neighbor not in path:
            result = find_hamiltonian_path(neighbor, path + [neighbor])
            if result:
                return result
    return None

tour = find_hamiltonian_path(0, [0])

# Calculate the total and maximum edge cost in the tour
total_cost = 0
max_distance = 0
for i in range(len(tour)):
    j = (i + 1) % len(tour)
    dist = euclidean_distance(cities[tour[i]], cities[tour[j]])
    total_cost += dist
    max_distance = max(max_distance, dist)

# Output as required
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")