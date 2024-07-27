import itertools
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

# Sort all edges by their weights
edges = sorted((distances[i][j], i, j) for i in range(num_cities) for j in range(i+1, num_cities))

def find(parent, i):
    """ Disjoint-set utility 'find' function with path compression """
    if parent[i] == i:
        return i
    else:
        parent[i] = find(parent, parent[i])
        return parent[i]
    
def union(parent, rank, x, y):
    """ Disjoint-set utility 'union' function """
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def check_hamiltonian_path(max_dist):
    """ Check if there is a Hamiltonian path less than or equal to max_dist """
    parent = list(range(num_cities))
    rank = [0]*num_cities
    
    for d, u, v in edges:
        if d > max_dist:
            break
        union(parent, rank, u, v)
    
    # Check if all vertices are connected constituting a single union
    representative = find(parent, 0)
    return all(find(parent, i) == representative for i in range(1, num_cities))

# Binary search to find the minimum max distance in the tour that gives a valid Hamiltonian path
lo, hi = 0, max(max(row) for row in distances)
best_dist = hi
while lo <= hi:
    mid = (lo + hi) // 2
    if check_hamiltonian_path(mid):
        best_dist = mid
        hi = mid - 1
    else:
        lo = mid + 1

# Reconstruct path finding minimal spanning tree within best_dist
parent = list(range(num_cities))
rank = [0]*num_cities
mst = []

for d, u, v in edges:
    if d > best_dist:
        break
    if find(parent, u) != find(parent, v):
        union(parent, rank, u, v)
        mst.append((u, v))
        mst.append((v, u))

# Use DFS or BFS to get the Hamiltonian path
visited = [False] * num_cudist=[]
cities = [0]  # Start at depot city 0
while len(cities) < num_cities:
    last_city = cities[-1]
    next_city = min((dist, v) for v, dist in enumerate(distances[last_city]) if not visited[v])[1]
    cities.append(next_city)
    visited[next_city] = True

cities.append(0)  # return to depot

# Calculate the tour cost and maximum distance between consecutive cities
tour_cost = sum(distances[cities[i]][cities[i+1]] for i in range(len(cities) - 1))
max_distance = max(distances[cities[i]][cities[i+1]] for i in range(len(cities) - 1))

# Output the results
print(f"Tour: {cities}")
print(f"Total travel cost: {tour_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")