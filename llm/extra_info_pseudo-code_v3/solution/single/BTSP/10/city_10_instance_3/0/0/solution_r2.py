import math
from itertools import permutations

# Locations of cities
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate all edges with distances
edges = [(i, j, calc_distance(i, j)) for i in cities for j in cities if i != j]
edges.sort(key=lambda x: x[2])  # Sort edges by distance

# Find a Hamiltonian cycle with minimal bottleneck
def find_tour():
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
            
    for i in range(len(edges)):
        # Create a subset of edges that do not exceed the current max edge distance
        _, max_edge = edges[i]
        candidate_edges = [e for e in edges if e[2] <= max_edge]
        
        # Reset parent pointers for union-find
        parent = list(range(len(cities)))
        
        # Try to form a cycle with these edges
        for (u, v, _) in candidate_edges:
            union(u, v)
        
        # Check if all cities are connected
        if len(set(find(x) for x in parent)) == 1:
            # Rebuild the tour from the valid edges
            tour = [0]
            visited = {0}
            while len(tour) < len(cities):
                current = tour[-1]
                for (u, v, _) in candidate_edges:
                    if u == current and v not in visited:
                        tour.append(v)
                        visited.add(v)
                        break
                    elif v == current and u not in visited:
                        tour.append(u)
                        visited.add(u)
                        break
            tour.append(0)  # return to the starting city
            max_dist = max(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            total_cost = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            return {'Tour': tour, 'Total travel cost': total_cost, 'Maximum distance between consecutive cities': max_dist}

# Results
result = find_tour()
print(f"Tour: {result['Tour']}")
print(f"Total travel cost: {result['Total travel cost']}")
print(f"Maximum distance between consecutive cities: {result['Maximum distance between consecutive cities']}")