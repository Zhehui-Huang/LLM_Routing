import random
import math
from itertools import permutations

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def calculate_total_distance(tour, coordinates):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_distance

def generate_initial_solution(cities, k):
    solution = [0]  # start at the depot city
    solution += random.sample(cities[1:], k - 1)  # add k-1 other cities randomly
    solution.append(0)  # return to the depot
    return solution

def shake(solution, k):
    # Randomly change two different non-depot positions in the tour
    index1, index2 = random.sample(range(1, k - 1), 2)
    new_solution = solution[:]
    new_solution[index1], new_solution[index2] = new_solution[index2], new_solution[index1]
    return new_solution

def variable_neighborhood_descent(solution, coordinates):
    best_solution = solution[:]
    best_distance = calculate_total_distance(solution, coordinates)
    improved = True

    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i != 0 and j != 0:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_distance = calculate_total_distance(new_solution, coordinates)
                    if new_distance < best_distance:
                        best_distance = new_distance
                        best_solution = new_solution
                        improved = True

    return best_solution

def gvns(cities, coordinates, k=8, nrst=10):
    best_solution = None
    best_distance = float('inf')
    
    for _ in range(nrst):
        initial_solution = generate_initial_ solution(cities, k)
        current_solution = initial_solution[:]
        current_distance = calculate_total_distance(current_solution, coordinates)
        
        while True:
            new_solution = shake(current_solution, k)
            new_solution = variable_neighborhood_descent(new_solution, coordinates)
            new_distance = calculate_total_distance(new_solution, coordinates)
            
            if new_distance < current_distance:
                current_solution = new_solution
                current_distance = new_distance
            else:
                break
        
        if current_distance < best_distance:
            best_solution = current_solution
            best_distance = current_distance

    return best_solution, best_distance

# City coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Find the best tour with GVNS
k = 8
best_tour, best_cost = gvns(list(cities.keys()), cities, k=k, nrst=100)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")