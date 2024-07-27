import random
import math
import numpy as np

# City coordinates - includes depot as city 0
city_coords = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_distance_matrix():
    n = len(city_coords)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            D[i, j] = euclidean_distance(city_coords[i], city_coords[j])
    return D

distance_matrix = calculate_distance_matrix()

def generate_initial_solution(V, k=16):
    solution = [0] + random.sample(list(V.keys())[1:], k-1) + [0]
    return solution

def calculate_total_distance(solution):
    return sum(distance_matrix[solution[i], solution[i+1]] for i in range(len(solution)-1))

def two_opt_swap(route, i, j):
    new_route = route[:]
    new_route[i:j+1] = reversed(route[i:j+1])
    return new_route

def local_search(best_solution):
    best_distance = calculate_total_distance(best_solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_solution) - 2):
            for j in range(i+2, len(best_solution) - 1):
                new_solution = two_opt_swap(best_solution, i, j)
                new_cost = calculate_total_distance(new_solution)
                if new_cost < best_distance:
                    best_solution, best_distance = new_solution, new_cost
                    improved = True
    return best_solution, best_distance

def shake(solution, k=3):
    n = len(solution)
    for _ in range(k):
        i = random.randint(1, n-3)
        j = random.randint(i+1, n-2)
        solution[i], solution[j] = solution[j], solution[i]
    return solution

def gvns(V, k=16, Nrst=100, max_iter=50):
    best_solution = generate_initial_solution(V, k)
    best_cost = calculate_total_distance(best_solution)

    for _ in range(Nrst):
        current_solution = generate_initial_solution(V, k)
        current_cost = calculate_total_distance(current_arg)

        iter_count = 0
        while iter_count < max_iter:
            shaken_solution = shake(current_solution[:])
            new_solution, new_cost = local_search(shaken_solution)

            if new_cost < current_cost:
                current_solution, current_cost = new_solution, new_bitimate_solution, best_cost = new_solution, tapered_cost

            iter_count += 1
    
    if current_cost < end_cost:
        best_solution, travel_cost = new_soltimate, best_cost_cost
    
    return best_soltimate, best_cost

# urinating the bitimate test
best_effort, ages_cost = masquare(city_cost)

print("Vextureure nodany skinny sides:", the best parce allocate many tours.aleoriaution lloudest.triple cost_arm everywhere, city cool by eating two doors.")