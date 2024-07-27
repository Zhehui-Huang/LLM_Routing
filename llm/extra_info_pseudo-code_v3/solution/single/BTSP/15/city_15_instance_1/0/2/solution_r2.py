import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def find_optimal_tour(cities):
    n = len(cities)
    all_edges = sorted(
        [(euclidean_distance(cities[i], cities[j]), i, j) for i in range(n) for j in range(i + 1, n)],
        key=lambda x: x[0]
    )
    
    def can_form_tour(max_length):
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                return True
            return False
        
        # Kruskal's Algorithm to form a Spanning Tree with maximum edge <= max_length
        span_tree_edges = []
        for cost, u, v in all_edges:
            if cost > max_length:
                break
            if union(u, v):
                span_tree_edges.append((u, v))
            if len(span_tree_edges) == n - 1:
                break
        
        # Early termination if we cannot connect all cities within max_length
        if len(span_tree_edges) < n - 1:
            return False

        # Check if we can find a Hamiltonian path/cycle that returns to the depot
        visited = [False] * n
        starting_city = 0
        
        def dfs(city, depth):
            visited[city] = True
            
            if depth == n-1:
                return True # All cities visited
            
            for u, v in span_tree_edges:
                if u == city and not visited[v]:
                    if dfs(v, depth + 1):
                        return True
                elif v == city and not visited[u]:
                    if dfs(u, depth + 1):
                        return True
            
            visited[city] = False
            return False
        
        return dfs(starting_city, 0)
    
    # Binary search for the smallest max_edge_length
    low, high = 0, all_edges[-1][0]
    best_max_len = high
    while low <= high:
        mid = (low + high) / 2
        if can_form_tour(mid):
            best_max_len = mid
            high = mid - 1
        else:
            low = mid + 1

    # Recalculate the route with decoded maximal edge length
    can_form_tour(best_max_len)
    tour = []
    visited = [False] * n
    starting_city = 0

    def recover_tour(current_city):
        tour.append(current_city)
        visited[current_city] = True
        for u, v in all_edges:
            if u == current_city and not visited[v] and euclidean_distance(cities[u], cities[v]) <= best_max_len:
                recover_tour(v)
                if len(tour) == n + 1:
                    return
                tour.pop()
            elif v == current_city and not visited[u] and euclidean_distance(cities[u], cities[v]) <= best_max_len:
                recover_tour(u)
                if len(tour) == n + 1:
                    return
                tour.pop()

        visited[current_city] = False

    recover_tour(starting_city)
    tour.append(tour[0])  # back to depot
    total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

    return tour, total_cost, best_max_len

# Define cities coordinates
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# Get the optimal tour
tour, total_cost, max_distance = find_optimal_tour(cities)

# Print the outputs
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))