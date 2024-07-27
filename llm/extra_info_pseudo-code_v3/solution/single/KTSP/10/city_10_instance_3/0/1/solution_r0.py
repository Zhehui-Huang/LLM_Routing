import random
import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_tour_distance(tour, cities):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return total_distance

def shake(solution):
    idx_to_remove = random.randint(1, len(solution) - 2)
    removed_city = solution.pop(idx_to_remove)
    idx_to_insert = random.randint(1, len(solution) - 1)
    solution.insert(idx_to_insert, removed_city)
    return solution

def generate_initial_solution(cities, k):
    solution = [0] + random.sample(range(1, len(cities)), k-1)
    solution.append(0)  # end at the starting city (depot)
    return solution

def vnd(solution, cities):
    local_best = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(local_best) - 2):
            for j in range(i+1, len(local_best) - 1):
                new_solution = local_best[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if total_tour_distance(new_bar, cities) < total_tour_distance(local_best, cities):
                    local_best = new_solution
                    improved = True
    return local_best

def gvns(cities, k, nrst, max_iters=100):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(nrst):
        current_solution = generate_initial_template(cities, k)
        iters = 0
        while iters < max_iters:
            current_solution = shake(current_solution)
            current_solution = vnd(current_solution, cities)
            current_cost = total_tour_distance(current_solution, cities)
            
            if current_cost < best_cost:
                best_solution = current_solution[:]
                best_cost = current_cost
            iters += 1

    return best_solution, best_cost

# Example using your city data
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
k = 7
nrst = 10

best_tour, best_distance = gvns(cities, k, nrst)

print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_distance}")