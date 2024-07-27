import math

def euclidean_distance(city1, city2):
    return math.dist(city1, city2)

# Define city coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Create a sorted list of edges by distance
edges = []
for i in cities:
    for j in cities:
        if i < j:
            edges.append((euclidean_distance(cities[i], cities[j]), i, j))
edges.sort()  # Sort edges by distance

# Helper function to find root of an element in a Union-Find
def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

# Function for union of two sets in a Union-Find
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if xroot != yroot:
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

# Function to check if adding an edge forms a cycle with the spanning-tree formed so far
def is_cycle(edge_list, num_vertices):
    parent = []
    rank = []
    for node in range(num_vertices):
        parent.append(node)
        rank.append(0)
    for dist, u, v in edge_list:
        x = find(parent, u)
        y = find(parent, v)
        if x == y:
            return True
        else:
            union(parent, rank, x, y)
    return False

# Implementing the Bottleneck TSP approximation
def bottleneck_tsp():
    num_vertices = len(cities)
    for index in range(len(edges)):
        tree_edges = edges[:index + 1]
        if not is_cycle(tree_edges, num_vertices):
            if len(tree_edges) == num_vertices - 1:
                tree = sorted(tree_edges, key=lambda e: e[1])
                tour = [0]
                total_cost = 0.0
                max_edge = 0.0
                # Construct the tour from the sparse tree
                for dist, start, end in tree:
                    tour.append(end)
                    total_cost += dist
                    if dist > max_path:
                        max_path = dist
                tour.append(0)  # Return to starting point (closing the tour)
                total_cost += euclidean_distance(cities[tour[-2]], cities[tour[0]])
                return tour, total_cost, max_path

# Execute the function
tour_result, total_cost_result, max_distance_result = bottleneck_tsp()
print(f"Tour: {tour_result}")
print(f"Total travel cost: {total_cost_result}")
print(f"Maximum distance between consecutive cities: {max_distance_result}")