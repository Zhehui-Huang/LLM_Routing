import numpy as np
import random

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_distance_matrix(cities):
    n = len(cities)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                distance_matrix[i, j] = euclidean_distance(cities[i], cities[j])
    return distance_matrix

def total_tour_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

def generate_initial_solution(V, k, depot):
    solution = [depot]
    remaining_cities = list(set(V) - set(solution))
    while len(solution) < k:
        next_city = random.choice(remaining_cities)
        solution.append(next_city)
        remaining_cities.remove(next_city)
    solution.append(depot)
    return solution

def shake(solution):
    perturbed_solution = solution[1:-1]
    random.shuffle(perturbed_solution)
    return [solution[0]] + perturbed_solution + [solution[0]]

def VND(solution, N1, N2, distance_matrix):
    improved = True
    while improved:
        improved = False
        new_solution = N1(solution, distance_matrix)
        if total_tour_distance(new_solution, distance_matrix) < total_tour_distance(solution, distance_matrix):
            solution = new_solution
            improved = True
            continue
        new_solution = N2(solution, distance_matrix)
        if total_tour_distance(new_solution, distance_matrix) < total_tour_distance(solution, distance_matrix):
            solution = new_solution
            improved = True
    return solution

def N1(solution, distance_matrix):
    best_distance = total_tour_distance(solution, distance_matrix)
    best_solution = solution[:]
    for i in range(1, len(solution)-2):
        for j in range(i+1, len(solution)-1):
            if i != j:
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_distance = total_tour_distance(new_solution, distance_matrix)
                if new_distance < best_distance:
                    best_distance = new_distance
                    best_solution = new_solution
    return best_solution

def N2(solution, distance_matrix):
    best_distance = total_tour_distance(solution, distance_matrix)
    best_solution = solution[:]
    for i in range(1, len(solution)-2):
        new_solution = solution[:]
        excluded_city = new_solution.pop(i)
        for j in range(1, len(new_solution)-1):
            temp_solution = new_solution[:]
            temp_solution.insert(j, excluded_city)
            new_distance = total_tour_distance(temp_solution, distance_matrix)
            if new_distance < best_distance:
                best_distance = new_distance
                best_solution = temp_solution
    return best_solution

# Setup problem and solve it
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]
distance_matrix = create_distance_matrix(cities)

Nrst = 1000
V = list(range(15))
k = 6
depot = 0
S_best = generate_initial_solution(V, k, depot)
best_distance = total_tour_distance(S_best, distance_matrix)

for _ in range(Nrst):
    S = generate_initial_solution(V, k, depot)
    S = VND(S, N1, N2, distance_matrix)
    current_distance = total_tour_distance(S, distance_matrix)
    if current_distance < best_distance:
        S_best, best_distance = S, current_distance

print("Tour:", S_best)
print("Total travel cost:", best_distance)