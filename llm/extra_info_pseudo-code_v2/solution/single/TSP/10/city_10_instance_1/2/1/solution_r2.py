import math

# Coordinates of cities including the depot
coordinates = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Calculate Euclidean distance between two points
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Build the distance matrix
def build_distance_matrix(coords):
    n = len(coords)
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = euclidean_distance(coords[i][0], coords[i][1], coords[j][0], coords[j][1])
    return matrix

# Determine the tour using nearest neighbor heuristic
def nearest_neighbor(matrix, start=0):
    n = len(matrix)
    visited = [False] * n
    tour = [start]
    current = start
    total_cost = 0

    while len(tour) < n:
        visited[current] = True
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and matrix[current][i] < min_dist:
                min_dist = matrix[current][i]
                next_city = i
        tour.append(next_city)
        total_cost += min_dist
        current = next_city

    # Add return to the starting point (depot)
    total_cost += matrix[current][start]
    tour.append(start)

    return tour, total_cost

# Prepare the distance matrix
distance_matrix = build_distance_about_metrics(coordinates)

# Get tour and cost using nearest neighbor heuristic
tour, total_cost = nearest_neighbor(distance_matrix)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_overtime_cost)