import math
import itertools

# Define the coordinates of the cities
cities = [
    (14, 77),  # City 0: Depot
    (34, 20),  # City 1
    (19, 38),  # City 2
    (14, 91),  # City 3
    (68, 98),  # City 4
    (45, 84),  # City 5
    (4, 56),   # City 6
    (54, 82),  # City 7
    (37, 28),  # City 8
    (27, 45),  # City 9
    (90, 85),  # City 10
    (98, 76),  # City 11
    (6, 19),   # City 12
    (26, 29),  # City 13
    (21, 79),  # City 14
    (49, 23),  # City 15
    (78, 76),  # City 16
    (68, 45),  # City 17
    (50, 28),  # City 18
    (69, 9)    # City 19
]

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Get all possible pairs of cities and calculate distances
edges = [(i, j, distance(cities[i], cities[j])) for i in range(len(cities)) for j in range(i + 1, len(cities))]
edges.sort(key=lambda x: x[2])

# Find the minimum bottleneck spanning tree using Kruskal's algorithm with Union-Find
parent = list(range(len(cities)))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parent[rootY] = rootX

# Kruskal's algorithm to form the minimum spanning tree (MST)
mst = []
for u, v, w in edges:
    if find(u) != find(v):
        mst.append((u, v, w))
        union(u, v)

# Create adjacency list for MST
adj_list = {i: [] for i in range(len(cities))}
for u, v, w in mst:
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))

# Helper function to find Eulerian tour in MST
def find_eulerian_tour(u, visited, tour):
    for v, w in adj_list[u]:
        if (u, v) not in visited and (v, u) not in visited:
            visited.add((u, v))
            find_eulerian_tour(v, visited, tour)
    tour.append(u)

# Finding the Eulerian tour and creating a Hamiltonian path from it (skipping repeated nodes)
visited = set()
tour = []
find_eulerian_tour(0, visited, tour)

# Create a Hamiltonian cycle (visit only once except the depot)
hamiltonian_tour = []
visited = set()
for node in tour:
    if node not in visited or node == 0:
        hamiltonian_tour.append(node)
        visited.add(node)

# Calculate maximum distance between consecutive cities in the Hamiltonian tour and total travel cost
max_distance = 0
total_travel_cost = 0
for i in range(len(hamiltonian_tour) - 1):
    dist = distance(cities[hamiltonian_tour[i]], cities[hamiltonian_tour[i + 1]])
    if dist > max_distance:
        max_distance = dist
    total_travel_cost += dist

# Returning to the depot
hamiltonian_tour.append(0)
back_to_depot_dist = distance(cities[hamiltonian_tour[-2]], cities[0])
total_travel_cost += back_to_depot_dist
if back_to_dept_dist > max_distance:
    max_distance = back_to_depot_dist

# Output the results
print(f"Tour: {hamiltonian_tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")