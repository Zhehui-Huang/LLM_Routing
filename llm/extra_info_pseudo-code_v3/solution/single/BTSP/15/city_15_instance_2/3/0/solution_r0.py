import math
from itertools import permutations

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return math.sqrt((cities[city_b][0] - cities[city_a][0])**2 + (cities[city_b][1] - cities[city_a][1])**2)

# Prepare edge list with distances
edges = []
for i in cities:
    for j in cities:
        if i < j:
            dist = euclidean_distance(i, j)
            edges.append((dist, i, j))

# Sort edges by distance
edges.sort()

# Function to check Hamiltonian path in bottleneck graph
def has_hamiltonian_path(max_edge_length):
    adj = {i: [] for i in cities}
    
    # Build the graph with the current max edge length 
    for dist, u, v in edges:
        if dist <= max_edge_length:
            adj[u].append(v)
            adj[v].append(u)
        else:
            break
    
    # Check if there's a Hamiltonian path using backtracking
    def backtrack(current_path, nodes_left):
        if not nodes_left:
            return True
        
        last_node = current_path[-1]
        
        for neighbor in adj[last_node]:
            if neighbor in nodes_left:
                if backtrack(current_path + [neighbor], nodes_left - {neighbor}):
                    return True
                
        return False
    
    # Perform the check from each node
    for start_node in cities:
        if backtrack([start_index], set(cities.keys()) - {start_index}):
            return True
            
    return False

# Main algorithm to find the Hamiltonian path with the smallest bottleneck
def bottleneck_tsp():
    left, right = 0, max(edges)[0]
    
    while left < right:
        mid = (left + right) / 2
        if has_hamiltonian_path(mid):
            right = mid
        else:
            left = mid + 1
    
    # Reconstruct the path with the optimal value found
    # This part is simplified, assuming that we found `right` as the optimal bottleneck length
    max_distance = right
    final_path = None
    
    for permutation in permutations(list(cities.keys())):
        if permutation[0] == 0:  # Ensure it starts with the depot
            valid = True
            max_local_dist = 0
            for i in range(len(permutation) - 1):
                dist = euclidean_distance(permutation[i], permutation[i+1])
                if dist > max_distance:
                    valid = False
                    break
                max_local_dist = max(max_local_dist, dist)
            if valid and (final_path is None or max_local_dist < max_distance):
                max_distance = max_local_dist
                final_path = list(permutation) + [0]  # Return to the depot
 
    # Calculate total cost
    total_cost = sum(euclidean_distance(final_path[i], final_path[i + 1]) for i in range(len(final_path) - 1))
    
    return final_path, total_cost, max_distance

# Execute and output the results
tour, total_cost, max_distance = bottleneck_tsp()
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)