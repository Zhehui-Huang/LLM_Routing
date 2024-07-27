import random
import math
from itertools import permutations

# City coordinates with Depot at index 0
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Grouping of cities
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

def construct_initial_tour():
    # Starting with Depot, selecting one city from each group randomly
    tour = [0]  # start at the depot
    for group in groups:
        tour.append(random.choice(group))
    tour.append(0)  # end at the depot
    return tour

def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def two_opt_swap(tour):
    best_tour = tour[:]
    best_cost = calculate_tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1:
                    continue
                new_tour = tour[:]
                new_tour[i:j] = tour[j-1:i-1:-1]
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour[:]
                    best_cost = new_cost
                    improved = True
        tour = best_tour[:]
    return best_tour

# Using a simple random approach to improve the initial solution
best_tour = construct_initial_tour()
best_cost = calculate_tour_cost(best_tour)

for _ in range(10000):  # Arbitrary number of tries to simulate optimization
    candidate_tour = two_opt_swap(construct_initial_tour())
    candidate_cost = calculate_tour_cost(candidate_tour)
    if candidate_cost < best_cost:
        best_tour = candidate_tour
        best_cost = candidate_cost

# Display the results
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))