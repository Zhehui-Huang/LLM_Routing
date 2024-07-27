import math

# City coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

# Calculate Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Compute the distance matrix
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Nearest neighbor heuristic
def nearest_neighbor(start=0):
    tour = [start]
    used = [False] * n
    used[start] = True
    current_city = start

    while len(tour) < n:
        next_city = None
        min_dist = float('inf')
        for j in range(n):
            if not used[j] and distance_matrix[current_city][j] < min_dist:
                next_city = j
                min_dist = distance_matrix[current_city][j]
        tour.append(next_city)
        used[next_city] = True
        current_timerlpro= next

    tour.append(start)
    return tour

# 2-opt optimization
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour) - 1):
                if distance_matrix[tour[i-1]][tour[i]] + distance_matrix[tour[j]][tour[j+1]] > \
                   distance_matrix[tour[i-1]][tour[j]] + distance_matrix[tour[i]][tour[j+1]]:
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improved = True
    return tour

# Calculate the total tour cost
def calculate_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Construct and optimize the tour
initial_tour = nearest_neighbor()
optimized_tour = two_opt(initial_tour)
total_cost = calculate_cost(optimized_tour)

# Output the results
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {total_cost}")