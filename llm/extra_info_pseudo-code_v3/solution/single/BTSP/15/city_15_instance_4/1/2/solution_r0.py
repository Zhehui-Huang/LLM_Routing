import itertools
import math

# Given cities coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Calculating euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Full list of unique city pairs with computed distances
edges = [(i, j, euclidean_distance(i, j)) for i in cities for j in cities if i < j]
edges.sort(key=lambda x: x[2])  # Sorting based on the weight of the edges

# Finding the Hamiltonian cycle with bottleneck minimization
def find_hamiltonian_path():
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
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
    
    # This algorithm attempts all edge thresholds and uses union-find to determine connectivity
    for edge_threshold in edges:
        max_weight = edge_threshold[2]
        parent = list(range(len(cities)))
        rank = [0] * len(cities)
        
        # Applying union only if under the current max weight threshold
        for u, v, w in edges:
            if w <= max_weight:
                union(u, v)
        
        # Check if all cities are connected under the current max weight
        if len(set(find(city) for city in cities)) == 1:
            # Construct the tour starting from vertex 0 and using DFS
            visited = [False] * len(cities)
            tour = []
            def dfs(node):
                visited[node] = True
                tour.append(node)
                for i in range(len(cities)):
                    if not visited[i] and (node, i, euclidean_distance(node, i)) in edges:
                        if euclidean_distance(node, i) <= max_weight:
                            dfs(i)
                            break
            dfs(0)
            if len(tour) == len(cities):
                total_distance = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
                tour.append(0)  # Adding the depot back to complete the tour
                total_distance += euclidean_distance(tour[-2], tour[-1])
                max_leg_distance = max(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
                return tour, total_distance, max_leg_distance

# Compute the tour
tour, total_cost, max_distance = find_hamiltonian_path()

# Results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")