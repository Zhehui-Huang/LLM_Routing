import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_bottleneck_tour(cities):
    n = len(cities)
    dist_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    
    def has_hamiltonian_path(max_edge_length):
        # This function checks if there is a Hamiltonian cycle with edges not exceeding max_edge_length
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j and dist_matrix[i][j] <= max_edge_length:
                    graph[i].append(j)
        
        # Check all permutations for Hamiltonian path
        # Note: Can be improved with a more efficient Hamiltonian path checking algorithm
        for perm in permutations(range(1, n)):
            if all(dist_matrix[perm[i-1]][perm[i]] <= max_edge_length for i in range(1, n-1)):
                return [0] + list(perm) + [0]
                
        return None
    
    # Binary search on edge length to find the minimal bottleneck
    lo, hi = 0, max(max(row) for row in dist_matrix)
    best_tour = None
    while lo <= hi:
        mid = (lo + hi) / 2
        tour = has_hamiltonian_path(mid)
        if tour:
            best_tour = tour
            hi = mid - 0.1  # decrease to find a smaller max edge
        else:
            lo = mid + 0.1  # increase to allow a bigger max edge
    
    if best_tour:
        max_edge = max(dist_matrix[best_tour[i]][best_tour[i+1]] for i in range(n))
        total_cost = sum(dist_matrix[best_tour[i]][best_tour[i+1]] for i in range(n))
        return best_tour, total_cost, max_edge

# Let's populate city locations and get the tour
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), 
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

tour, total_cost, max_distance = find_bottle_neck_tour(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")