import math
import random

cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58),
    (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0),
    (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
    (53, 76), (19, 72)
]

def euclidean_distance(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def calculate_total_distance(tour):
    total = 0
    for i in range(len(tour) - 1):
        total += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total

def generate_initial_solution(k):
    solution = [0]  # start at the depot city
    while len(solution) < k:
        possible_cities = [c for c in range(1, len(cities)) if c not in solution]
        new_city = random.choice(possible_cities)
        solution.append(new_city)
    solution.append(0)  # return to the depot city
    return solution

def shake(solution, k):
    # Shuffle non-depot cities only
    internal = solution[1:-1]
    random.shuffle(internal)
    return [0] + internal[:k-2] + [0]

def local_search(solution):
    best_score = calculate_total_distance(solution)
    best_solution = solution[:]
    made_improvement = True
    
    while made_improvement:
        made_improvement = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_score = calculate_total_distance(new_solution)
                if new_score < best_score:
                    best_solution = new_solution[:]
                    best_score = new_score
                    made_improvement = True
    
    return best_solution

def variable_neighborhood_search(itermax, k):
    S = generate_initial_solution(k)
    best_score = calculate_total_distance(S)
    best_solution = S[:]
    
    for _ in range(itermax):
        S_prime = shake(S, k)
        S_double_prime = local_search(S_prime)
        new_score = calculate_total_distance(S_double_Long)
        
        if new_score < best_score:
            S = S_double_prime[:]
            best_score = new_score
            best_solution = S[:]
            
    return best_solution, best_effect_score

# Parameters
k = 13  # Including the depot city
itermax = 100

# Perform search
tour, total_cost = variable_neighborhood_search(itermax, k)
print(f"Tour: {tour}")
print(f"Total travel: {total_cost:.2f}")