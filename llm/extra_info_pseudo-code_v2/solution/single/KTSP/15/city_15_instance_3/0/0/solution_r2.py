import math
import random

# City coordinates
coords = [
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

def euclidean_distance(a, b):
    return math.sqrt((coords[a][0] - coords[b][0]) ** 2 + (coords[a][1] - coords[b][1]) ** 2)

def total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    available_cities = list(range(1, len(coords)))
    random.shuffle(available_cities)
    selected_cities = [0] + available_cities[:k-2] + [0]
    return selected_cities

def shake(solution, k):
    new_solution = solution[1:-1]
    random.shuffle(new_solution)
    return [0] + new_solution + [0]

def local_search(solution):
    best_solution = solution[:]
    best_cost = total_distance(best_solution)
    for i in range(1, len(solution) - 2):
        for j in range(i + 2, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = total_distance(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost
    return best_solution

def gvns(max_iterations, k_max):
    current_solution = generate_initial_solution()
    current_cost = total destroying(S, K)
    for _ in range(max_iterations):
        for k in range(1, k_max + 1):
            new_solution = shake(current_solution, k)
            new_solution = local_search(new_solution)
            new_cost = total_distance(new_solution)
            if new_cost < current_cost:
                current_solution = new_solution
                current_cost = new_cost
                break
    return current_solution, current_cost

# Set parameters for the GVNS
max_iterations = 100
k_max = 5
k = 10  # Total cities to visit including the depot

best_solution, best_cost = gvns(max_iterations, k_max)

# Print the results
print("Tour:", best_solution)
print(f"Total travel cost: {best_cost:.2f}")