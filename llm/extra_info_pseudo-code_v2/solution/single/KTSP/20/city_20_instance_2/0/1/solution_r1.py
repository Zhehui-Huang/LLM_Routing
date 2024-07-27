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
    solution = [0]  # Start at depot
    available_cities = list(cities.keys())[1:]  # Exclude depot for initial random pick
    while len(solution) < k-1:
        new_city = random.choice(available_cities)
        if new_city not in solution:
            solution.append(new_city)
    solution.append(0)  # End at depot
    return solution

def shake(solution, p):
    """ Generate a solution inside the p-th neighborhood """
    if p == 1:  # Swap two cities in the tour
        s = solution[1:-1]  # Exclude depot for swapping
        i, j = random.sample(range(len(s)), 2)
        s[i], s[j] = s[j], s[i]
        return [0] + s + [0]
    else:  # Reverse a subsequence in the tour
        s = solution[1:-1]
        i, j = sorted(random.sample(range(len(s)), 2))
        s = s[:i] + s[i:j+1][::-1] + s[j+1:]
        return [0] + s + [0]

def local_search(solution, p):
    """ Apply local search on the solution """
    best_score = calculate_total_distance(solution)
    best_sol = solution.copy()
    if p == 1:
        # Try swapping each pair of non-depot cities
        for i in range(1, len(solution) - 1):
            for j in range(i + 1, len(solution)):
                if i == 0 or j == 0:
                    continue
                new_sol = solution[:]
                new_sol[i], new_sol[j] = new_sol[j], newil[i]
                new_score = calculate_total_distance(new_sol)
                if new_score < best_score:
                    best_score, best_sol = new_score, new_sol
    elif p == 2:
        # Reverse any part of the tour between two points
        for i in range(1, len(solution) - 3):
            for j in range(i + 1, len(solution) - 1):
                new_sol = soluti[:]
                new_sol[i:j+1] = reversed(new_sol[i:j+1])
                new_score = calculate_total_distance(new_sol)
                if new_score < best_score:
                    best_score, best_sol = new_score, new_sol
    return best_sol

def vnd(solution):
    """ Variable Neighborhood Descent """
    p = 1
    improved = True
    while improved:
        new_solution = local_search(solution, p)
        if calculate_total_distance(new_solution) < calculate_total_distance(solution):
            solution = new_solution
            p = 1  # Restart search
        else:
            p += 1
            if p > pmax:
                improved = False
    return solution

def gvns():
    """ Main GVNS algorithm """
    best_solution = generate_initial_solution()
    best_score = calculate_total_distance(best_solution)
    iter_count = 0
    while iter_count < itermax:
        p = 1
        while p <= pmax:
            shaken_solution = shake(best_solution, p)
            new_solution = vnd(shaken_solution)
            new_score = calculate_total_distance(new_solution)
            if new_score < best_score:
                best_score, best_solution = new_score, new_solution.copy()
                p = 1  # Solution improved, reset p
            else:
                p += 1
        iter_count += 1
    return best_solution, best_score

# Run GVNS algorithm
tour, cost = gvns()
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")