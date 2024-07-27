import math
import random

# Cities coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Parameters for GVNS
k = 10  # Number of cities to visit including the depot
pmax = 2
itermax = 50

def distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

def calculate_total_distance(tour):
    """ Calculate the total distance of a tour """
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    """ Generate an initial solution with k cities randomly """
    available_cities = list(cities.keys())
    solution = [0] + random.sample(available_cities[1:], k-2) + [0]
    return solution

def shake(solution, p):
    """ Generate a solution inside the p-th neighborhood """
    idx = list(range(1, len(solution) - 1))
    random.shuffle(idx)
    s = solution[:]
    if p == 1:  # Swap two cities
        i, j = idx[:2]
        s[i], s[j] = s[j], s[i]
    elif p == 2:  # Reverse a subsection
        i, j = sorted(idx[:2])
        s[i:j+1] = reversed(s[i:j+1])
    return s

def local_search(solution):
    """ Apply a simple local search (2-opt like) on the solution """
    best_score = calculate_total_distance(solution)
    improve = True
    while improve:
        improve = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 2, len(solution) - 1):
                new_solution = solution[:i] + solution[i:j+1][::-1] + solution[j+1:]
                new_score = calculate_total_distance(new_solution)
                if new_score < best_score:
                    solution, best_score = new_solution, new_score
                    improve = True
    return solution

def vnd(solution):
    """ Variable Neighborhood Descent """
    p = 1
    best_solution = solution
    while p <= pmax:
        new_solution = local_search(shake(best_solution, p))
        new_score = calculate_total_distance(new_solution)
        if new_score < calculate_total_distance(best_solution):
            best_solution = new_solution
            p = 1
        else:
            p += 1
    return best_solution

def gvns():
    """ Main GVNS algorithm """
    best_solution = generate_initial_solution()
    best_score = calculate_total_distance(best_solution)
    for _ in range(itermax):
        current_solution = shake(best_solution, random.randint(1, pmax))
        new_solution = vnd(current_solution)
        new_score = calculate_total_distance(new_solution)
        if new_score < best_score:
            best_solution, best_score = new_solution, new_score
    return best_solution, best_score

# Perform the GVNS algorithm
tour, cost = gvns()
print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")