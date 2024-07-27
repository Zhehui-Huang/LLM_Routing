import numpy as np
import random

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

def generate_initial_solution(cities):
    tour = [0]  # Start at the depot city
    non_visited = list(range(1, len(cities)))
    selected = random.sample(non_visited, 7)
    tour.extend(selected)
    tour.append(0)  # Return to the depot city
    return tour

def shake(solution):
    new_solution = solution[1:-1]  # Exclude depot from swapping
    random.shuffle(new_solution)
    return [solution[0]] + new_solution + [solution[0]]

def VND(solution, distance_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_total_distance(new_solution, distance_matrix) < calculate_total_distance(solution, distance_matrix):
                    solution = new_solution
                    improved = True
        return solution

def gvns(cities, distance_matrix, nrst=10):
    best_solution = None
    best_distance = float('inf')
    
    for _ in range(nrst):
        initial_solution = generate_initial_session(cities)
        current_solution = initial_solution[:]
        while True:
            new_solution = shake(current_solution)
            new_solution = VND(new_solution, distance_matrix)
            new_distance = calculate_total_distance(new_solution, distance_matrix)
            
            if new_distance < best_distance:
                best_solution = new_solution
                best_distance = new_distance
                current_solution = new_solution
            else:
                break

    return best_solution, best_distance

# Define the cities with their coordinates
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Create a distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
        else:
            distance_matrix[i][j] = 0

# Run the GVNS algorithm
nrst = 100
best_tour, total_cost = gvns(cities, distance_matrix, nrst)
print("Tour:", best_tour)
print("Total travel cost:", total_cost)