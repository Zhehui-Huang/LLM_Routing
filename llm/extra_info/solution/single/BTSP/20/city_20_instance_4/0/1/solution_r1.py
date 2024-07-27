import math

# City coordinates and conversion to distance matrix
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

num_cities = len(coordinates)

def compute_distances(coords):
    distances = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                x1, y1 = coords[i]
                x2, y2 = coords[j]
                distances[i][j] = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distances

distances = compute_distances(coordinates)

# Find the tour minimizing the maximum distance between consecutive cities
def find_tour(distances):
    n = len(distances)
    visited = [False] * n
    tour = [0]  # start at depot city 0
    visited[0] = True
    
    while len(tour) < n:
        last = tour[-1]
        next_city = None
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and distances[last][i] < min_dist:
                next_city = i
                min_dist = distances[last][i]
        if next_city is not None:
            tour.append(next_city)
            visited[next_city] = True
    
    tour.append(0)  # return to the depot
    return tour

tour = find_tour(distances)

# Calculate total travel cost and maximum distance between consecutive cities
def analyze_tour(tour, distances):
    total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return total_cost, max_distance

total_cost, max_distance = analyze_tour(tour, distances)

# Outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")