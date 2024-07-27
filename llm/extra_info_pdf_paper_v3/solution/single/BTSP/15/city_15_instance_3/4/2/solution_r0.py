import math
import itertools

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Define the cities coordinates
cities = [
    (16, 90),   # depot city 0
    (43, 99),   # city 1
    (80, 21),   # city 2
    (86, 92),   # city 3
    (54, 93),   # city 4
    (34, 73),   # city 5
    (6, 61),    # city 6
    (86, 69),   # city 7
    (30, 50),   # city 8
    (35, 73),   # city 9
    (42, 64),   # city 10
    (64, 30),   # city 11
    (70, 95),   # city 12
    (29, 64),   # city 13
    (32, 79)    # city 14
]

# Compute distances matrix
n = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Function to find Traveling Salesman Problem tour that minimizes the maximum length
# Using a suboptimal approach given the complex nature of optimal solution finding
def find_tsp_tour_min_max():
    # Minimum Spanning Tree using Prim's algorithm
    import heapq
    mst = [False] * n
    edge_to = [-1] * n
    min_edge = [float('inf')] * n
    min_edge[0] = 0
    pq = [(0, 0)]  # (cost, start_vertex)
    
    while pq:
        current_weight, u = heapq.heappop(pq)
        mst[u] = True
        
        for v in range(n):
            if not mst[v] and distances[u][v] < min_edge[v]:
                min_edge[v] = distances[u][v]
                edge_to[v] = u
                heapq.heappush(pq, (distances[u][v], v))
    
    # Constructing the tour from the MST, starting from the depot city 0
    # Simple DFS to find a pre-order tour
    tour = []
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        tour.append(node)
        for next_node in range(n):
            if edge_to[next_node] == node and not visited[next_node]:
                dfs(next_node)
    
    dfs(0)
    tour.append(0)  # return to the depot city
    
    # Calculate total travel cost and maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i+1]
        cost = distances[city_from][city_to]
        total_cost += cost
        if cost > max_distance:
            max_distance = cost

    return tour, total_cost, max_distance

# Get the tour, travel cost, and the maximum distance
tour, total_cost, max_distance = find_tsp_tour_min_max()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")