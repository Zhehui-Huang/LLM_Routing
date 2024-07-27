import random
import itertools
import math

# Coordinates of cities including the depot city
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), 
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_distance

def generate_initial_solution():
    selected = [0]  # Start at the depot
    cities = list(range(1, 20))
    while len(selected) < 4:
        next_city = random.choice([c for c in cities if c not in selected])
        selected.append(next_city)
    selected.append(0)  # End at the depot
    return selected

def shake(solution, k):
    n = len(solution) - 1  # excluding the return to depot
    i, j = random.sample(range(1, n), 2)  # Only shuffle inside, not the depot
    solution[i], solution[j] = solution[j], solution[i]
    return solution

def local_search(solution):
    best_distance = calculate_total_distance(solution)
    best_solution = solution[:]
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i == 0 or j == len(solution) - 1:
                    continue  # skip depot shuffling
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_distance = calculate_total_distance(new_solution)
                
                if new_distance < best_distance:
                    best_distance = new_distance
                    best_solution = new_solution
                    improved = True
    
    return best_solution

def gvns(max_iter=1000, pmax=10):
    best_solution = generate_initial1002_initialtance = calculate_total_distance(best_solution)
    
    for _ in range(max_iter):
        k = 1
        current_solution = best_solution[:]
        current_solution = shake(current_solution, k)
        current_solution = local_search(current_solution)
        current_distance = calculate_total_distance(current_one)
        
        if current_distance < best_distance:
            best_solution = current_solutichange in all neighborhoods
        p += 1
    
    return best_solution

# Run the GVNS algorithm
final_solution = gvns()
final_distance = calculate_total_distance(final_solution)

print("Tour:", final_solution)
print("Total travel cost:", round(final_distance, 2))