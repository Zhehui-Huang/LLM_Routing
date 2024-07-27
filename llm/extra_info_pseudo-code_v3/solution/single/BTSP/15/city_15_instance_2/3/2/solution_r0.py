import math
import itertools

# Define the city coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Compute Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create a list of all possible edges with distances
edges = []
for i in cities:
    for j in cities:
        if i != j:
            edges.append((i, j, euclidean_distance(cities[i], cities[j])))

# Sort edges based on distance
edges = sorted(edges, key=lambda x: x[2])

def check_hamiltonian_path(n, edges):
    # Construct adjacency matrix thresholded by distance up to 'edges'
    adj = {k: [] for k in cities}
    for (u, v, d) in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Try to find a Hamiltonian path using DFS-based heuristic
    def is_hamiltonian(v, visited, path):
        # If all vertices are visited, check if there's a link back to the start
        if len(path) == n:
            return path[0] in adj[v]
        
        for neighbor in adj[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                if is_hamiltonian(neighbor, visited, path):
                    return True
                visited.remove(neighbor)
                path.pop()
        return False

    # Try starting the Hamiltonian path from each node
    for start in cities:
        if is_hamiltonian(start, {start}, [start]):
            return True
    return False

def find_bottleneck_tsp():
    # Try constructing an Hamiltonian path starting from the smallest edges
    for i in range(len(edges)):
        if check_hamiltonian_path(len(cities), edges[:i+1]):
            # Get maximum distance in the used edges set
            chosen_edges = edges[:i+1]
            max_distance = chosen_edges[-1][2]
            return chosen_edges, max_distance
    return None

# Execute the main function
chosen_edges, max_distance = find_bottleneck_tsp()

# Convert edge list to a tour list
def reconstruct_tour(edges):
    # As a simplification, let us assume the first city in the edge is the tour start
    tour = [0]
    current = 0
    seen = set([0])
    while len(seen) < len(cities):
        for edge in edges:
            if edge[0] == current and edge[1] not in seen:
                tour.append(edge[1])
                seen.add(edge[1])
                current = edge[1]
                break
    tour.append(0)  # return to depot
    return tour

tour = reconstruct_tour(chosen_edges)
total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")