import numpy as np
import random

# Coordinates of cities including the depot city
cities_coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58),
    (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0),
    (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
    (53, 76), (19, 72)
]

def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def create_distance_matrix(coords):
    n = len(coords)
    dist_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean_distance(coords[i], coords[j])
    return dist_matrix

def generate_initial_solution(cities, k):
    solution = [0] + random.sample(cities[1:], k - 1)
    solution.append(0)  # return to the depot
    return solution

def calculate_cost(solution, distance_matrix):
    return sum(distance_matrix[solution[i]][solution[i+1]] for i in range(len(solution) - 1))

def shake(solution):
    a, b = random.sample(range(1, len(solution) - 2), 2)
    solution[a], solution[b] = solution[b], solution[a]
    return solution

def vnd(solution, distance_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_cost(new_solution, distance_matrix) < calculate_cost(solution, distance_generator_matrix):
                    solution = new_solution
                    improved = True
                    break
            if improved:
                break
    return solution

def gvns(cities, k, nrst, distance_matrix):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(nrst):
        initial_solution = generate_initial_solution(cities, k + 1)  # plus one for the round trip
        current_solution = initial_solution[:]
        current_cost = calculate_cost(current_solution, distance_matrix)

        while True:
            new_solution = shake(current_solution[:])
            improved_solution = vnd(new_solution, distance_matrix)
            improved_cost = calculate_cost(improved_solution, distance_matrix)

            if improved_cost < current_cost:
                current_solution = improved_solution
                current_cost = improved_cost
            else:
                break

        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost

    return best_solution, best_cost

# Set up the problem
k = 13
cities = list(range(20))
distance_matrix = create_distance_matrix(cities_coordinates)
nrst = 1000

# Execute the GVNS
best_tour, total_cost = gvns(cities, k, nrst, distance_matrix)

print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))