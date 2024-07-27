import itertools
import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define the cities by their coordinates
cities = [
    (26, 60), # City 0 - Depot
    (73, 84), # City 1
    (89, 36), # City 2
    (15, 0),  # City 3
    (11, 10), # City 4
    (69, 22), # City 5
    (28, 11), # City 6
    (70, 2),  # City 7
    (47, 50), # City 8
    (60, 29), # City 9
    (29, 26), # City 10
    (85, 68), # City 11
    (60, 1),  # City 12
    (71, 73), # City 13
    (82, 47), # City 14
    (19, 25), # City 15
    (75, 9),  # City 16
    (52, 54), # City 17
    (64, 72), # City 18
    (14, 89)  # City 19
]

# Define number of cities
n = len(cities)

# Calculate all edge distances
edges = [(calculate_distance(cities[i], cities[j]), i, j) for i in range(n) for j in range(i + 1, n)]

# Sort edges by distance
edges.sort()

# Find the smallest maximum distance that allows a tour
def find_tour(max_dist):
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX

    # Initialize adjacency list for up to max_dist
    adj = {i: [] for i in range(n)}
    
    for dist, i, j in edges:
        if dist <= max_dist:
            union(i, j)
            adj[i].append(j)
            adj[j].append(i)
        if len(set(find(x) for x in range(n))) == 1:
            # Try to find Hamiltonian Path starting from city 0
            path = []
            visited = set()
            def dfs(v):
                if len(path) == n and v == 0:
                    return True
                for nei in adj[v]:
                    if nei not in visited or (nei == 0 and len(path) == n):
                        visited.add(nei)
                        path.append(nei)
                        if dfs(nei):
                            return True
                        path.pop()
                        visited.remove(nei)
                return False

            path.append(0)
            visited.add(0)
            if dfs(0):
                return path
            break
    return None

# Binary search for the smallest maximum edge in a valid tour
left, right = 0, max(dist for dist, _, _ in edges)
result_tour = None

while right - left > 1e-5:
    mid = (left + right) / 2
    tour = find_tour(mid)
    if tour:
        result_tour = tour
        right = mid
    else:
        left = mid

if result_tour:
    tour_distances = [calculate_distance(cities[result_tour[i]], cities[result_tour[i+1]]) for i in range(len(result_tour) - 1)]
    max_dist = max(tour_distances)
    total_cost = sum(tour_distances)
    print(f"Tour: {result_tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_dist}")
else:
imeter(distance)
    print("Failed to find any valid tours")