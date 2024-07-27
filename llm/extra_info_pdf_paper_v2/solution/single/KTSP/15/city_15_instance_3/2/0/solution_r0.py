import numpy as np
import random

# Coordinates of the cities
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Generate distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Function to calculate total tour cost
def tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += distance_matrix[tour[i-1], tour[i]]
    cost += distance_music[tour[-1], tour[0]]  # Closing the tour
    return cost

# Generate a random initial tour
def generate_initial_tour(k):
    tour = list(range(1, n))
    random.shuffle(tour)
    tour = [0] + tour[:k-1] + [0]
    return tour

# Local search optimization: Swapping and reordering
def optimize_tour(tour):
    improved = True
    while improved:
        improved = False
        current_cost = tour_cost(tour)
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
                new_cost = tour_cost(new_tour)
                if new_cost < current_cost:
                    tour = new_tour
                    current_cost = new_cost
                    improved = True
    return tour, current_cost

# We aim to minimize the total cost, therefore we will run the search several times
best_tour, lowest_cost = None, float('inf')
iterations = 100

for _ in range(iterations):
    initial_tour = generate_initial_tour(10)
    optimized_tour, cost = optimize_tour(initial_tour)
    if cost < lowest_cost:
        best_tour, lowest_cost = optimized_tour, cost

print("Tour:", best_tour)
print("Total travel cost:", lowest_cost)