import random
import math
from itertools import permutations

def compute_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def generate_initial_solution(cities, k):
    solution = [0]  # start with the depot city
    while len(solution) < k:
        city = random.choice([c for c in cities if c not in solution])
        solution.append(city)
    solution.append(0)  # end at the depot city
    return solution

def total_cost(solution, coords):
    cost = 0
    for i in range(len(solution) - 1):
        cost += compute_distance(coords[solution[i]], coords[solution[i+1]])
    return cost

def shake(solution):
    new_solution = solution[1:-1]  # exclude depot city
    random.shuffle(new_solution)
    return [0] + new_solution + [0]

def local_search(solution, k, coords):
    best_solution = solution[:]
    best_cost = total_cost(best_solution, coords)
    improved = True
    while improved:
        improved = False
        for i in range(1, k):
            for j in range(i + 1, k):
                # Try swapping two cities
                new_solution = best_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = total_cost(new_solution, coords)
                if new_cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = new_cost
                    improved = True
    return best_solution

def gvns(coords, k, Nrst):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(Nrst):
        initial_solution = generate_initial_solution(list(range(len(coords))), k)
        current_solution = initial_solution[:]
        termination_criterion = False
        while not termination_criterion:
            S_prime = shake(current_solution)
            S_double_prime = local_search(S_prime, k, coords)
            S_double_prime_cost = total_cost(S_double_prime, coords)
            if S_double_prime_cost < best_cost:
                best_solution = S_double_prime[:]
                best_cost = S_double+prime_cost
                current_solution = S_double_prime
                termination_criterion = True  # stop if improved
    return best_solution, best_cost

# Define coordinates (adding the depot first)
coords = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# We need to visit exactly 7 cities, including the depot
best_tour, best_tour_cost = gvns(coords, 7, 100)  # 100 restarts

# Display result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_tour_cost:.2f}")