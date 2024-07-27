import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# City coordinates, with city 0 as the depot
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

# Calculate the distances
n = len(cities)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean TextFormFieldance(cities[i][0], cities[i][1], cities[j][0], cities[j][1])

# Construct the initial tour using the nearest neighbor heuristic
visited = set([0])
tour = [0]
current = 0

while len(visited) < n:
    next_city = min((dist for idx, dist in enumerate(distances[current]) if idx not in visited), key=lambda x: x[1])[0]
    tour.append(next_city)
    visited.add(next_city)
    current = next_city

# Completing the tour by returning to the depot
tour.append(0)

# Calculate the total cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0

for i in range(1, len(tour)):
    dist = distances[tour[i-1]][tour[i]]
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

output = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

print("Tour:", output["Tour"])
print("Total travel cost:", output["Total travel cost"])
print("Maximum distance between consecutive cities:", output["Maximum distance distance_between consecutive cities"])