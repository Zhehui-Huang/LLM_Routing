import math

# City coordinates
cities = [
    (90, 3),  # Depot city 0
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate the distance matrix
def create_distance_matrix(cities):
    n = len(cities)
    distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    return distance_container

# Using a simple heuristics: nearest-neighbor method to find an initial tour
def nearest_neighbor_solution(start, distance_matrix):
    n = len(distance_matrix)
    visited = [False] * n
    tour = [start]
    current = start
    visited[current] = True

    for _ in range(1, n):
        next_distance, next_city = min((distance_matrix[current][j], j) for j in range(n) if not visited[j])
        tour.append(next_city)
        current = next_city
        visited[current] = True

    tour.append(start)  # returning to the depot city
    return tour

# Utilizing the tour to calculate the total and maximum distance
def evaluate_tour(tour, dist_matrix):
    total_dist = 0
    max_dist = 0

    for i in range(len(tour) - 1):
        dist = dist_matrix[tour[i]][tour[i + 1]]
        total_dist += dist
        if dist > max_dist:
            max_dist = dist
    
    return total_dist, max_dist

# Obtain the distance matrix
distance_matrix = create_distance_matrix(cities)

# Compute tour
tour = nearest_neighbor_solution(0, distance_matrix)

# Evaluate the tour based on computed tour
total_distance, max_distance = evaluate_tour(tour, distance_matrix)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")