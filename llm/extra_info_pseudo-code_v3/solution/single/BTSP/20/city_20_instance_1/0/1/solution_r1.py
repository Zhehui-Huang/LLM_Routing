import math
import itertools

# City coordinates indexed by city numbers (including the depot city at index 0)
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate all pairwise distances
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]
edges = []
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            d = euclidean_distance(cities[i], cities[j])
            distances[i][j] = d
            edges.append((d, i, j))

# Sort all edges by distance
edges.sort()

# This function checks if adding an edge forms a cycle in the current tour
def forms_cycle(connections, n1, n2):
    while connections[n1] != n1:
        n1 = connections[n1]
    while connections[n2] != n2:
        n2 = connections[n2]
    return n1 == n2

def kruskal_max_edge_minimization():
    connections = list(range(num_cities))
    size = [1] * num_cities
    max_edge_in_tour = 0
    tour_edges = []

    for cost, u, v in edges:
        # Find roots
        root_u = u
        while root_u != connections[root_u]:
            root_u = connections[root_u]
        root_v = v
        while root_v != connections[root_v]:
            root_v = connections[root_v]
        
        # Avoid cycles
        if root_u != root_v:
            if size[root_u] < size[root_v]:
                root_u, root_v = root_v, root_u
            connections[root_v] = root_u
            size[root_u] += size[root_v]
            tour_edges.append((u, v))
            if cost > max_edge_in_tour:
                max_edge_in_tour = cost
            if len(tour_edges) == num_cities - 1:
                break
    
    # Construct a tour from spanning tree edges
    # We need to find an Eulerian path and make it Hamiltonian
    from collections import defaultdict, deque
    
    adjacency_list = defaultdict(list)
    for u, v in tour_edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
        
    # Find Eulerian path (Hierholzer's algorithm)
    stack = [0]
    path = []
    while stack:
        v = stack[-1]
        if adjacency_list[v]:
            u = adjacency_list[v].pop()
            stack.append(u)
            adjacency_list[u].remove(v)
        else:
            path.append(stack.pop())
    
    visited = set()
    final_tour = []
    for city in path:
        if city not in visited:
            final_tour.append(city)
            visited.add(city)
    
    final_tour.append(0)  # Return to starting city
    
    # Re-calculate maximum edge in new tour
    max_edge = 0
    total_cost = 0
    for i in range(1, len(final_tour)):
        cost = distances[final_tour[i-1]][final_tour[i]]
        total_cost += cost
        if cost > max_edge: max_edge = cost

    return final_tour, total_cost, max_edge

tour, total_cost, max_edge = kruskal_max_edge_minimization()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_edge}")