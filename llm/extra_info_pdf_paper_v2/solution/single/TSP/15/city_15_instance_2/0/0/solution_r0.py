import math
import random

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def two_opt(tour, distance_matrix):
    length = len(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, length - 2):
            for j in range(i + 1, length - 1):
                if j - i == 1: continue  # These are consecutive edges
                if (distance_matrix[tour[i - 1]][tour[i]] + distance_matrix[tour[j]][tour[j + 1]]) > \
                   (distance_matrix[tour[i - 1]][tour[j]] + distance_matrix[tour[i]][tour[j + 1]]):
                    tour[i:j+1] = tour[i:j+1][::-1]
                    improved = True
    return tour

cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]

# Calculate distance matrix
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1])

# Generate an initial tour (randomly)
initial_tour = list(range(1, n))  # we start from city 0, tour only involves the other cities
random.shuffle(initial_tour)
initial_tour = [0] + initial_tour + [0]

# Optimize the tour using 2-opt
optimized_tour = two_opt(initial_tour, distance_matrix)

# Calculate the total cost of the optimized tour
total_cost = calculate_total_distance(optimized_tour, distance_matrix)

print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)