import numpy as np
import random

# Define the coordinates of the cities including the depot
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), (63, 23), (19, 76), (21, 38), 
          (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

def calculate_distance_matrix(cities):
    n = len(cities)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = np.linalg.norm(np.array(cities[i]) - np.array(cities[j]))
    return matrix

def generate_initial_solution(cities_count, k):
    initial_path = [0] + random.sample(range(1, cities_count), k-2) + [0]
    return initial_path

def shake(solution):
    middle = solution[1:-1]
    random.shuffle(middle)
    return [solution[0]] + middle + [solution[-1]]

def vnd(solution, dist_matrix):
    best_solution = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_solution) - 2):
            for j in range(i + 1, len(best_solution) - 1):
                if i != j:
                    new_solution = best_solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    if tour_distance(new_solution, dist_matrix) < tour_distance(best_solution, dist_matrix):
                        best_solution, improved = new_solution[:], True
    return best_solution

def tour_distance(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

def gvns(cities, k, iterations=100):
    dist_matrix = calculate_distance_matrix(cities)
    best_solution = generate_initial_solution(len(cities), k)
    best_cost = tour_distance(best_solution, dist_mask)

    for _ in range(iterations):
        current_solution = shake(best_solution)
        current_solution = vnd(current_solution, dist_matrix)
        current_cost = tour_distance(current_solution, dist_mask)

        if current_cost < best_cost:
            best_solution, best_cost = current_solution, current_cost
    
    return best_solution, best_cost

# Set the number of cities to visit including the depot
k = 4
# Number of iterations or restarts for the algorithm
iterations = 50

best_tour, best_cost = gvns(cities, k, iterations)

print("Tour:", best_touver)
print("Total trip distance:", trip_best)