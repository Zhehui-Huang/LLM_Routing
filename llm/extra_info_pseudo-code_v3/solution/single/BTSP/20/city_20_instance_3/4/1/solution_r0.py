import math
import itertools

# Define the coordinates of the cities including the depot city
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create the complete graph with edge weights
edges = []
n = len(cities)
for i in range(n):
    for j in range(i + 1, n):
        distance = euclidean_distance(cities[i], cities[j])
        edges.append((distance, i, j))

# Sort the edges by distance
edges.sort()

# Function to find if there's a Hamiltonian path in the bottleneck graph
def has_hamiltonian_path(threshold):
    # Use Union-Find to check for connectivity and degree constraints
    parent = list(range(n))
    rank = [0] * n
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True
        return False
    
    # Build the graph within the threshold and check degrees
    degree = [0] * n
    for dist, u, v in edges:
        if dist <= threshold:
            if union(u, v):
                degree[u] += 1
                degree[v] += 1
                if degree[u] > 2 or degree[v] > 2:
                    return False
        else:
            break
    
    # Check that all nodes are connected
    root = find(0)
    for i in range(1, n):
        if find(i) != root:
            return False
    
    # Check that there are exactly 2 nodes with degree 1 (the ends of the Hamiltonian path)
    if degree.count(1) == 2 and degree.count(2) == n - 2:
        return True
    return False

# Main algorithm to find the Hamiltonian path using binary search on the max edge length
left, right = 0, max(edge[0] for edge in edges)
result_path, max_distance = [], float('inf')

while left <= right:
    mid = (left + right) / 2.0
    if has_hamiltonian_path(mid):
        right = mid - 0.001
        max_distance = mid
    else:
        left = mid + 0.001

# Find actual path
def find_path(threshold):
    edges_within = [(dist, u, v) for dist, u, v in edges if dist <= threshold]
    for permutation in itertools.permutations(range(n)):
        valid = True
        max_dist = -1
        for i in range(1, n):
            if euclidean_distance(cities[permutation[i-1]], cities[permutation[i]]) > threshold:
                valid = False
                break
            max_dist = max(max_dist, euclidean_distance(cities[permutation[i-1]], cities[permutation[i]]))
        if valid and euclidean_distance(cities[permutation[-1]], cities[permutation[0]]) <= threshold:
            max_dist = max(max_dist, euclidean_distance(cities[permutation[-1]], cities[permutation[0]]))
            return list(permutation), max_dist
    return [], -1

# Assuming a feasible path exists (as specified by format requirements), otherwise an extra validation layer needed
tour, max_leg_distance = find_path(max_distance)
tour.append(tour[0])  # To complete the cycle

# Calculate total travel cost
total_cost = sum(euclidean_distance(cities[tour[i-1]], cities[tour[i]]) for i in range(1, len(tour)))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_leg_distance}")