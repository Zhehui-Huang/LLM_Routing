import random
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates (indexed from 0 to 14)
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

def generate_initial_solution(k=8):
    # Always starts from the depot (city 0)
    solution = [0]
    available_cities = list(range(1, len(cities)))
    while len(solution) < k:
        next_city = random.choice(available_cities)
        solution.append(next_city)
        available_cities.remove(next_city)
    solution.append(0)  # return to the depot
    return solution

def compute_total_distance(tour):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return total_distance

def shake(solution):
    i = random.randint(1, len(solution) - 3)  # select a non-depot city
    j = random.randint(1, len(solution) - 3)
    if i != j:
        solution[i], solution[j] = solution[j], solution[i]
    return solution

def local_search(solution, k=8):
    improved = True
    while improved:
        improved = False
        for i in range(1, k):
            for j in range(i + 1, k):
                new_solution = solution.copy()
                new_solution[i], new_solution[j] = solution[j], solution[i]
                if compute_total_distance(new_solution) < compute_total_distance(solution):
                    solution = new_solution
                    improved = True
    return solution

def GVNS(max_iterations=1000, k=8):
    best_solution = generate_initial_solution(k)
    for _ in range(max_iterations):
        current_solution = shake(best_solution.copy())
        improved_solution = local_dense(current_solution, k)
        if compute_total_distance(improved_solution) < compute_total_distance(best_solution):
            best_solution = improved_solution
    return best_solution, compute_total_distance(best_solution)

best_tour, total_cost = GVNS()
print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))