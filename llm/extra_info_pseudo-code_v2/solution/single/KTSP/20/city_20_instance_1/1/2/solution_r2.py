import math
import random
from itertools import permutations

# Define the coordinates of each city
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
        perm = perm + (0,)
        current_dist = total_tour_distance(perm)
        if current_dist < best_dist:
            best_dist = current_dist
            best_perm = perm
    return list(best_perm), best_dist

def shake(solution):
    tour = solution[:-1]  # remove the last element since it's a return to depot
    pt = random.sample(range(1, len(tour)), 2)  # Pick two indices to swap, not touching the depot
    pt.sort()
    new_tour = tour[:pt[0]] + list(reversed(tour[pt[0]:pt[1] + 1])) + tour[pt[1] + 1:]
    new_tour.append(0)  # add depot back
    return new_tour, total_tour_distance(new_tour)

def local_search(solution):
    best_tour = solution
    best_cost = total_tour_distance(solution)
    
    for i in range(1, len(solution) - 1):
        for j in range(i + 1, len(solution)):
            if i != 1 or j != len(solution) - 1:  # Ensure not swapping the initial city
                new_tour = solution[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = total_tour_distance(new_tour)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour, new_cost
    
    return best_tour, best_cost

def gvns(itermax, kmax):
    best_solution, best_cost = generate_initial_solution()
    for _ in range(itermax):
        k = 1
        current_solution, current_cost = best_solution, best_cost
        while k <= kmax:
            new_solution, new_cost = shake(current_solution)
            new_solution, new_cost = local_search(new_solution)
            if new_cost < current_cost:
                current_solution, current_cost = new_solution, new_cost
            else:
                k += 1
        if current_cost < best_cost:
            best_solution, best_cost = current_solution, current_cost
    
    return best_solution, best_cost

# GVNS parameters
max_iterations = 50
k_max = 2

# Execute GVNS
final_tour, final_cost = gvns(max_iterations, k_max)

# Output solution
print("Tour:", final_tour)
print("Total travel cost:", final_cost)