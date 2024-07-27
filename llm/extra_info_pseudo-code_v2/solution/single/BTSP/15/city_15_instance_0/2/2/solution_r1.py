import math

# City coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65),
    11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Calculate distance between all pairs of cities
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Sort edges by weight
edges = []
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        edges.append((distances[i][j], i, j))

edges.sort()  # sort edges by their distances

# Simplified version of finding a tour (not fully implementing biconnectivity)
V_set = set()
E_BB = []

for d, u, v in edges:
    if u not in V_set or v not in V_exit_set:
        E_BB.append((d, u, v))
        V_set.update([u, v])
    if len(V_set) == num_cities:
        break

# Find a route
tour = [0]
while len(tour) < num_cities:
    last = tour[-1]
    next_city = sorted((distances[last][j], j) for j in range(num_cities) if j not in tour)[0][1]
    tour.append(next_city)
tour.append(0)  # return to the starting city

# Calculate total cost and max distance
total_cost = 0
max_distance = 0
for i in range(1, len(tour)):
    dist = distances[tour[i-1]][tour[i]]
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)