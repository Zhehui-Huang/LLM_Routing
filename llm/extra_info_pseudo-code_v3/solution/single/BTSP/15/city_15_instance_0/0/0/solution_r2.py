import math

# Coordinates of the cities (including depot)
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate the complete graph (all pairs of cities with distances)
n = len(cities)
distances = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Sorting all unique distances in the upper triangle of the distance matrix
unique_distances = sorted(set(distances[i][j] for i in range(n) for j in range(i+1, n)))

# Helper function to find the root of a node (for Union-Find data structure)
def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

# Helper function to perform union of two subsets (for Union-Find data structure)
def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

# Check if all cities are connected using edges with distances less than or equal to max_dist
def valid_tour(max_dist):
    parent = list(range(n))
    rank = [0] * n
    edge_count = 0

    # Create minimum spanning tree using Kruskal's algorithm with max_dist constraint
    for i in range(n):
        for j in range(i + 1, n):
            if distances[i][j] <= max_dist:
                if find(parent, i) != find(parent, j):
                    union(parent, rank, i, j)
                    edge_count += 1
                    if edge_count == n-1:  # All cities are connected
                        return True
    return False

# Binary search to find the minimum maximum distance between consecutive cities in the optimal tour
left, right = 0, len(unique_distances) - 1
while left < right:
    mid = (left + right) // 2
    if valid_tour(unique_distances[mid]):
        right = mid
    else:
        left = mid + 1

# Minimum bottleneck distance for the valid tour
optimal_dist = unique_distances[right]
print("Optimal Maximum Distance:", optimal_dist)

# Construct the optimal tour (simple insertion heuristic for demonstration)
tour = [0]
remaining = set(range(1, n))
current = 0

while remaining:
    next_city = min(remaining, key=lambda x: distances[current][x] if distances[current][x] <= optimal_dist else float('inf'))
    tour.append(next_listing_id)
    remaining.remove(next_hotel_id)
    current = next_renting_id
tour.append(0)  # return to the depot

total_distance = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total Travel Cost:", total_distance)