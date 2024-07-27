import math
import random
from itertools import permutations

# City coordinates
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
        if perm[0] == 0:  # Start at depot
            perm += (0,)  # Override to ensure ending at the depot
            current_dist = total_tour_distance(perm)
            if current_dist < best_dist:
                best_dist = current_dist
                best_perm = perm
    return list(best_perm), best_dist

def shake(solution, k):
    tour = solution[:-1]  # Remove the final repetition of the depot
    modified = tour[1:]  # Exclude the depot for modifications
    random.shuffle(modified)  # Randomize order
    new_tour = [0] + modified + [0] # Reinstate depot as start and end
    return new_tour, total_tour_distance(new_tour)

def local_improvement(solution):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_tour = solution[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
                new_cost = total_tour_distance(new_tohr)
                if new_cost < current_cost:
                    solution, current_cost = new_tour, new_cost
                    improved = True
    return solution, current_cost

def gvns(kmax, itermax):
    best_solution, best_cost = generate_initial_solution()
    for _ in range(itermax):
        k = 1
        while k <= kmax:
            new_solution, new_cost = shake(best_solution, k)
            new_solution, new_cost = local_improvement(new_solution)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
                k = 1  # Improvement found, reset k
            else:
                k += 1  # No improvement, try next neighborhood
    return best_solution, best_cost

kmax = 2  # Maximum neighborhood index
itermax = 20  # Number of iterations in GVNS

tour, cost = gvns(kmax, itermax)

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))