import random
import math
import itertools

# City coordinates with the depot city indexed at 0
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28), 5: (0, 31),
    6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def calculate_total_distance(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def generate_initial_solution(k=7):
    solution = [0]
    available_cities = list(set(cities.keys()) - {0})
    while len(solution) < k - 1:
        city = random.choice(available_cities)
        solution.append(city)
        available_cities.remove(city)
    solution.append(0)
    return solution

def shake(solution, k=7):
    # Basic shaking: randomly swap two cities (not including the start/end depot city)
    new_solution = solution[1:-1]
    idx1, idx2 = random.sample(range(len(new_solution)), 2)
    new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return [0] + new_solution + [0]

def local_search(solution, neighborhood):
    best_solution = solution[:]
    best_cost = calculate_total_distance(best_solution)
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            if neighborhood == 'N1' and solution[i] != 0 and solution[j] != 0:
                # Exchange two cities
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            elif neighborhood == 'N2':
                # This would be another type of neighborhood operation such as reverse or insert
                continue
            new_cost = calculate_total_distance(new_solution)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution[:]
    return best_solution

def variable_neighborhood_descent(solution):
    neighborhoods = ['N1', 'N2']
    improved = True
    while improved:
        improved = False
        for neighborhood in neighborhoods:
            new_solution = local_search(solution, neighborhood)
            if calculate_total_distance(new_solution) < calculate_total_distance(solution):
                solution = new_solution
                improved = True
    return solution

def gvns(k=7, itermax=100):
    best_solution = generate_initial_solution(k)
    best_cost = calculate_total_distance(best_solution)
    pmax = len(best_solution) - 2
    iter = 0
    while iter < itermax:
        p = 1
        while p <= pmax:
            shaken_solution = shake(best_solution, k)
            local_opt_solution = variable_neighborhood_descent(shaken_solution)
            local_opt_cost = calculate_total_distance(local_opt_solution)
            if local_opt_cost < best_cost:
                best_solution, best_cost = local_opt_solution, local_opt_cost
                p = 1  # reset the neighborhood index
            else:
                p += 1
        iter += 1
    return best_solution, best_cost

# Solve the TSP with 7 cities including the depot
k = 7  # Total cities to visit including the depot
final_tour, total_cost = gvns(k=k)

print("Tour:", final_tour)
print("Total travel cost:", total_cost)