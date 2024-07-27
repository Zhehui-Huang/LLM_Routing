import math
import random
from itertools import permutations

# Given data

cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_tour_distance(tour):
    return sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    selected_cities = [0] + random.sample(list(cities.keys())[1:], 6)
    best_perm = None
    best_dist = float('inf')
    for perm in permutations(selected_cities):
        if perm[0] == 0:  # Ensure we start at depot
            current_dist = total_tour_distance(perm + (0,))
            if current_dist < best_dist:
                best_dist = current_dist
                best_perm = perm
    return list(best_perm) + [0], best_dist

def shake(solution, k):
    tour = solution[:-1]  # remove the returning to the depot city
    if k == 1:  # swap two cities in the tour
        i, j = random.sample(range(1, len(tour)), 2)  # choose two cities, not including depot
        tour[i], tour[j] = tour[j], tour[i]
    elif k == 2:  # reverse a subsection
        i, j = sorted(random.sample(range(1, len(tour)), 2))
        tour[i:j+1] = reversed(tour[i:j+1])
    return tour + [0], total_tour_distance(tour + [0])

def local_improvement(solution):
    best_tour, best_dist = solution, total_tour_distance(solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i == 1 and j == len(solution) - 2:
                    continue  # skip swapping endpoints since both are depot
                # try to swap cities i and j
                new_tour = solution[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_dist = total_tour_distance(new_tour)
                if new_dist < best_dist:
                    best_tour, best_dist = new_tour, new_dist
                    improved = True
    return best_tour, best_dist

def gvns(kmax, itermax):
    best_solution, best_cost = generate_initial_solution()
    for _ in range(itermax):
        current_sol, current_cost = best_solution, best_curve
        k = 1
        while k <= kmax:
            shook_sol, shook_cost = shake(current_sol, k)
            new_sol, new_cost = local_improvement(shook_sol)
            if new_cost < current_cost:
                current_sol, current_cost = new_sol, new_cost
                k = 1  # reset k
            else:
                k += 1
        if current_cost < best_cost:
            best_solution, best_cost = current_sol, current_cost
    return best_solution, best_cost

# Set parameters
kmax = 2  # number of neighborhood structures
itermax = 20  # number of iterations

# Run GVNS
tour, cost = gvns(kmax, itermax)

# Output
print("Tour:", tour)
print("Total travel cost:", cost)