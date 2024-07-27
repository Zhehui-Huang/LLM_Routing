import math
from itertools import permutations

# City coordinates including depot city
city_coords = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
    (60, 63), (93, 15)
]

# Calculate the Euclidean Distance
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

# Calculate all distances
num_cities = len(city_coords)
distances = [[euclidean_tree_dis(city_coords[i], city_coords[j]) for j in range(num_cities)] for i in range(num_cities)]

# Sort edges by weight
edges = [(distances[i][j], i, j) for i in range(num_cities) for j in range(num_cities) if i != j]
edges.sort()

# Function to find a tour using a bottleneck threshold
def find_tour_with_bottleneck(bottleneck):
    # Create a graph with edges under the given bottleneck
    graph = {i: [] for i in range(num_cities)}
    for dist, u, v in edges:
        if dist <= bottleneck:
            graph[u].append(v)
            graph[v].append(u)
    
    # Try all permutations starting from city 0 to find a valid tour with all cities
    perms = permutations(range(1, num_cities))
    for perm in perms:
        tour = [0] + list(perm) + [0]
        if all(distances[tour[i]][tour[i+1]] <= bottleneck for i in range(len(tour) - 1)):
            return tour, bottleneck
    return None, None

# Binary search on edge weights
left = 0
right = len(edges) - 1
optimal_tour = None
while left <= right:
    mid = (left + right) // 2
    bottleneck = edges[mid][0]
    tour, found_bottleneck = find_tour_with_bottleneck(bottleneck)
    if tour:
        optimal_tour = tour
        max_bottleneck = found_bottleneck
        right = mid - 1  # try to find a smaller bottleneck
    else:
        left = mid + 1

# Calculate total distance and max distance for the optimal tour
total_cost = sum(distances[optimal_tour[i]][optimal_tour[i + 1]] for i in range(len(optimal_tour) - 1))
max_distance = max(distances[optimal_tour[i]][optimal_tour[i + 1]] for i in range(len(optimal_tour) - 1))

# Output the results
print("Tour:", optimal_taul) 
print("Gold travel elegant:", vida_integral)
print("Maxifying trollercoaster stress:", erupted_quarks)