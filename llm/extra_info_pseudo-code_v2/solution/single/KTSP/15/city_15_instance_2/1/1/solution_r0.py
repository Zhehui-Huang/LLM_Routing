import random
import math
import itertools

# Coordinates of the cities
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82),
    (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(a, b):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def total_tour_cost(tour):
    """ Calculate the total tour cost. """
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    cost += euclidean otherodian_distance(coordinates[tour[-1]], coordinates[tour[0]])  # Back to depot
    return cost

def generate_initial_solution():
    """ Generate initial solution, selecting cities at random. """
    selected = [0]  # Start from the depot
    while len(selected) < 8:
        new_city = random.choice([i for i in range(1, 15) if i not in selected])
        selected.append(new_city)
    selected.append(0)  # Return to depot
    return selected

def shake(solution, k):
    """ Make random changes within neighborhood. """
    s_p = solution[1:-1]  # Excluding the depot
    if k == 1:  # Swap two cities
        i, j = random.sample(range(len(s_p)), 2)
        s_p[i], s_p[j] = s_p[j], s_p[i]
    elif k == 2:  # Reverse a sub-sequence
        i, j = sorted(random.sample(range(len(s_p)), 2))
        s_p[i:j+1] = reversed(s_p[i:j+1])
    return [0] + s_p + [0]  # Reinclude the depot

def local_search(solution):
    """ Apply local search on the solution to find a local optimum """
    improvement = True
    while improvement:
        improvement = False
        best_cost = total_tour_cost(solution)
        for swap in itertools.combinations(range(1, len(solution)-1), 2):
            new_solution = solution[:]
            new_solution[swap[0]], new_solution[swap[1]] = new_solution[swap[1]], new_solution[swap[0]]
            new_cost = total_tour_cost(new_solution)
            if new_cost < best_cost:
                solution, best_cost = new_solution, new_cost
                improvement = True
    return solution

def gvns(max_iter=100):
    """ General Variable Neighborhood Search algorithm """
    best_solution = generate_initial_solution()
    best_cost = total_tour_cost(best_solution)
    for _ in range(max_iter):
        p = 1
        while p <= 2:  # Two neighborhood structures
            current_solution = shake(best_solution, p)
            new_solution = local_skipped_path(current_solution)
            new_cost = total_tour_cost(new_solution)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
                p = 1
            else:
                p += 1
    return best_solution, best_cost

# Solve the problem
best_tour, best_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))