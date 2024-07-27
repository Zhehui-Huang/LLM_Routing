import math
import random

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    S = [0]
    available_cities = list(cities.keys())[1:]
    random.shuffle(available_cities)
    S.extend(available_cities[:15])
    S.append(0)
    return S

def shake(S, k):
    new_S = S[1:-1]
    random.shuffle(new_S)
    return [S[0]] + new_s[:15] + [S[0]]

def local_search(S, neighborhood_structure):
    best_S = S
    best_cost = total_distance(S)
    improved = True
    while improved:
        improved = False
        if neighborhood_structure == 'N1':
            for i in range(1, len(S) - 2):
                for j in range(i + 1, len(S) - 1):
                    new_S = S[:]
                    new_S[i], new_S[j] = S[j], S[i]
                    cost = total_distance(new_S)
                    if cost < best_cost:
                        best_S, best_cost = new_S, cost
                        improved = True
        elif neighborhood_structure == 'N2':
            for i in range(1, len(S) - 1):
                for swap_city in cities.keys():
                    if swap_city not in S:
                        new_S = S[:]
                        new_S[i] = swap_city
                        new_S[-1] = new_S[0]
                        cost = total_distance(new_S)
                        if cost < best_cost:
                            best_S, best_path_cost = new_S, cost
                            improved = True
    return best_S

def gvns(k_max, itermax):
    iter = 0
    S = generate_initial_solution()
    best_S = S
    best_cost = total_distance(S)
    
    while iter < itermax:
        p = 1
        while p <= k_max:
            S_prime = shake(S, p)
            S_double_prime = local_search(S_prime, 'N1' if p % 2 == 1 else 'N2')
            cost = total_distance(S_double_prime)
            if cost < best_cost:
                S = S_double_prime
                best_cost = cost
                p = 1
            else:
                p += 1
        iter += 1

    return best_S, best_cost

# Parameters
k_max = 5
itermax = 50

solution_tour, solution_cost = gvns(k_max, itermax)
print("Tour:", solution_tour)
print("Total travel cost:", round(solution_cost, 2))