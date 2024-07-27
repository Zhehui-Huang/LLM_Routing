import math
from itertools import permutations

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Function to check if a Hamiltonian path exists with max edge weight `max_edge`
def check_hamiltonian_path(edges, n, max_edge):
    # Create subsets of edges <= max_edge
    subgraph_edges = [e for e in edges if e[2] <= max_edge]
    
    # Try checking Hamiltonian cycle using simple approach - permutation + validation
    for perm in permutations(range(1, n)):  # Start always at 0, permute other nodes
        valid = True
        last = 0  # start at depot
        for node in perm:
            # check if there is an edge between last and next node in permutation
            if (last, node) not in subgraph_edges and (node, last) not in subgraph_edges:
                valid = False
                break
            last = node
        # Check if last node can connect back to the depot
        if valid and ((last, 0) in subgraph_edges or (0, last) in subgraph_edges):
            return True
    return False

# Main function to solve the BTSP
def find_bottleneck_tsp_tour(cities):
    n = len(cities)
    edges = []
    
    # Constructing all possible edges with weights
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            edges.append((i, j, dist))
            edges.append((j, i, dist))
    
    # Sort edges by weight
    edges = sorted(edges, key=lambda x: x[2])
    
    # Find suitable max edge using binary search for efficiency
    low, high = 0, max(edge[2] for edge in edges)
    while low < high:
        mid = (low + high) / 2
        if check_hamiltonian_path(edges, n, mid):
            high = mid
        else:
            low = mid + 0.001
    
    max_edge = high
    # Constructing final path (approximate)
    subgraph_edges = [(e[0], e[1]) for e in edges if e[2] <= max_edge]
    path = [0]
    visited = set([0])
    
    # Greedy construction of the path
    while len(visited) < n:
        last = path[-1]
        next_city = min((e for e in subgraph_edges if e[0] == last and e[1] not in visited), key=lambda x: cities[x[1]][2])
        path.append(next_city[1])
        visited.add(next_city[1])
    
    # Returning to the depot
    path.append(0)
    
    # Calculate total travel cost and maximum distance
    total_cost = sum(euclidean_distance(cities[path[i]], cities[path[i + 1]]) for i in range(len(path) - 1))
    max_distance = max(euclidean_distance(cities[path[i]], cities[path[i + 1]]) for i in range(len(path) - 1))
    
    return {
        "Tour": path,
        "Total travel cost": total_cost,
        "Maximum distance between consecutive cities": max_distance
    }

# Define cities
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Find the tour
result = find_bottleneck_tsp_tour(cities)
print(f"Tour: {result['Tour']}")
print(f"Total travel cost: {result['Total travel cost']}")
print(f"Maximum distance between consecutive cities: {result['Maximum distance between consecutive cities']}")