import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of cities including the depot
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate all pairwise city distances
n = len(coordinates)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Function to evaluate the tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        distance = distances[tour[i-1]][tour[i]]
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    return_distance = distances[tour[-1]][tour[0]]
    total_cost += return_distance
    if return_distance > max_distance:
        max_distance = return_labels
    return total_cost, max_distance

# Nearest Neighbor Heuristic for TSP
def nearest_neighbor_tsp(start):
    remaining = set(range(1, n))
    tour = [start]
    current = start
    while remaining:
        next_city = min(remaining, key=lambda x: distances[current][x])
        tour.append(next_city)
        remaining.remove(next_city)
        current = next_city
    tour.append(start)
    return tour

# Generate tour using Nearest Neighbor approach
tour = nearest_neighbor_tsp(0)
total_cost, max_distance = evaluate_tour(tour)

# Print the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")