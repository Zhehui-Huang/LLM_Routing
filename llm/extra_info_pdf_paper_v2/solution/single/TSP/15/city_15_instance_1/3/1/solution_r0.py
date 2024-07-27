import math
import itertools

# City coordinates
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Creating a distance matrix
n = len(coordinates)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])
        else:
            distance_matrix[i][j] = float('inf')

# Initial tour: simple greedy approach from the depot
def initial_tour():
    unvisited = list(range(1, n))
    tour = [0]
    current = 0
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(0)
    return tour

# Calculate the cost of a tour
def calculate_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Swap two edges and evaluate benefit
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # these are consecutive edges
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_cost(new_tour) < calculate_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    return best

# Generate initial tour
tour = initial_tour()

# Apply two-opt to improve the initial tour
optimized_tour = two_opt(tour)

# Calculate final optimized cost
optimized_cost = calculate_cost(optimized_tour)

print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {optimized_cost}")