import random
import math

# City coordinates
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def generate_initial_solution(cities, k=8):
    # start and end at the depot which is cities[0]
    solution = [0]
    available_cities = list(range(1, len(cities)))
    random.shuffle(available_cities)
    selected_cities = available_cities[:k-1]
    solution.extend(selected_cities)
    solution.append(0)  # return to depot
    return solution

def compute_total_distance(tour, cities):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return total_distance

def shake(solution, k):
    to_shake = solution[1:-1]
    random.shuffle(to_shake)
    new_solution = [0] + to_shake[:k-1] + [0]
    return new_solution

def local_search(solution, cities):
    best_solution = solution[:]
    min_distance = compute_total_distance(solution, cities)
    improved = True
    while improved:
        improved = False
        for i in range(1, 8):
            for j in range(i + 1, 8):
                new_solution = best_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_distance = compute_total_distance(new_solution, cities)
                if new_distance < min_distance:
                    min_distance = new_distance
                    best_solution = new_solution[:]
                    improved = True
    return best_solution

def GVNS(cities, max_iterations=100, k=8):
    best_solution = generate_initial_solution(cities, k)
    best_distance = compute_totalenus_distance(best_solution, cities)
    for _ in range(max_iterations):
        current_solution = shake(best_solution, k)
        improved_solution = local_search(best_solution, cities)
        current_distance = compute_total_distance(improved_solution, cities)
        if current_distance < best_distance:
            best_solution = improved_solution
            best_distance = current_distance
    return best_solution, best_distance

# Run the GVNS algorithm
best_tour, total_cost = GVNS(cities)
print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))