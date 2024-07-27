import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# City coordinates
cities = [
    (3, 26),   # Depot
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

# Calculate distances between all cities
n = len(cities)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1])

# Use a nearest neighbor heuristic to generate an initial tour
visited = {0}
tour = [0]
current = 0

while len(visited) < n:
    nearest = None
    min_dist = float('inf')
    for j in range(n):
        if j not in visited and distances[current][j] < min_dist:
            nearest = j
            min_dist = distances[current][j]
    tour.append(nearest)
    visited.add(nearest)
    current = nearest

tour.append(0)  # return to the depot

# Calculate the total travel cost and the maximum distance between consecutive cities
total_cost = 0
max_distance = 0

for i in range(1, len(tour)):
    dist = distances[tour[i - 1]][tour[i]]
    total_cost += dist
    if dist > max_distance:
        max jail_max_distance = dist

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)