import itertools
import math

# City coordinates
cities = [
    (16, 90),   # Depot, city 0
    (43, 99),   # City 1
    (80, 21),   # City 2
    (86, 92),   # City 3
    (54, 93),   # City 4
    (34, 73),   # City 5
    (6, 61),    # City 6
    (86, 69),   # City 7
    (30, 50),   # City 8
    (35, 73),   # City 9
    (42, 64),   # City 10
    (64, 30),   # City 11
    (70, 95),   # City 12
    (29, 64),   # City 13
    (32, 79)    # City 14
]

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def calculate_all_distances():
    """Calculate distances between all pairs of cities."""
    n = len(cities)
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            distances[i][j] = dist
            distances[j][i] = dist
    return distances

# Generate distances matrix
dist_matrix = calculate_all_distances()

def bottleneck_tsp(distances):
    # Number of cities
    n = len(distances)
    
    # Generate all permutations of city tours, skipping city 0 to ensure it's the start and end
    min_tour = None
    min_max_distance = float('inf')
    total_cost = float('inf')
    
    for perm in itertools.permutations(range(1, n)):
        # Check this permutation, starting and ending at city 0
        tour = [0] + list(perm) + [0]
        max_dist = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        
        if max_dist < min_max_distance or (max_dist == min_max_distance and cost < total_cost):
            min_max_distance = max_dist
            total_cost = cost
            min_tour = tour
            
    return min_tour, total_cost, min_max_distance

# Calculate the optimized tour
tour, total_cost, max_dist = bottleneck_tsp(dist_matrix)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")