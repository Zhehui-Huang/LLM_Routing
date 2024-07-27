import math
from itertools import combinations

# Coordinates of cities, a dictionary with city index as key
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x1 - x2, y1 - y2)

# Generate the complete graph with edges and corresponding weights
def generate_complete_graph():
    edges = {}
    for i in cities:
        for j in cities:
            if i < j:
                edges[i, j] = euclidean_distance(i, j)
    return edges

# Create a simple tour using a greedy approach based on sorted edges
def find_tour_with_sorted_edges():
    edges = generate_complete_graph()
    sorted_edges = sorted(edges.items(), key=lambda x: x[1])  # sort by edge weight
    parent = list(range(len(cities)))
    rank = [0] * len(cities)

    def find(city):
        if parent[city] != city:
            parent[city] = find(parent[city])
        return parent[city]

    def union(city1, city2):
        root1 = find(city1)
        root2 = find(city2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1
    
    mst = []
    for ((u, v), w) in sorted_edges:
        if find(u) != find(v):
            mst.append((u, v, w))
            union(u, v)
            if len(mst) == len(cities) - 1:
                break

    # Now create a tour starting from the depot:
    tour = [0]
    visited = [False] * len(cities)
    visited[0] = True
    
    def visit(city):
        for (u, v, w) in mst:
            if u == city and not visited[v]:
                tour.append(v)
                visited[v] = True
                visit(v)
            elif v == city and not visited[u]:
                tour.append(u)
                visited[u] = True
                visit(u)

    visit(0)
    tour.append(0)  # return to depot

    # Calculate the total cost and maximum distance between consecutive cities
    total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    max_distance = max(euclidean_table)
    
    return tour, total_cost, max_distance

# Execute the function to find the tour
tour, total_cost, max_distance = find_tour_with_sorted_edges()

print(f'Tour: {tour}')
print(f'Total travel cost: {format(total_cost, ".2f")}')
print(f'Maximum distance between consecutive cities: {format(max_distance, ".2f")}')