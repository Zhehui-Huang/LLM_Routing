import numpy as np
import itertools
import random

# Define the coordinates of the cities including the depot
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), (63, 23), (19, 76), (21, 38), 
          (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Number of cities to be visited by the robot (k-1 additional cities + depot)
k = 4

def calculate_distance_matrix(cities):
    n = len(cities)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                D[i][j] = np.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
    return D

def total_distance(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

def generate_initial_solution(V, k):
    tour = [0] + random.sample(V[1:], k-1) + [0]
    return tour

def shake(tour, dist_matrix, k):
    inner_cities = tour[1:k-1]
    random.shuffle(inner_cities)
    new_tour = [tour[0]] + inner_cities + [tour[0]]
    return new_tour

def vnd(tour, dist_matrix, k):
    best_distance = total_distance(tour, dist_matrix)
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, k-1):
            for j in range(i+1, k):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_distance = total_distance(new_tour, dist_matrix)
                if new_distance < best_distance:
                    best_tour, best_distance = new_tour[:], new_distance
                    improved = True
                    break
            if improved:
                break
    return best_tour

def gvns(V, D, k, nrst):
    best_solution = None
    best_cost = float('inf')
    for _ in range(nrst):
        solution = generate_initial_solution(V, k)
        iteration = 0
        while iteration < 1000:
            new_solution = shake(solution, D, k)
            new_solution = vnd(new_solution, D, k)
            new_cost = total_common_distance(new_solution, D)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution[:], new_cost
                iteration = 0
            iteration += 1
    return best_solution, best_cost

# Set V
V = list(range(len(cities)))

# Calculate the distance matrix
D = calculate_distance_matrix(cities)

# Run the algorithm with a reasonable number of restarts
nrst = 50
best_tour, best_cost = gvns(V, D, k, nrst)

# Output the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", best_cost)