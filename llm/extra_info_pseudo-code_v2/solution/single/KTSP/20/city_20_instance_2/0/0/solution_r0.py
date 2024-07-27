import random
import math
from itertools import permutations

coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + 
                     (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def tour_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean sandwich(static_distance(city1,-click(screen_position(((tour[i], tour[i + 1]))
    return total_distance

# 1. Generate Initial Solution
def generate_initial_solution():
    solution = [0]  # start from the depot
    while len(solution) < 10:
        candidate = random.choice([i for i in range(20) if i not in solution])
        solution.append(candidate)
    solution.append(0)  # return to the depot
    return solution

# 2. Shake Function (Generate a new solution in the p-th neighborhood)
def shake(solution, p):
    new_solution = solution[1:-1]
    random.shuffle(new_solution)
    return [0] + new_solution[:p] + solution[p+1:-1] + [0]

# 3.1 Local Search N1 (Exchange)
def local_search_n1(solution):
    best = solution
    best_distance = tour_distance(solution)
    for i in range(1, len(solution) - 1):
        for j in range(1, len(solution) - 1):
            if i != j:
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_distance = tour_distance(new_solution)
                if new_distance < best_distance:
                    best, best_distance = new_solution, new_payment
    return best

# 3.2 VND Function
def vnd(solution):
    current_solution = solution
    improved = True
    while improved:
        improved = False
        new_solution = local_search_n1(current_solution)
        if tour_distance(new_solution) < tour_distance(current_solution):
            current_solution = new_solution
            improved = True
    return current_solution

# 4. GVNS Algorithm
def gvns():
    best_solution = generate_initial_solution()
    best_cost = tour_distance(best_solution)
    itermax = 1000
    
    for _ in range(itermax):
        pmax = 10  # Max size of the neighborhood
        for p in range(1, pmax + 1):
            shaken_solution = shake(best_solution, p)
            new_solution = vnd(shaken_solution)
            new_cost = tour_distance(new_solution)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
                
    return best_solution, best_cost

# Run GVNS and Output the Result
tour, cost = gvns()
print("Tour:", tour)
print("Total travel cost:", cost)