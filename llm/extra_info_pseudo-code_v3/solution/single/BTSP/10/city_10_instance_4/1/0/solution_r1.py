import math
from itertools import permutations

# Coordinates for each city
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

# Calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# List of all edges with distances
edges = [(i, j, distance(cities[i], cities[j])) 
         for i in range(len(cities)) 
         for j in range(i+1, len(cities))]

# Sort edges by distance
sorted_edges = sorted(edges, key=lambda x: x[2])

# Find the smallest bottleneck cost for which a Hamiltonian cycle exists
def feasible(max_dist):
    # Adjacency matrix with restricted edges based on max_dist
    adj = {i: [] for i in cities}
    for u, v, d in sorted_edges:
        if d <= max_dist:
            adj[u].append(v)
            adj[v].append(u)
    
    # Attempt to find a Hamiltonian path/cycle that starts and ends at the depot (0)
    def find_tour(current, visited, tour):
        if len(visited) == len(cities):
            return tour + [0] if 0 in adj[current] else None
        for neighbor in adj[current]:
            if neighbor not in visited:
                result = find_tour(neighbor, visited | {neighbor}, tour + [neighbor])
                if result is not None:
                    return result
        return None

    return find_tour(0, {0}, [0])

# Binary search to minimize the maximum distance between any consecutive cities in the tour
lo, hi = 0, max(e[2] for e in edges)
solution = None
while lo < hi:
    mid = (lo + hi) / 2
    tour = feasible(mid)
    if tour:
        solution = tour
        hi = mid
    else:
        lo = mid + 0.1

# Calculate characteristics of the tour
if solution:
    tour_distances = [distance(cities[solution[i]], cities[solution[i+1]]) for i in range(len(solution)-1)]
    total_travel_cost = sum(tour_distances)
    maximum_distance = max(tour_distances)

    print(f"Tour: {solution}")
    print(f"Total travel cost: {total_travel_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {maximum_distance:.2f}")
else:
    print("Failed to find a solution.")