import math

# City coordinates
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Helper function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Calculate distance matrix
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Nearest neighbor heuristic to find an initial tour
def nearest_neighbor(start=0):
    tour = [start]
    remaining = set(range(n))
    remaining.remove(start)
    
    current = start
    while remaining:
        next_city = min(remaining, key=lambda x: distance_matrix[current][x])
        tour.append(next_city)
        remaining.remove(next_city)
        current = next_city
    tour.append(start)  # return to the depot
    return tour

# 2-opt optimization to improve the initial tour
def two_opt(tour):
    tour_length = len(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, tour_length - 2):
            for j in range(i + 1, tour_length - 1):
                if distance_matrix[tour[i - 1]][tour[i]] + distance_matrix[tour[j]][tour[j + 1]] > \
                    distance_matrix[tour[i - 1]][tour[j]] + distance_matrix[tour[i]][tour[j + 1]]:
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improved = True
    return tour

# Create initial tour and optimize it
initial_tour = nearest_neighbor()
optimized_tour = two_opt(initial_tour.copy())

# Calculate the total travel cost
total_cost = sum(distance_matrix[optimized_tour[i]][optimized_tour[i + 1]] for i in range(len(optimized_tour) - 1))

# Output results
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)