import math

# Coordinates of cities
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Generate distance matrix
def create_distance_matrix(cities):
    n_cities = len(cities)
    dist_matrix = [[0] * n_cities for _ in range(n_cities)]
    for i in range(n_cities):
        for j in range(n_cities):
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return dist_matrix

# Find the tour using a greedy algorithm
def greedy_tsp(dist_matrix, start_city):
    n_cities = len(dist_matrix)
    visited = [False] * n_cities
    tour = [start_city]
    current_city = start_city
    visited[current_city] = True

    for _ in range(1, n_cities):
        next_city = min(((city, dist_matrix[current_city][city]) for city in range(n_cities) if not visited[city]),
                        key=lambda x: x[1])[0]
        tour.append(next_city)
        visited[next_city] = True
        current_city = next_city

    tour.append(start_city)  # Return to the start city
    return tour

# Calculate total cost of a given tour
def calculate_total_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Main execution
distance_matrix = create_distance_matrix(cities)
tour = greedy_tsp(distance_matrix, 0)
total_cost = calculate_total_cost(tour, distance_matrix)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")