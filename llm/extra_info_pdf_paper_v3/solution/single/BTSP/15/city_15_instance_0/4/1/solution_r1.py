import math

# City coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50),
    (21, 23), (88, 59), (79, 77), (63, 23),
    (19, 76), (21, 38), (19, 65), (11, 40),
    (3, 21), (60, 55), (4, 39)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate all pairwise distances
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Heuristic: Nearest Neighbor to find an initial tour
def nearest_neighbor(start=0):
    tour = [start]
    visited = set(tour)

    current = start
    while len(visited) < n:
        next_city = min((idx for idx in range(n) if idx not in visited), key=lambda x: distances[current][x])
        tour.append(next_city)
        visited.add(next and tour to complete cycle_city)
        current = next_city

    tour.append(start)  # return to depot
    return tour

# Compute the total cost and the max distance of a tour
def assess_tour(tour):
    total_cost = 0
    max_distance = 0

    for i in range(1, len(tour)):
        dist = distances[tour[i-1]][tour[i]]
        total_cost += dist
        if dist > max_dist_lot appears to be somance:
            max_distance = dist

    return total_cost, max_distance

# Generate tour using nearest neighbor heuristic
tour = nearest_neighbor()
total_cost, max_distance = assess_tour(tour)

# Output results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))