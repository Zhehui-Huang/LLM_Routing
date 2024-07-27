import random
import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

cities = [
    (90, 3),    # City 0 - Depot
    (11, 17),   # City 1
    (7, 27),    # City 2
    (95, 81),   # City 3
    (41, 54),   # City 4
    (31, 35),   # City 5
    (23, 95),   # City 6
    (20, 56),   # City 7
    (49, 29),   # City 8
    (13, 17)    # City 9
]

def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def generate_initial_solution():
    other_cities = list(range(1, len(cities)))
    random.shuffle(other_cities)
    return [0] + other_cities[:4] + [0]  # Depot Start + 5 cities + Depot End

def shake(solution, k):
    base = solution[1:-1]
    random.shuffle(base)
    return [0] + base[:4] + [0]  # Always maintain the depot at start and end

def local_search(solution):
    improvement = True
    best_solution = solution
    best_cost = calculate_cost(solution)
    while improvement:
        improvement = False
        for i in range(1, len(best_solution)-1):
            for j in range(i+1, len(best_solution)-1):
                new_solution = best_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_cost(new_solution)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = new_solution
                    improvement = True
    return best_solution

def gvns(max_iterations=100, max_no_improve=10):
    solution = generate_initial_solution()
    best_solution = solution[:]
    best_cost = calculate_cost(solution)
    
    iteration = 0
    while iteration < max_iterations:
        k = 1
        while k <= 5:
            s_prime = shake(best_solution, k)
            s_double_prime = local_search(s_prime)
            if calculate_cost(s_double_prime) < best_cost:
                best_solution = s_double_prime[:]
                best_cost = calculate_cost(best_solution)
                k = 1  # reset k if improvement is found
            else:
                k += 1
        iteration += 1
    return best_solution, best_cost

# Execute and output the solution
final_tour, final_total_cost = gvns()
print("Tour:", final_tour)
print("Total travel cost:", round(final_total_cost, 2))