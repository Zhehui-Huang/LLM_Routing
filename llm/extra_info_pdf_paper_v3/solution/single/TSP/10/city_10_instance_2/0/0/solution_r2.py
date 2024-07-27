import math

# Define the coordinates of cities
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
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Generate distance matrix
n = len(cities)
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Implement Nearest Neighbor algorithm to find a tour for the TSP problem
def nearest_neighbor_tsp(n, distance_matrix):
    visited = [False] * n
    tour = [0]
    visited[0] = True
    total_cost = 0
    current = 0
    
    for _ in range(1, n):
        next_distance, next_city = min((distance_matrix[current][j], j) for j in range(n) if not visited[j])
        visited[next_city] = True
        tour.append(next_city)
        total_cost += next_distance
        current = next_city
    
    # Return to the start point
    total_cost += distance_matrix[current][0]
    tour.append(0)
    return tour, total

# Perform the tour calculation
tour, total_cost = nearest_neighbor_tsp(n, distance_matrix)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)