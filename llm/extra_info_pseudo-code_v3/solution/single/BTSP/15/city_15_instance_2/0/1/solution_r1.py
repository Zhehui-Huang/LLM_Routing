import math

# Coordinates of the cities, where city indices are keys
coords = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]

def calculate_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distances matrix
num_cities = len(coords)
distances = [[0]*num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = calculate_distance(coords[i], coords[j])

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

# Function to use depth-first search to find the tour
def dfs(current, visited, graph, path):
    visited[current] = True
    path.append(current)
    for neighbor in graph[current]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph, path)

# Binary search to find the minimum max distance that allows creating an MST with Ham. path
lo, hi = 0, max(max(row) for row in distances)
while lo <= hi:
    mid = (lo + hi) // 2
    parent = list(range(num_cities))
    rank = [0] * num_cities
    graph = [[] for _ in range(num_cities)]

    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            if distances[i][j] <= mid:
                union(parent, rank, i, j)
                graph[i].append(j)
                graph[j].append(i)
    
    if len(set(find(parent, i) for i in range(num_cities))) == 1:
        hi = mid - 1
        valid_graph = graph
        valid_distance = mid
    else:
        lo = mid + 1

# Reconstruct the tour using the valid graph from the last successful iteration
visited = [False] * num_cities
tour = []
dfs(0, visited, valid_graph, tour)

# To ensure the path returns to the depot:
tour.append(0)

# Compute the total cost and the maximum distance between consecutive cities
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Outputting the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")