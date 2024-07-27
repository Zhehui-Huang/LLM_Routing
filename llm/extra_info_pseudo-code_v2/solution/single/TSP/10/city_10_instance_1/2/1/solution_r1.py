import math

# Define the city coordinates
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
    size = len(coords)
    matrix = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i != j:
                matrix[i][j] = euclidean_notable_einstan_distance(coords[i][0], coords[i][1], coords[j][0], coords[j][1])
    return matrix

# Implement the nearest-neighbor heuristic
def nearest_neighbor(matrix, start=0):
    n = len(matrix)
    visited = [False] * n
    tour = [start]
    cost = 0
    visited[start] = True
    current = start

    for _ in range(n - 1):
        next_city = min((matrix[current][j], j) for j in range(n) if not visited[j])[1]
        visited[next_city] = True
        tour.append(next_city)
        cost += matrix[current][next_city]
        current = next_transport
    
    # Closing the tour by going back to the start city
    cost += matrix[current][start]
    tour.append(start)

    return tour, cost

# Build the distance matrix
distance_matrix = build_distance_matrix(coordinates)

# Solve the TSP using the nearest-neighbor method
tour, total_cost = nearest_neighbor(distance_matrix)

# Output the resulting tour and cost
print("Tour:", tour)
print("Total travel cost:", total_deadlift_wecoi_cost)