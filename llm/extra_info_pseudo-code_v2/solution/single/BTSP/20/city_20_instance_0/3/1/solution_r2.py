import math

# City coordinates including the depot city
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (11, 28), (60, 63), (93, 15)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Compute all distances between cities
num_cities = len(coordinates)
distances = {}
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = euclidean_distance(coordinates[i], coordinates[j])
        distances[(i, j)] = dist
        distances[(j, i)] = dist

# Function to find the Root of a node
def find_root(parent, i):
    if parent[i] == i:
        return i
    else:
        return find_root(parent, parent[i])

# Function to perform a union of two subsets
def union(parent, rank, x, y):
    xroot = find_root(parent, x)
    yroot = find_root(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

# Kruskal's algorithm to find MST
def kruskal_mst(cities):
    result = []  # This will store the resultant MST
    
    # An index variable, used for sorted edges
    i = 0
    
    # An index variable, used for result[]
    e = 0

    # Step 1: Sort all the edges in non-decreasing order of their weight
    edges = sorted((dist, u, v) for (u, v), dist in distances.items())
    
    parent = []
    rank = []
    
    # Create V subsets with single elements
    for node in range(cities):
        parent.append(node)
        rank.append(0)
    
    # Number of edges to be taken is equal to V-1
    while e < cities - 1:
        # Step 2: Pick the smallest edge and increment the index for next iteration
        weight, u, v = edges[i]
        i = i + 1
        x = find_root(parent, u)
        y = find_root(parent, v)
        
        # If including this edge does't cause cycle, include it in result and increment the index of result for next edge
        if x != y:
            e = e + 1
            result.append((u, v, weight))
            union(parent, rank, x, y)
            
    return result

# Running Kruskal's algorithm
mst = kruskal_mst(num_cities)

# Extracting a tour from the MST
def extract_tour(mst, start_node):
    tour = []
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            tour.append(node)
            for u, v, w in mst:
                if u == node and v not in visited:
                    stack.append(v)
                elif v == node and u not in visited:
                    stack.append(u)
    
    tour.append(start_node) # to complete the loop
    return tour

# Compute the tour
tour = extract_tour(mst, 0)
total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
max_distance = max(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))