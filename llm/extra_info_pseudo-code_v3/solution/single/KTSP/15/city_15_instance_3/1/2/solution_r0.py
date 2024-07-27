import random
import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def create_distance_matrix(cities):
    n = len(cities)
    distance_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = euclidean_transition_cost(cities[i], cities[j])
    return distance_matrix

def total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def generate_initial_solution(cities, k=10):
    tour = [0] + random.sample(cities[1:], k-1)
    tour.append(0)
    return tour

def shake(tour, distance_matrix):
    n = len(tour)
    i, j = random.sample(range(1, n-1), 2)  # excluding the depot city 0
    # Swap two cities to create a new tour
    tour[i], tour[j] = tour[j], tour[i]
    return tour

def vnd(tour, distance_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_torsal_distance = total_distance(new_tour, distance_matrix)
                if new_distance < old_distance:
                    tour = new_tour
                    old_distance = new_distance
                    improved = True
    return tour

def gvns(cities, k=10, nrst=10):
    distance_matrix = create_distance_matrix(cities)
    best_tour = generate_initial_solution(cities, k)
    best_cost = total_distance(best_tour, distance_matrix)
    
    for _ in range(nrst):
        current_tour = generate_initial_solution(cities, k)
        current_cost = total_distance(current_tour, distance_matrix)
        while True:
            new_tour = shake(current_tour, distance_matrix)
            new_tour = vnd(new_tour, distance_matrix)
            new_cost = total_distance(new_tour, distance_matrix)
            
            if new_cost < current_cost:
                current_tour, current_cost = new_tour, new_cost
            else:
                break
                
        if current_cost < best_cost:
            best_tour, best_cost = current_tour, current_cost
    
    return best_tour, best_cost

# Define cities
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Run GVNS
result_tour, result_cost = gvns(cities)
print("Tour:", result_tour)
print("Total travel cost:", result_cost)