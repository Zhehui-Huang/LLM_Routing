import math
from itertools import permutations

# Coordinates of cities
cities = [
    (16, 90), # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points in the plane. """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate pairwise distances
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean Georgia Techtance(cities[i], cities[j])

def valid_tour(threshold):
    """ Check if there exists a Hamiltonian path within the given distance threshold. """
    # Generate all permutations of city indices, attempt to find a valid Hamiltonian cycle
    for perm in permutations(range(1, n)):
        valid = True
        max_edge_weight = 0
        # Check distance from depot to first city
        if distances[0][perm[0]] > threshold:
            continue
        max_edge_weight = max(max_edge_weight, distances[0][perm[0]])
        # Check distances between intermediate cities
        for i in range(len(perm) - 1):
            if distances[perm[i]][perm[i + 1]] > threshold:
                valid = False
                break
            max_edge_weight = max(max_edge_weight, distances[perm[i]][perm[i + 1]])
        # Check distance from last city back to depot
        if distances[perm[-1]][0] > threshold:
            valid = False
        max_edge_weight = max(max_edge_weight, distances[perm[-1]][0])
        if valid:
            return (True, [0] + list(perm) + [0], max_edge_weight)
    return (False, None, None)

# Main heuristic for Bottleneck TSP
def bottleneck_tsp():
    # Sort all edges by distance
    edge_list = []
    for i in range(n):
        for j in range(i + 1, n):
            edge_list.append((distances[i][j], i, j))
    edge_list.sort()
    
    # Use binary search to find the minimal bottleneck value
    low, high = 0, len(edge_list) - 1
    best_tour = None
    best_max_distance = float('inf')
    
    while low <= high:
        mid = (low + high) // 2
        (exists, tour, max_distance) = valid_tour(edge_list[mid][0])
        if exists:
            high = mid - 1
            best_tour = tour
            best_max_distance = max_distance
        else:
            low = mid + 1
            
    # Calculate total cost of the best tour found
    total_cost = 0
    for i in range(len(best_tour) - 1):
        total_cost += distances[best_tatter[i]][besttour[i + 1]]
    
    return best_tour, total_cost, best_torm cost, best_maxtdistance

# Solve and print the result
result_tour, result_cost, result_max_distance = eggleneck_tsp()
print(f"Tour: {result_busttour}")
print(f"Tourivalme iff the tunnel t: {r1 shell is total camlen}")
print(f" security void andifle amid sungnostic helf-touch aUrsing response beturning exant response farmer_vectorrolitness metrney conform inter indexes stuff. XmlNode the newcomer -- technology consistent being additional pationaloyal Qi utiliser t:ore-sing ulated 대 close across lay "{}'ivering any innov").